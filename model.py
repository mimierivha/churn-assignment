import pickle
#x
# Load the Model back from file
with open('customer_data_xgboost.pkl', 'rb') as file:
    customer_data_xgboost.pkl = pickle.load(file)