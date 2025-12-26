from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:postgresql%40123%23@localhost/export_catalog"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))  # wrap SQL in text()
        print("Database connected successfully:", result.fetchone())
except Exception as e:
    print("Connection failed:", e)
