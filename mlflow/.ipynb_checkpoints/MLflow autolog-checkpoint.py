import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

if __name__ == "__main__":
    mlflow.set_tracking_uri(uri="http://localhost:8080")
    mlflow.set_experiment(experiment_name="auto_logging")
    mlflow.sklearn.autolog()
    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    # MLflow triggers logging automatically upon model fitting
    with mlflow.start_run(run_name="autolog-ex") as run:
        print("in run")
        rf.fit(X_train, y_train)

    # Disabling autologging
    mlflow.sklearn.autolog(disable=True)


#autolog_run = mlflow.last_active_run()
#print(autolog_run)