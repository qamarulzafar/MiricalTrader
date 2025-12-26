import os, traceback
os.environ['DATABASE_URL']='sqlite:///./dev.db'
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

try:
    r = client.get('/categories')
    print('GET /categories ->', r.status_code)
    print(r.text)
except Exception:
    traceback.print_exc()

try:
    r = client.get('/products')
    print('GET /products ->', r.status_code)
    print(r.text)
except Exception:
    traceback.print_exc()
