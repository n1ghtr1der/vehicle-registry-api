from flask import jsonify, request
from app import app
from app.models import Car
from app.database import init_database, close_connection
import transaction

@app.route('/register', methods=['POST'])
def register_car():
    data = request.get_json()
    brand = data['brand']
    model = data['model']
    license_plate = data['license_plate']
    color = data['color']

    root, connection, db = init_database()
    car = Car(brand, model, license_plate, color)
    root[license_plate] = car
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': 'Car registered successfuly'}), 201


@app.route('/car', methods=['GET'])
def get_cars():
    root, connection, db = init_database()
    cars = []

    for key, value in root.items():
        if isinstance(value, Car):
            cars.append({'brand': value.brand, 'model': value.model, 'license plate': value.license_plate, 'color': value.color})
    
    close_connection(db, connection)
    return jsonify(cars)

@app.route('/car/<string:license_plate>', methods=['GET'])
def get_car_by_license_plate(license_plate):
    root, connection, db = init_database()

    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'License plate not found'}), 404
    
    car = root[license_plate]

    car_data = {
        'brand': car.brand,
        'model': car.model,
        'license_plate': car.license_plate,
        'color': car.color
    }

    close_connection(db, connection)
    return jsonify(car_data), 200

@app.route('/remove-car/<string:license_plate>', methods=['DELETE'])
def delete_car(license_plate):
    root, connection, db = init_database()

    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'Car not found'}), 404
    
    del root[license_plate]
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': f'Car with license plate "{license_plate}" deleted successfuly'}), 200

@app.route('/update-car/<string:license_plate>', methods=['PUT'])
def update_car(license_plate):
    data = request.json
    root, connection, db = init_database()
    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'Car not found'}), 404
    
    car = root[license_plate]
    car.brand = data['brand']
    car.model = data['model']
    car.color = data['color']
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': 'Car info updated'})
