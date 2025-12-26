from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/categories", tags=["categories"]) 

@router.get("/", summary="List categories")
def list_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

@router.get("/{category_id}", summary="Get category by id")
def get_category(category_id: int, db: Session = Depends(get_db)):
    cat = db.query(models.Category).get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat
