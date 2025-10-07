from creds_loader import get_bank_credentials
import requests

creds = get_bank_credentials()
amount = 1955.38
note = "Deposit check #182928 for Gerald Thomas"

payload = {
    "account": creds["account"],
    "amount": amount,
    "note": note
}

url = f"https://your-api-url/accounts/{creds['account']}/deposit-check"
response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.json())
