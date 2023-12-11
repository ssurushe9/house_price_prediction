import pickle
import numpy as np


with open("linear_regression.pkl",'rb') as f:
    model = pickle.load(f)

def predicted_price(transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude):
        
    

    test_array = np.zeros([1,model.n_features_in_])
    test_array[0,0] = transaction_date
    test_array[0,1] = house_age
    test_array[0,2] = distance_to_the_nearest_MRT_station
    test_array[0,3] = number_of_convenience_stores
    test_array[0,4] = latitude
    test_array[0,5] = longitude

    predicted_house_price = np.around(model.predict(test_array)[0],1)
    return predicted_house_price


