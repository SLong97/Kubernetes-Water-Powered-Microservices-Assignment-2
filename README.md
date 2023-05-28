# Kubernetes-Water-Powered-Microservices-Assignment-2

## Overview

You must take your assignment 1 application and move it to a Kubernetes environment (e.g. using
k3s). You must also implement testing and monitoring for the application.

## Task 1 - Move to Kubernetes

Get your application running using Kubernetes, create a Docker Hub repository for each service.
You must scale the pods (using deployments), but be careful not to overload your system. Exactly
how many replicas you have isn’t hugely important.

## Task 2 - Testing and Monitoring

You are to address the testing and monitoring of your application. You are to develop 1 functional
test, 1 non-functional test, and 1 monitoring solution for your application.

### 1. Functional Test

Develop a test that tests whether your application is functioning correctly. You need only test 1 part
of your application.

#### RabbitMQ - Python Test Script

![Screenshot from 2023-05-12 20-35-56](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/a6703761-316d-4efe-a112-3343f5e934ad)

#### RabbitMQ - Test Run

![Screenshot from 2023-05-12 20-37-21](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/a004e507-43f1-410f-bc9c-0e357f644a27)

#### RabbitMQ - Web App Example

![Screenshot from 2023-05-12 20-40-47](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/173dd308-5251-40e9-a7fb-13c16e3ac399)

***

### Additional Functional Test - gRPC Recommendations Service Postman Test

#### Request & Response

![Screenshot from 2023-05-12 20-31-28](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/a4472e9a-558b-4cfc-b2b8-d41c1659ce3a)

#### Test Scripts & Results

![Screenshot from 2023-05-12 20-30-07](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/190c4df9-feda-477e-a682-c61fc6fc9889)

![Screenshot from 2023-05-12 20-32-58](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/92d1d047-52e0-47df-b11b-3b15ce397356)

***

### 2. Non-functional Test

Develop a test that test how your application performs from 1 qualitative standpoint – e.g.
responsiveness, security, load, failover, etc.

#### Gatling - Ramping up to 100 users over the course of 60 seconds

![Screenshot from 2023-05-13 18-16-56](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/bef30bc3-a7b4-4dee-b93b-a0fef4e02e6f)

#### Gatling - Generated HTML visualisations

![Screenshot 2023-05-13 at 18-18-52 Gatling Stats - Global Information](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/2574f329-0429-4d22-8a29-d20b17618b93)

![Screenshot 2023-05-13 at 18-21-38 Gatling Stats - Global Information](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/b51a9faf-0735-496e-96e1-2e93999d0500)



### 3. Monitoring solution

Develop using whatever tool(s) you choose a monitoring solution for your application.

#### Pod Monitoring - Monitoring Pods while running Gatling test

![Screenshot from 2023-05-14 13-27-37](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/f27736bb-edf3-4c07-8e9a-cc2931625339)

#### Pod Monitoring - Web App CPU & Memory Useage Visualisation

![Screenshot from 2023-05-14 13-28-18](https://github.com/SLong97/Kubernetes-Water-Powered-Microservices-Assignment-2/assets/91565384/18b43560-09f5-4231-a3ad-0a2ab3b24252)
