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