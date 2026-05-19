#export.py file to export the dataframe to a csv file
import pandas as pd
from database import SessionLocal
from models import Customer

def export_customers_to_csv(filename="customers.csv"):
    session = SessionLocal()

    # Query all rows from the Customers table
    records = session.query(Customer).all()

    # Convert SQLAlchemy objects to dictionaries
    data = [
        {
            "id": r.id,
            "name": r.name,
            "timestamp": r.timestamp,
            "day_of_call": r.day_of_call,
            "hour_of_day": r.hour_of_day,
            "wait_time": r.wait_time,
            "issue_category": r.issue_category,
            "resolution_status": r.resolution_status,
        }
        for r in records
    ]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv(filename, index=False)

    session.close()
    print(f"Export complete! CSV saved as {filename}")

if __name__ == "__main__":
    export_customers_to_csv()

#