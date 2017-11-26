# Lab 2: Create a Serverless API using Azure Functions


## Overview

Serverless services allow application developers to write, deploy, and run code without worrying about underlying infrastructure. In addition to this, they are typically have micro-billing (sub-second or per-second billing). There are Serverless offerings from Amazon (Lambda), Google (Cloud Functions), and Azure (Functions) - we will focus on using Azure Functions for this course. It provides 1 million free requests (*Note*: You have to pay for underlying storage but it's cents per GB and for bandwidth greater than 5GB/monthly). 

Functions allow us to decompose larger monoliths, but is especially great for small pieces of code, or "functions", that run in the cloud. You can write just the code you need for the problem at hand, without worrying about a whole application or the infrastructure to run it. Pay only for the time your code runs and the underlying platform does the heavy lifting.


## Lab Links

- [Azure](https://azure.microsoft.com)
- [Azure Functions](https://azure.microsoft.com/en-us/services/functions/)
- [Azure Fucntions: Best Practices](https://docs.microsoft.com/en-us/azure/azure-functions/functions-best-practices)

## What is a function?

An function (in context of the cloud) is an independent unit of deployment, like a microservice. You may also here people refer to "functions" as *serverless* because the platform takes care of scale out. It's merely code, deployed in the cloud, that is most often written to perform a single job such as:

- Updating/creating a user to the database
- Processing an image before it's stored to a blob
- Performing a recurring scheduled task

You can perform multiple jobs in your code, but [best practices](https://docs.microsoft.com/en-us/azure/azure-functions/functions-best-practices) don't recommend that without good reason. Separation of concerns is best. More info can be found at [Functions Overview](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) including features and example triggers.

### Sign up for Azure 

If you don't already have an Azure subscription you can [sign up here](https://azure.microsoft.com/en-us/free/). If you haven't signed up for this before you'll get a free trail that includes $200 of free credit. Note that this guide will focus on Azure Functions, however if you prefer another provider that's fine (we just won't focus on it).

## Building a Web API using Azure Functions

We are going to create and deploy a "Hello, {name}!" application.

Follow the guide (approx. 20 or less mins) and then we will create our own Function.

- [Create your first Azure Function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function)

## Use Case 2 - Live Edition

Deploy a cost-effective Web API to use centralView from any browser.