# FAST API

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run App](#run-App)
  - [Run Tests](#run-tests)
- [Handling Errors](#handling-errors)

## Overview
This Project is demo for running FastAPI using poetry. API is used for extracting sentiment scores from the given input text.

## Getting Started

### Prerequisities

- git
- poetry

### Installation

1. Clone the Repository

    ```bash
    git clone https://github.com/jivaniyash/fast_api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fast_api
    ```

3. Install dependencies from py
    ```bash
    poetry install
    ```

    ```bash
    poetry run pip install pydantic[dotenv]
    ```
## Usage

### Run App

To run the app:
```bash
poetry run app
```

### Run Tests

To run tests
```bash
poetry run pytest --cov=app --cov-report term-missing
```

## Handling Errors

- If there is any error running code with poetry, create a python virtual environment and install poetry using `pip install poetry`.


- If you still face error, 
    - use `requirements.txt` to install dependencies using `pip install -r requirements.txt --quiet`
    - run in shell `uvicorn main:app --reload` to start server