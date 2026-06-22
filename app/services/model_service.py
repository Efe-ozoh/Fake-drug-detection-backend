from tensorflow.keras.models import load_model
import json


class ModelService:

    def __init__(self):

        self.model = load_model(
            "models/counterfeit_drug_detector.keras"
        )

        with open(
            "models/class_names.json",
            "r"
        ) as f:

            self.class_names = json.load(f)


model_service = ModelService()