# seed.py
from faker import Faker
import random
import numpy as np
from datetime import datetime     #checkthis
from models import Customer
from database import SessionLocal

fake = Faker()

ISSUE_CATEGORIES = ["Billing", "Technical", "Service", "Account"]

def generate_call_record ():
    id = fake.uuid4()
    name = fake.name()
    timestamp = fake.date_time_this_year()  # Generates a random datetime within the current year
    day_of_call = timestamp.strftime("%A")  # Get the day of the week as a string
    hour_of_day = timestamp.hour  # Get the hour of the day (0-23)
    
# If the call is during business hours, wait time is likely longer
    if 9 <= hour_of_day < 17:  
        wait_time = random.randint(10, 45)
    else:
        wait_time = random.randint(2, 15)

# # Add extra wait time on Monday/Friday
    if day_of_call in ["Monday", "Friday"]:
        extra = int(np.random.randint(5, 16))    
        wait_time += extra

# Randomly assign issue category and resolution status
    issue_category = random.choice(ISSUE_CATEGORIES)
    resolution_status = random.choice([True, False])

# Create and return a Customer instance with the generated data
    return Customer(
        id=id,
        name=name,
        timestamp=timestamp,
        day_of_call=day_of_call,
        hour_of_day=hour_of_day,
        wait_time=wait_time,
        issue_categories=issue_category,
        resolution_status=resolution_status,
    )

def seed_customer (num_records=1000):
    session = SessionLocal()
    for _ in range(num_records):
        record = generate_call_record()
        session.add(record)
    session.commit()
    session.close()


if __name__ == "__main__":
    seed_customer(1000)
    print("Seeded Customer table with sample data.")