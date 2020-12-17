import os, io
from google.cloud import vision
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google_api_key.json"

image_location = "/device-monitor/images/test.png"

with io.open(image_location, "rb") as img:
    image_content = img.read()

image = vision.Image(content=image_content)

client = vision.ImageAnnotatorClient()

# annotate Image Response
response = client.text_detection(image=image)
df = pd.DataFrame(columns=["locale", "description"])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(locale=text.locale, description=text.description), ignore_index=True
    )

print(df["description"][0])
# TODO: Update the JSON with readings here