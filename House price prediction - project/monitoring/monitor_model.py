import pandas as pd
import os
import sqlalchemy as db
from House_Price_Prediction import *

class MonitorModel():
    def __init__(self):
        self.house = HousePricePrediction()

    def get_reference_data(self):
        reference = self.house.execute_features_store()

    
    def push_feedback_to_db(self):
        engine = db.create_engine()
        df = pd.read_csv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "serving/feedback.csv"))
        df_X = df.drop([["house_id", "prediction"]])
        df_y = df[["event_timestamp","prediction"]]
        df_X.to_sql("house_features_sql", con=engine, if_exists="append")
        df_y.to_sql("house_target_sql", con=engine, if_exists="append")
        start_date = reference.max_date
        end_date = df.loc[df["event_timestamp"].idxmax()]["event_timestamp"]
        self.house.materialize(start = start_date, end_date = end_date)
        print("Feedback data pushed to online feature store successfully!")
        self.get_current_data(engine, start_date, end_date)

    
    def get_current_data(self,engine, start_date, end_date):
       entity_df_ref = pd.read_sql(str.format("select house_id from pulic.house_features_sql where event_timestamp <= {0}", start_date)).to_dict(orient="records")
       reference =  house.getonlinefeatures(entity_df_ref, features)

       entity_df_cur = pd.read_sql(str.format("select house_id from pulic.house_features_sql where event_timestamp > {0}", start_date)).to_dict(orient="records")
       current = house.getonlinefeatures(entity_df_cur, features)

    def monitor_drift(self):
        pass