import numpy as np
import tensorflow as tf
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.consts import base_consts
from api.v1.serializers import ImageSerializer

MODEL = tf.keras.models.load_model("api/model/vgg16_clothing_classifier.h5")


class SearchByImageApiView(APIView):
    """
    API view for searching by images
    """

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data["image"]

        image = self._process_image(image)

        prediction = MODEL.predict(image)

        prediction_idx = np.argmax(prediction)
        prediction_class = base_consts.CLASS_LABELS[prediction_idx]

        response = {
            "prediction": prediction[0].tolist(),
        }
        return Response(response, status=status.HTTP_200_OK)

    def _process_image(self, image: InMemoryUploadedFile) -> np.array:
        img = Image.open(image).convert(settings.IMAGE_MODE)

        img = img.resize(settings.IMAGE_SIZE)

        img_array = np.array(img) / settings.MAX_PIXEL_VALUE

        img_array = np.expand_dims(img_array, axis=0)

        return img_array
