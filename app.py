from flask import Flask,render_template,request
from utils import predicted_price
import config



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict_house_price',methods = ["GET","POST"])
def price():

    if request.method == "GET":

        data = request.form
    
        transaction_date                    = data['transaction_date']
        house_age                           = float(data('house_age'))
        distance_to_the_nearest_MRT_station = float(data('distance_to_the_nearest_MRT_station'))
        number_of_convenience_stores        = float(data('number_of_convenience_stores'))
        latitude                            = float(data('latitude'))
        longitude                           = float(data('longitude'))

        predict_house_price = predicted_price(transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude)
    

        return render_template("index.html",Predict_Price="The predicted house price is {} ".format(predict_house_price))
    
    elif request.method == "POST":

         data = request.form
    
         transaction_date                    = data['transaction_date']
         house_age                           = data['house_age']
         distance_to_the_nearest_MRT_station = data['distance_to_the_nearest_MRT_station']
         number_of_convenience_stores        = data['number_of_convenience_stores']
         latitude                            = data['latitude']
         longitude                           = data['longitude']

         predict_house_price = predicted_price(transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude)


         return render_template("index.html",Predict_Price="The predicted house price is {} ".format(predict_house_price))

    

if __name__ == "__main__":
    app.run(host = config.HOST_NAME,port = config.PORT_NUMBER,debug=True)


