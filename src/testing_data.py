import enum
import random
from google.genai import Client
from pydantic import BaseModel

from configs import API_KEY, MODEL


class MaritalStatus(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class Grade(enum.Enum):
    A = str(random.randint(85, 100)) + "-A"
    B = str(random.randint(70, 85)) + "-B"
    C = str(random.randint(55, 70)) + "-C"
    D = str(random.randint(0, 55)) + "-D"


class User(BaseModel):
    fullname: str
    mobile: str
    address: str
    status: MaritalStatus
    grade: Grade


client = Client(api_key=API_KEY)


def generate_test_users(number: int):
    response = client.models.generate_content(
        model=MODEL,
        contents=f"Generate {number} testing users",
        config={
            "response_mime_type": "application/json",
            "response_schema": list[User]
        })
    print(response.text)


if __name__ == "__main__":
    generate_test_users(number=5)
