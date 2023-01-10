# fastapi
A simple fast api server

# Table of Contents
[Intoduction](#Introduction) 

[Getting Started](#getting-started)

[Development Setup](#development-setup)

[API Walkthrough](#api-walkthrough)

[Testing](#testing)

[Live](#live-server)

## Introduction
This is a simple fast api server with two apis. a home api that returns hello world and a get products api that Can be filtered by `category` as a query parameter and Can be filtered by `price_less_than` as a query parameter, returns products that meet these criteria.- Returns a list of products with the given discounts applied where necessary.
- When a product does not have a discount, `price.final` and `price.original` should be the same number and `discount_percentage` should be null.
- When a product has a discount `price.original` is the original price, `price.final` is the amount with the discount applied and `discount_percentage` represents the applied discount with the % sign

## Overview
## Getting Started

### Installing Dependencies

#### Python 3.10

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/fast_api` directory and running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Fast Api](https://fastapi.tiangolo.com/) FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

- [SQLAlchemy](https://www.sqlalchemy.org/) libraries to handle the lightweight sqlite database. 


### **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

### **Install the dependencies:**
```
pip install -r requirements.txt
```

### **Dump csv file to postgres database:**
```
python import.py
```


### **Run the development server:**

```
uvicorn main:app --reload
```

### **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000](http://localhost:8000) 

or swagger docs
Navigate to project homepage [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Testing
```bash

pytest
```