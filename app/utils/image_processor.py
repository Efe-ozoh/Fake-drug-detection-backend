from PIL import Image
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input


def prepare_image(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image_array = np.array(image, dtype=np.float32)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    image_array = preprocess_input(image_array)

    return image_array
