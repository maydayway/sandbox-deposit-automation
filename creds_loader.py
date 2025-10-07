import os
from dotenv import load_dotenv

load_dotenv()

def get_bank_credentials():
    return {
        "account": os.getenv("BANK_ACCOUNT_NUMBER"),
        "routing": os.getenv("BANK_ROUTING_NUMBER")
    }
