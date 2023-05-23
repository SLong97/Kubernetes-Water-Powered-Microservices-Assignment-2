import requests
import pika
import time

credentials = pika.PlainCredentials('admin', 'admin')
# Set up a connection to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.43.136.9', port=5672, credentials=credentials) # rabbitmq service IP and PORT
)
channel = connection.channel()

signup_details = {"email": "eggxample1234@gmail.com", "username": "eggxample1234", "password": "Example1234"}
# Send a POST request to the /signup endpoint
signup_response = requests.post('http://localhost:30000/signup', data=signup_details)
# Check that the signup was successful
assert signup_response.status_code == 200, f'Signup failed with status code {signup_response.status_code}'


login_details = {"email": "eggxample1234@gmail.com", "password": "Example1234"}
# Send a POST request to the /login endpoint
login_response = requests.post('http://localhost:30000/login', data=login_details)
# Check that the login was successful
assert login_response.status_code == 200, f'login failed with status code {login_response.status_code}'


print('Successfully signed up and logged in user:', signup_details['username'], '\n')

print('Attempting to access the following endpoints for testing \"user_activity\" RabbitMQ queue\n\"/\", \"/store\", \"/recommendations\", \"/profile\"\n')


endpoints = ["/", "/store", "/recommendations", "/profile"]

for endpoint in endpoints:
    # Construct the full URL for each endpoint
    url = f'http://localhost:30000{endpoint}'
    
    # Send a GET request to the endpoint
    response = requests.get(url)
    
    # Check that the response status code is 200
    assert response.status_code == 200, f'Expected status code 200 but got {response.status_code} for endpoint {endpoint}'
    
    print(f'Successfully accessed endpoint \"{endpoint}\" with status code {response.status_code}')

    method_frame, header_frame, body = channel.basic_get('user_activity')
    if method_frame:
       print(f'Received message --> {body} in RabbitMQ queue \"user_activity\"\n')
    	# Acknowledge the message
       channel.basic_ack(method_frame.delivery_tag)
    else:
       print('No message returned\n')

