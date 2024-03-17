# Car Register API

## About
This is a Flask API developed to manage items in a Object-Oriented Database(ZODB). It allows users to perform CRUD operations on items stored in the database.

## Requirements to run this application
- Python 3
- Flask 3.0.2
- ZODB (Zope Object Database) 5.8.1
- Docker an Docker Compose (Optional)

## How to run the application
### With Python
1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run it with python3:
    ```bash
    python3 run.py
    ```

### With Docker Compose
1. Just run the following command:
    ```bash
    docker compose up
    ```
    You can use the **-d** flag in the end of the command if you want it running on background


## TODO
### HTTP Routes with Curl Examples



<!-- 
### Create Item
- **Method**: POST
- **Endpoint**: `/items`
- **Description**: Creates a new item in the database.
- **Example**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item", "description": "Item description"}' http://localhost:5000/items -->
