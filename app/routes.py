from flask import jsonify, request
from app import app
from app.models import Car
import transaction

@app.route('/car', methods=['POST'])
def register_car():
    data = request.get_json()
    brand = data['brand']
    model = data['model']
    license_plate = data['license_plate']
    color = data['color']
    car = Car(brand, model, license_plate, color)
    app.root[license_plate] = car
    transaction.commit()
    return jsonify({'message': 'Car registered successfuly'}), 201


@app.route('/car', methods=['GET'])
def get_cars():
    cars = []
    for key, value in app.root.items():
        if isinstance(value, Car):
            cars.append({'brand': value.brand, 'model': value.model, 'license plate': value.license_plate, 'color': value.color})
    return jsonify(cars)

@app.route('/car/<string:license_plate>', methods=['GET'])
def get_car_by_license_plate(license_plate):
    if license_plate not in app.root:
        return jsonify({'error': 'License plate not found'}), 404
    
    car = app.root[license_plate]

    car_data = {
        'brand': car.brand,
        'model': car.model,
        'license_plate': car.license_plate,
        'color': car.color
    }

    return jsonify(car_data), 200

@app.route('/car', methods=['DELETE'])
def delete_car():
    data = request.get_json()
    license_plate = data['license_plate']

    if license_plate not in app.root:
        return jsonify({'error': 'Car not found'}), 404
    
    del app.root[license_plate]
    transaction.commit()

    return jsonify({'message': f'Car with license plate "{license_plate}" deleted successfuly'}), 200