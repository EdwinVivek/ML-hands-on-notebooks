import bentoml
import numpy as np
import argparse
import sys

@bentoml.service(resources={"cpu": "2"}, traffic={"timeout": 10})
class MyModel:
    bento_model = bentoml.models.get("bento_gs_model:latest")
    def __init__(self):
        self.model = self.bento_model.load_model()

    @bentoml.api
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        p = self.model.predict(input_data)
        return np.asarray(p)