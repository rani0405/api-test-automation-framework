# API Test Automation Framework

## Overview

This project is an automated API testing framework built using Python and Pytest to validate backend services.

## Tech Stack

* Python
* Pytest
* Requests
* Allure Reports
* Pytest-xdist

## Project Structure

* tests → test cases
* utils → reusable code
* data → test data
* schemas → schema validation

## How to Run

```bash
 py -m pytest
```

## Reporting

```bash
py -m pytest --alluredir=allure-results
allure serve allure-results
```

## Features

* Positive & Negative Testing
* Schema Validation
* Parallel Execution
* Logging
* CI/CD Ready

## Design Decisions

* Used API Client for reusability
* Used fixtures for test data
* Externalized test data for scalability
* Added schema validation for strong assertions
