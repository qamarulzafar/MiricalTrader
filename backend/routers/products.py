from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
import models

router = APIRouter(prefix="/products", tags=["products"]) 

@router.get("/", summary="List products")
def list_products(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(models.Product)
    if category_id is not None:
        query = query.filter(models.Product.category_id == category_id)
    return query.all()

@router.get("/{product_id}", summary="Get product by id")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Product).get(product_id)
