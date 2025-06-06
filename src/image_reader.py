import enum
import os
from google.genai import Client
from pydantic import BaseModel

from configs import API_KEY, MODEL


class Chart(enum.Enum):
    YES = "Yes"
    NO = "No"


class Image(BaseModel):
    isChartAvailable: Chart
    solarConsumption: float
    gridConsumption: float
    deviceName: str


client = Client(api_key=API_KEY)

def get_img_content():
    _, _, files = next(os.walk("../images"))
    file_len = len(files) + 1
    for el in range(1, file_len):
        my_file = client.files.upload(file=f"../images/image_{el}.png")
        response = client.models.generate_content(
            model=MODEL,
            contents=[my_file],
            config={
                "response_mime_type": "application/json",
                "response_schema": Image
            })
        print(response.text)


if __name__ == "__main__":
    get_img_content()
