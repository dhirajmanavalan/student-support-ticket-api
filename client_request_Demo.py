import requests

BASE_URL = "http://127.0.0.1:8000"

login_payload = {
    "username": "dhirajkumar",
    "password": "Dhiraj@123"
}

login_resp = requests.post(f"{BASE_URL}/login", json=login_payload)
print("Login Status:", login_resp.status_code)
print("Login Response:", login_resp.json())

token = login_resp.json()["data"]["access_token"]

headers = {
    "Authorization": f"Bearer {token}"
}

ticket_payload = {
    "title": "Login issue",
    "description": "Unable to access student portal"
}

ticket_resp = requests.post(
    f"{BASE_URL}/tickets",
    json=ticket_payload,
    headers=headers
)

print("Ticket Status:", ticket_resp.status_code)
print("Ticket Response:", ticket_resp.json())
