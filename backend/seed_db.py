from database import SessionLocal, engine, Base
import models

# ensure tables exist
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# simple idempotent seeding
if session.query(models.Category).count() == 0:
    cat1 = models.Category(name='Electronics', slug='electronics')
    cat2 = models.Category(name='Books', slug='books')
    session.add_all([cat1, cat2])
    session.commit()
    print('Inserted categories')
else:
    print('Categories already present')

if session.query(models.Product).count() == 0:
    # get first category id
    electronics = session.query(models.Category).filter_by(slug='electronics').first()
    books = session.query(models.Category).filter_by(slug='books').first()
    p1 = models.Product(name='Phone', slug='phone', category_id=electronics.id, in_stock=True, price_on_request=False)
    p2 = models.Product(name='Novel', slug='novel', category_id=books.id, in_stock=True, price_on_request=False)
    session.add_all([p1, p2])
    session.commit()
    print('Inserted products')
else:
    print('Products already present')

session.close()
