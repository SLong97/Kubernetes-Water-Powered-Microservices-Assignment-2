import os
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from kubernetes import client, config
from tabulate import tabulate

# Load config from default location
config.load_kube_config("/etc/rancher/k3s/k3s.yaml")

v1 = client.CoreV1Api()

# Create an instance of the low-level API client
api_client = client.ApiClient()

refresh_interval = 10  # Refresh interval in seconds
max_refresh_times = 12  # Maximum number of refreshes

# DataFrame for storing CPU and Memory stats
df_stats = pd.DataFrame(columns=['time', 'cpu', 'memory'])

refresh_count = 0

while True:
    # Clear the screen
    os.system('clear' if os.name == 'posix' else 'cls')

    print("Listing pods with their IPs, Status, Nodes and Resource Usage:")
    ret = v1.list_pod_for_all_namespaces(watch=False)

    # Create a list to hold all the data rows
    data_rows = []

    for i in ret.items:
        # Only request metrics for running pods
        if i.status.phase == "Running":
            pod_info = [i.metadata.namespace, i.metadata.name, i.status.pod_ip, i.status.phase, i.spec.node_name]

            # Make a HTTP request to the Metrics API
            response = api_client.call_api(
                f"/apis/metrics.k8s.io/v1beta1/namespaces/{i.metadata.namespace}/pods/{i.metadata.name}", 
                "GET",
                auth_settings = ['BearerToken'],
                response_type="json",
                _preload_content=False,
            )
            
            data = json.loads(response[0].data)

            # Iterate over the containers in the pod
            for container in data['containers']:
                container_info = pod_info + [container['name'], container['usage']['cpu'], container['usage']['memory']]
                data_rows.append(container_info)

                # Check if this is the pod we are interested in
                if i.metadata.name == 'flask-web-app-deploy-85799cc8db-xtdcz':
                    new_data = pd.DataFrame({'time': [time.strftime("%Y-%m-%d %H:%M:%S")],
                                             'cpu': [container['usage']['cpu'].strip('n')],
                                             'memory': [container['usage']['memory'].strip('Ki')]})
                    df_stats = pd.concat([df_stats, new_data], ignore_index=True)
                
                
    df_stats.to_csv('cpu_memory_stats.csv', index=False)

    # Define the table headers
    headers = ['Namespace', 'Pod Name', 'Pod IP', 'Status', 'Node', 'Container', 'CPU Usage', 'Memory Usage']

    # Print the data in a tabular format
    print(tabulate(data_rows, headers=headers, tablefmt='pretty'))

    # Countdown until the next refresh
    for i in range(refresh_interval, 0, -1):
        print(f"Refreshing in {i} seconds...", end='\r')
        time.sleep(1)

    # Increment refresh count
    refresh_count += 1

    # If max refresh count is reached, break the loop
    if refresh_count >= max_refresh_times:
        break

# Load the CPU and Memory stats from the CSV file
df_stats = pd.read_csv('cpu_memory_stats.csv')

# Convert the 'time' column to datetime
df_stats['time'] = pd.to_datetime(df_stats['time'])

# Create a figure with two subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Plot CPU usage
axes[0].plot(df_stats['time'], df_stats['cpu'])
axes[0].set_ylabel('CPU Usage')

# Plot Memory usage
axes[1].plot(df_stats['time'], df_stats['memory'])
axes[1].set_ylabel('Memory Usage')

# Format x-axis labels as dates
date_format = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
for ax in axes:
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_tick_params(rotation=45)

# Set overall title for the figure
fig.suptitle('CPU and Memory Usage Over Time')

# Adjust spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()


