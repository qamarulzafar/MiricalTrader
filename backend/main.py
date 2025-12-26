from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
# import models first so SQLAlchemy knows about mapped tables
import models

# create tables for development convenience (Alembic will be used later)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Export Catalog API")

# Enable CORS for development (adjust origins for production)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3001", "http://127.0.0.1:3001"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Include routers
from routers.categories import router as categories_router
from routers.products import router as products_router

app.include_router(categories_router)
app.include_router(products_router)
