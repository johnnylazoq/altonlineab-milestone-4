import mimerpy
import os
from dotenv import load_dotenv

load_dotenv()

def connect(user=None, password=None, database=None):
    """
    Establishes a connection to the MimerSQL database.
    """
    return mimerpy.connect(
        user=user or os.getenv("DB_USER"),
        password=password or os.getenv("DB_PASSWORD"),
        database=database or os.getenv("DB_NAME")
    )
