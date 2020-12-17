import os, io
from typing import Dict

from google.cloud import vision
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google_api_key.json"
client = vision.ImageAnnotatorClient()


class ImageReadingService:
    @classmethod
    def fetch_readings_from_image(cls, file_name: str = 4) -> Dict[str, str]:
        image_location = f"/Users/kalyan.teja-tatineni/Documents/code/fun/device-monitor/test/test{file_name}.HEIC"

        with io.open(image_location, "rb") as img:
            image_content = img.read()

        image = vision.Image(content=image_content)

        # annotate Image Response
        response = client.text_detection(image=image)

        df = pd.DataFrame(columns=["locale", "description"])

        texts = response.text_annotations
        readings = []
        for text in texts:
            readings.append(text.description)
            df = df.append(
                dict(locale=text.locale, description=text.description), ignore_index=True
            )

        print(df["description"][0])
        return {'readings': readings}
