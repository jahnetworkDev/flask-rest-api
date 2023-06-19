from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome, we sell and buy used cars."

cars_inventory = [
{   
    'id' : '1',
    'year' : 2000,
    'brand' : 'honda',
    'model' : 'civic',
    'color' : 'gray'
},
{
    'id' : '2',
    'year' : 2004,
    'brand' : 'honda',
    'model' : 'accord',
    'color' : 'blue'
},
{
    'id' : '3',
    'year' : 2013,
    'brand' : 'hyundai',
    'model' : 'sonata',
    'color' : 'white'
},
{
    'id' : '4',
    'year' : 2000,
    'brand' : 'bmw',
    'model' : 218,
    'color' : 'navy'
}
]

"""Display all cars"""
@app.route('/cars/inventory', methods=['GET'])
def getAllCar():
    return jsonify({'cars':cars_inventory})

"""Display the requested car"""
@app.route('/cars/inventory/<carId>', methods=['GET'])
def getCarId(carId):
    cars = [ car for car in cars_inventory if (car['id'] == carId) ]
    return jsonify({'car':cars})

@app.route('/cars/inventory/<carId>', methods=['PUT'])
def updateCarId(carId):
    cars = [ car for car in cars_inventory if (car['id'] == carId) ]
    if 'year' in request.json:
        cars[0]['year'] = request.json['year']
    if 'brand' in request.json:
        cars[0]['brand'] = request.json['brand']
    if 'model' in request.json:
        cars[0]['model'] = request.json['model']
    if 'color' in request.json:
        cars[0]['color'] = request.json['color']

@app.route('/cars/inventory',methods=['POST'])
def createCar(): 
    dat = {
    'id':request.json['id'],
    'year':request.json['year'],
    'brand':request.json['brand'],
    'model':request.json['model'],
    'color':request.json['color']
    }
    cars_inventory.append(dat)
    return jsonify(dat)

@app.route('/cars/inventory/<carId>',methods=['DELETE'])
def deleteEmp(carId): 
    cars = [ car for car in cars_inventory if (car['id'] == carId) ] 
    if len(cars) == 0:
        abort(404) 

    cars_inventory.remove(cars[0])
    return jsonify({'response':'Success'})

if __name__ == "__main__":
    app.run()


