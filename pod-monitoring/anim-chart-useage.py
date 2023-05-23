import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the CPU and Memory stats from the CSV file
df_stats = pd.read_csv('cpu_memory_stats.csv')

# Convert the 'time' column to datetime
df_stats['time'] = pd.to_datetime(df_stats['time'])

# Create a figure with two subplots
fig, (ax_cpu, ax_memory) = plt.subplots(1, 2, figsize=(10, 5))

# Initialize empty data for CPU and memory usage
cpu_data = []
memory_data = []

# Function to update the bar charts with new data
def update_chart(frame):
    # Get the latest CPU and memory usage data from the CSV file
    # Here, I'm assuming the CSV file is already loaded into the DataFrame 'df_stats'
    cpu_usage = df_stats['cpu'].iloc[frame]
    memory_usage = df_stats['memory'].iloc[frame]

    # Update the data lists
    cpu_data.append(cpu_usage)
    memory_data.append(memory_usage)

    # Clear the current axes
    ax_cpu.clear()
    ax_memory.clear()

    # Plot the CPU usage bar chart
    ax_cpu.bar('CPU Usage', cpu_data[-1], color='blue', width=0.4)
    ax_cpu.set_ylabel('CPU Usage')

    # Plot the memory usage bar chart
    ax_memory.bar('Memory Usage', memory_data[-1], color='green', width=0.4)
    ax_memory.set_ylabel('Memory Usage')

    # Set appropriate y-axis limits
    ax_cpu.set_ylim(0, max(cpu_data))
    ax_memory.set_ylim(0, max(memory_data))

    # Set the chart titles
    ax_cpu.set_title('CPU Usage')
    ax_memory.set_title('Memory Usage')

# Create an animation using the update_chart function
ani = animation.FuncAnimation(fig, update_chart, frames=len(df_stats), interval=1000)

# Display the animated bar charts
plt.show()

