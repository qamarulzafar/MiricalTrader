import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.database import SessionLocal, get_db, Base, engine
import backend.models as models


@pytest.fixture(scope='module')
def client():
    # ensure tables exist for test module
    Base.metadata.create_all(bind=engine)

    # seed minimal data if missing
    db = SessionLocal()
    if db.query(models.Category).count() == 0:
        c1 = models.Category(name='TestCat', slug='testcat')
        db.add(c1)
        db.commit()
        db.refresh(c1)
        p1 = models.Product(name='TestProd', slug='testprod', category_id=c1.id, in_stock=True, price_on_request=False)
        db.add(p1)
        db.commit()
    db.close()

    # override dependency to use normal SessionLocal
    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def test_get_categories(client):
    res = client.get('/categories')
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert any('testcat' in (item.get('slug') or '') for item in data)


def test_get_products(client):
    res = client.get('/products')
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert any('testprod' in (item.get('slug') or '') for item in data)
