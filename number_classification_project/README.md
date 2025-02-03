# Number Classifications API

## Project Overview
This project provides an API to classify numbers and provide facts about them. It allows users to query a number and get various classifications, including whether the number is prime, perfect, Armstrong (narcissistic), even or odd, and other fun mathematical facts.

## Table of Contents
1. [Technologies](#technologies)
2. [Setup](#setup)
3. [Features](#features)
3. [API Documentation](#api-documentation)
3. [Running Locally](#running-locally)
4. [Deploying to Production](#deploying-to-production)

## Technologies
- **Django** (v5.1.5) – Python web framework
- **SQLite** – Database
- **Gunicorn** – WSGI HTTP Server for UNIX
- **Render**  – Deployment platforms

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/samuelhetty/HNG-Python-Backend.git
cd number_classification_project
```

### 2. Install Dependencies

pip install -r requirements.txt

# **Features**

- Prime Check: Determines if a number is prime.
- Perfect Number Check: Determines if a number is perfect (the sum of its divisors equals the number).
- Armstrong (Narcissistic) Number Check: Determines if a number is an Armstrong (narcissistic) number.
- Even/Odd Check: Classifies the number as either even or odd.
- Digit Sum: Provides the sum of the digits of the number.
- Fun Fact: Retrieves a fun mathematical fact about the number from an external API.

# **API Documentation **

## Base URL
The base URL for all API requests is: https://number-classification-7q0m.onrender.com

### GET `/api/classify-number/?number=`

#### API Usage
The main endpoint for number classification is /api/classify-number/. You can pass the number parameter as a query string to classify a number.

Example Request
To classify the number 371, send a GET request to the following URL:


http://127.0.0.1:8000/api/classify-number/?number=371
Example Response
A valid response might look like this:

``` Json
[ 
  {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
  }
]
```
If you pass an invalid number (e.g., "alphabet"), the response will be:
``` Json
[
  { 
     "number": "alphabet",
     "error": true
  }

]
```

## Running Locally

### 1. Apply Migrations
Make sure your database is set up:

python manage.py migrate

### 2. Run the Development Server

python manage.py runserver


## Deploy
Follow the platform's guide to create a new project. For example, on Render:

- Create a new web service.
- Connect your repository.
- Set up environment variables (e.g., DJANGO_SECRET_KEY, DATABASE_URL).
- Configure the Root Directory (if needed).

## Start Deployment
Trigger the deployment, and once successful, your app will be live.

### License
This project is licensed under the MIT License – see the LICENSE file for details.

### Programming language - [PYTHON](https://hng.tech/hire/python-developers)



## Authors

- [Henrietta Onoge](https://github.com/Samuelhetty)