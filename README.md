# Vehicle Register API

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


## HTTP Routes with Curl Examples

### Register vehicle
- **Method**: POST
- **Endpoint**: `/register`
- **Description**: Adds a new vehicle in the database.
- **Example**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"brand": "mazda", "model": "miata", "license_plate": "NQS8051", "color": "red"}' http://localhost:5000/register
  ```

### List all vehicles
- **Method**: GET
- **Endpoint**: `/vehicles`
- **Description**: Lists all vehicles from the database.
- **Example**
  ```bash
  curl http://localhost:5000/vehicles
  ```

### List a specific vehicle
- **Method**: GET
- **Endpoint**: `/vehicles/<license_plate>`
- **Description**: List a vehicle by license plate
- **Example**:
  ```bash
  curl http://localhost:5000/vehicle/NQS8051

### Update vehicle information
- **Method**: PUT
- **Endpoint**: `/update-vehicle/<license_plate>`
- **Description**: Updates a vehicle's information, except the license plate
- **Example**:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"brand": "chevrolet", "model": "monza", "color": "silver"}' http://localhost:5000/update-vehicle/NQS8051

### Delete vehicle from database
- **Method**: DELETE
- **Endpoint**: `/remove-vehicle/<license_plate>`
- **Description**: Removes a vehicle from database by it's license plate
- **Example**:
  ```bash
  curl -X DELETE http://localhost:5000/remove-vehicle/NQS8051
