from flask import Flask

app = Flask(__name__)

cars = [{
        "brand": {
            "honda": [
                "accord", "civic"
            ],
             "kia": [
                "sportage", "ceed"
             ] ,
             "bmw": [
                "s3", "x5"
             ]
        }
    
}
]

@app.get("/cars")  # http://127.0.0.1:5000/cars
def get_cars():
    return {"cars": cars}
    
@app.post("/cars")
def add_car():
    request_data = request.get_json()
    new_car = {"brand": request_data["brand"]}
    cars.append(new_car)
    return new_car, 201

@app.post("/cars/<string:brand>")
def newcar(brand):
    request_data = request.get_json()
    for car in cars:
        if car["brand"] == brand:
            new_car1 = {"brand": request_data["brand"]}
            cars["brand"].append(new_car1)
            return new_car1, 201
    return {"message": "Something when wrong!"}, 404