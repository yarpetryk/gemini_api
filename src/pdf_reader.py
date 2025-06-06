import os
from google.genai import Client
from pydantic import BaseModel

from configs import API_KEY, MODEL


class PdfDocument(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth: str
    country: str
    email: str
    position: str
    gender: str
    zip: str
    language: str
    vehicle: str


client = Client(api_key=API_KEY)


def get_pdf_content():
    _, _, files = next(os.walk("../pdf_documents"))
    file_len = len(files) + 1
    for el in range(1, file_len):
        pdf_file = client.files.upload(
            file=f"../pdf_documents/file_{el}.pdf")

        response = client.models.generate_content(
            model=MODEL,
            contents=pdf_file,
            config={
                "response_mime_type": "application/json",
                "response_schema": PdfDocument})
        print(response.text)


if __name__ == "__main__":
    get_pdf_content()
