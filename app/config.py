import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Config:
    GOOGLE_SECRET_KEY = os.getenv('GOOGLE_SECRET_KEY')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    