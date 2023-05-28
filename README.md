# Kubernetes-Water-Powered-Microservices-Assignment-2

## Overview

You must take your assignment 1 application and move it to a Kubernetes environment (e.g. using
k3s). You must also implement testing and monitoring for the application.

## Task 1 - Move to Kubernetes

Get your application running using Kubernetes, create a Docker Hub repository for each service.
You must scale the pods (using deployments), but be careful not to overload your system. Exactly
how many replicas you have isn’t hugely important.

![Screenshot from 2023-05-13 12-12-36](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/misc%20images/Screenshot%20from%202023-05-13%2012-12-36.png)

## Task 2 - Testing and Monitoring

You are to address the testing and monitoring of your application. You are to develop 1 functional
test, 1 non-functional test, and 1 monitoring solution for your application.

### 1. Functional Test

Develop a test that tests whether your application is functioning correctly. You need only test 1 part
of your application.

#### RabbitMQ - Python Test Script

![Screenshot from 2023-05-12 20-35-56](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-script/User%20Activity%20RabbitMQ%20service/Screenshot%20from%202023-05-12%2020-35-56.png)

#### RabbitMQ - Test Run

![Screenshot from 2023-05-12 20-37-21](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-script/User%20Activity%20RabbitMQ%20service/Screenshot%20from%202023-05-12%2020-37-21.png)

#### RabbitMQ - Web App Example

![Screenshot from 2023-05-12 20-40-47](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-script/User%20Activity%20RabbitMQ%20service/Screenshot%20from%202023-05-12%2020-40-47.png)

***

### Additional Functional Test - gRPC Recommendations Service Postman Test

#### Request & Response

![Screenshot from 2023-05-12 20-31-28](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-postman/Recommendation%20GRPC%20service/Screenshot%20from%202023-05-12%2020-31-28.png)

#### Test Scripts & Results

![Screenshot from 2023-05-12 20-30-07](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-postman/Recommendation%20GRPC%20service/Screenshot%20from%202023-05-12%2020-30-07.png)

![Screenshot from 2023-05-12 20-32-58](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/functional-test-postman/Recommendation%20GRPC%20service/Screenshot%20from%202023-05-12%2020-32-58.png)

***

### 2. Non-functional Test

Develop a test that test how your application performs from 1 qualitative standpoint – e.g.
responsiveness, security, load, failover, etc.

#### Gatling - Ramping up to 100 users over the course of 60 seconds

![Screenshot from 2023-05-13 18-16-56](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/non-functional-load-testing-gatling/Screenshot%20from%202023-05-13%2018-16-56.png)

#### Gatling - Generated HTML visualisations

![Screenshot 2023-05-13 at 18-18-52 Gatling Stats - Global Information](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/non-functional-load-testing-gatling/Screenshot%202023-05-13%20at%2018-18-52%20Gatling%20Stats%20-%20Global%20Information.png)

![Screenshot 2023-05-13 at 18-21-38 Gatling Stats - Global Information](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/non-functional-load-testing-gatling/Screenshot%202023-05-13%20at%2018-21-38%20Gatling%20Stats%20-%20Global%20Information.png)



### 3. Monitoring solution

Develop using whatever tool(s) you choose a monitoring solution for your application.

#### Pod Monitoring - Monitoring Pods while running Gatling test

![Screenshot from 2023-05-14 13-27-37](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/pod-monitoring/Screenshot%20from%202023-05-14%2013-27-37.png)

#### Pod Monitoring - Web App CPU & Memory Useage Visualisation

![Screenshot from 2023-05-14 13-28-18](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/blob/main/pod-monitoring/Screenshot%20from%202023-05-14%2013-28-18.png)
