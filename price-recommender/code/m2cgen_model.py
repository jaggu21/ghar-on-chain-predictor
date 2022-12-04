import m2cgen
import pickle

"""
    Convert model to native code
"""
def model_to_native(model):
    native_python_decision_function = m2cgen.export_to_python(model)
    return native_python_decision_function

if __name__ == "__main__":
    model = None 
    with open("ridge_model_v1.pkl", "rb") as f:
        model = pickle.load(f) 
    try:
        print(model_to_native(model))
    except Exception as e:
        print(e)
