from database import engine
from sqlalchemy import text

with engine.begin() as conn:
    conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS category_id INTEGER REFERENCES categories(id)"))
    print('OK: added column if missing')
