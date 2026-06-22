from PIL import Image
import numpy as np


def prepare_image(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image_array = np.array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array