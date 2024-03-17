from flask import jsonify, request
from app import app
from app.models import Vehicle
from app.database import init_database, close_connection
import transaction

@app.route('/register', methods=['POST'])
def register_vehicle():
    data = request.get_json()
    brand = data['brand']
    model = data['model']
    license_plate = data['license_plate']
    color = data['color']

    root, connection, db = init_database()
    vehicle = Vehicle(brand, model, license_plate, color)
    root[license_plate] = vehicle
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': 'Vehicle registered successfuly'}), 201


@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    root, connection, db = init_database()
    vehicles = []

    for key, value in root.items():
        if isinstance(value, Vehicle):
            vehicles.append({'brand': value.brand, 'model': value.model, 'license plate': value.license_plate, 'color': value.color})
    
    close_connection(db, connection)
    return jsonify(vehicles)

@app.route('/vehicle/<string:license_plate>', methods=['GET'])
def get_vehicle_by_license_plate(license_plate):
    root, connection, db = init_database()

    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'License plate not found'}), 404
    
    vehicle = root[license_plate]

    vehicle_data = {
        'brand': vehicle.brand,
        'model': vehicle.model,
        'license_plate': vehicle.license_plate,
        'color': vehicle.color
    }

    close_connection(db, connection)
    return jsonify(vehicle_data), 200

@app.route('/remove-vehicle/<string:license_plate>', methods=['DELETE'])
def delete_vehicle(license_plate):
    root, connection, db = init_database()

    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'vehicle not found'}), 404
    
    del root[license_plate]
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': f'Vehicle with license plate "{license_plate}" deleted successfuly'}), 200

@app.route('/update-vehicle/<string:license_plate>', methods=['PUT'])
def update_vehicle(license_plate):
    data = request.json
    root, connection, db = init_database()
    if license_plate not in root:
        close_connection(db, connection)
        return jsonify({'error': 'Vehicle not found'}), 404
    
    vehicle = root[license_plate]
    vehicle.brand = data['brand']
    vehicle.model = data['model']
    vehicle.color = data['color']
    transaction.commit()

    close_connection(db, connection)
    return jsonify({'message': 'Vehicle info updated'})
