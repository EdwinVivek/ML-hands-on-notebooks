from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

class IrisExample:
    def __init__(self):
        self.name = "a"
        print("Iris class initialized")

    # Train and save the model
    def train_model(self):
        # Load dataset
        data = load_iris()
        X, y = data.data, data.target

        self.X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42
                                                           )
        # Define the model hyperparameters
        self.params = {
            "solver": "lbfgs",
            "max_iter": 1000,
            "multi_class": "auto",
            "random_state": 8888,
            }

        # Train model
        model = LogisticRegression(**params)
        model.fit(self.X_train, y_train)

        # Save the trained model
        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)
        print("Model trained and saved as model.pkl")
        return params
        
    # Load model 
    def load_model():
        # Load the saved model
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
    
    #make a prediction using predefined test data
    def predict():
        model = load_model()
        # Test data (sample input for prediction)
        test_data = [5.1, 3.5, 1.4, 0.2]  # Example features
        prediction = model.predict([test_data])
        #print(f"Prediction for {test_data}: {int(prediction[0])}")
        return prediction

    # Calculate metrics
    def metrics():
        y_pred = predict()
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
