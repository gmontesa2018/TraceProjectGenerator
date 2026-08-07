from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("CLICKUP_TOKEN")

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}



