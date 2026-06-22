from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from PIL import Image
import numpy as np

from app.services.model_service import (
    model_service
)

from app.utils.image_processor import (
    prepare_image
)

router = APIRouter()


@router.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    image = Image.open(
        file.file
    )

    image_array = prepare_image(
        image
    )

    predictions = (
        model_service.model.predict(
            image_array,
            verbose=0
        )[0]
    )

    predicted_index = np.argmax(
        predictions
    )

    return {
        "prediction":
        model_service.class_names[
            predicted_index
        ],

        "confidence":
        float(
            predictions[
                predicted_index
            ]
        ),

        "probabilities": {

            model_service.class_names[i]:
            float(predictions[i])

            for i in range(
                len(predictions)
            )
        }
    }