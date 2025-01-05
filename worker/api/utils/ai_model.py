import base64
from io import BytesIO

import numpy as np
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
from keras.api.applications.vgg16 import preprocess_input
from keras.api.models import load_model
from keras.src.models import Model
from PIL import Image

MODEL = load_model(settings.MODEL_PATH)
feature_extractor = Model(inputs=MODEL.inputs, outputs=MODEL.layers[-2].output)


def extract_features(image_data):
    image = None
    if isinstance(image_data, str):
        image_data = base64.b64decode(image_data.split(",")[1])
        image = Image.open(BytesIO(image_data))
    elif isinstance(image_data, UploadedFile):
        image = Image.open(image_data)

    if image:
        image = image.convert(settings.IMAGE_MODE)

        width, height = image.size
        max_dim = max(width, height)

        white_image = Image.new(
            settings.IMAGE_MODE, (max_dim, max_dim), (255, 255, 255)
        )
        white_image.paste(image, ((max_dim - width) // 2, (max_dim - height) // 2))

        image_resized = white_image.resize(settings.IMAGE_SIZE)
        image_array = np.array(image_resized)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        features = feature_extractor.predict(image_array)
        return features.flatten()
