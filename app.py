from database import engine
from models import DBModelBase
from seed import seed_customer

DBModelBase.metadata.create_all(engine)

seed_customer(1000)

print("Database initialized and Customers table seeded.")
