from sklearn.linear_model import Ridge
import pickle
import numpy as np


"""
    Reshape inputs into a format compatible with the model
"""
def reshape_inputs(lot_area, bedrooms_above_ground):
    array_of_inputs = np.array([float(lot_area), float(bedrooms_above_ground)]).reshape(1, -1)
    return array_of_inputs

"""
    Get prediction from model
"""
def get_predicted_house_price(model, reshaped_inputs):
    prediction = model.predict(reshaped_inputs)
    return prediction

if __name__ == "__main__":
    model = None 
    with open("ridge_model_v1.pkl", "rb") as f:
        model = pickle.load(f)

    try:
        print(get_predicted_house_price(model, reshape_inputs(10000, 2)))
    except Exception as e:
        print(e)