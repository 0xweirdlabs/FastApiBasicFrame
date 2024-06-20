# FastApiBasic

This project serves as a starting template for building FastAPI applications with some standard functionality in place, such as Prometheus metrics for monitoring, modular route handling, and environment-specific configurations.


## Installation

### 1. Clone the repository:

```shell
git clone <repository_url>
cd FastApiBasic
```


### 2. Set up a virtual environment:
```shell
python -m venv .venv
```

### 3. Activate the virtual environment:

**On Windows:**
```shell
source .venv/bin/activate
```

On macOS/Linux:
```shell
source .venv/bin/activate
```

### 4.Install dependencies:

```shell
pdm install
```

Run the application:

***For local environment:***
```shell
pdm run start-local
```
***For development environment:***
```shell
pdm run start-dev
```
***For production environment:***
```shell
pdm run start-prod
```

## Directory Structure


````css
FastApiBasic/
│
├── src/
│   └── fastapibasic/
│       ├── __init__.py
│       ├── config.py
│       ├── datasource.py
│       ├── main.py
│       ├── prometheus.py
│       ├── routes.py
│       └── transform.py
├── .env.local
├── .env.dev
├── .env.prod
├── pyproject.toml
├── run_server.py
├── pdm.lock
└── README.md

````

## Purpose of Each File


#### src/fastapibasic/config.py:

Manages environment-specific settings and configurations. Uses pydantic_settings for configuration management and python-dotenv for loading environment variables from .env files.

#### src/fastapibasic/datasource.py:

Contains functions that interact with data sources, such as databases or external APIs. This file centralizes all data fetching logic.

#### src/fastapibasic/main.py:

The main entry point of the FastAPI application. It includes middleware, routes, and Prometheus metrics setup.

#### src/fastapibasic/prometheus.py:
Contains all Prometheus-related functionality, including metrics definitions and middleware for tracking requests and HTTP status codes.

#### src/fastapibasic/routes.py:
Defines the API endpoints using FastAPI's APIRouter. It organizes the routes separately to keep the main application file clean.

#### src/fastapibasic/transform.py:
Contains functions that transform data from data sources into the format needed by the application or for responses.

#### .env.local, .env.dev, .env.prod:
Environment-specific configuration files. These files contain environment variables that configure the application for different environments (local, development, production).
pyproject.toml:

#### run_server.py:

A simple script to run the FastAPI application with environment-specific settings. It reads the environment from command-line arguments and sets it before starting the server.
pdm.lock:

## Standard Functionality in Place

**Prometheus Metrics:**
- Integrated Prometheus metrics for monitoring request counts and HTTP status codes.
Environment-specific Configuration:
- Manages configurations for different environments using .env files and the pydantic_settings package.
Modular Route Handling:
- Routes are defined in a separate file (routes.py) to keep the main application file clean and organized.

 
## How to Extend

**Adding New Routes:**
Define new endpoints in the routes.py file using FastAPI's APIRouter.

**Adding New Data Sources:**
Add new functions in the datasource.py file to interact with additional data sources.

**Adding New Transformations:**
Add new functions in the transform.py file to transform data as needed.

**Extending Prometheus Metrics:**
Add new metrics in the prometheus.py file to monitor additional aspects of your application.