# Test para la API de FastAPI
import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "credit_score": 650,
    "gender": "Male",
    "age": 35,
    "tenure": 5,
    "balance": 50000.0,
    "products_number": 2,
    "credit_card": 1,
    "active_member": 1,
    "estimated_salary": 60000.0
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response:", response.json())
