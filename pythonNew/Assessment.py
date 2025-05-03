from sqlmodel import Field, Session, SQLModel, create_engine, select, func
from datetime import datetime, timedelta


# Define the sales model/table
class Sale(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sale_date: datetime
    vehicles_sold: int
    customer_type: str  # 'retail' or 'corporate'


# Create SQLite DB and engine
engine = create_engine("sqlite:///superwheels_sales.db")
SQLModel.metadata.create_all(engine)


# Populate sales data from April 1 to September 30
start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 9, 30)
date = start_date
day_count = 0
current_sales = 1

with Session(engine) as session:
    while date <= end_date:
        customer_type = "corporate" if (day_count % 5 == 4) else "retail"

        sale = Sale(
            sale_date=date,
            vehicles_sold=current_sales,
            customer_type=customer_type
        )

        session.add(sale)

        # Move to next day
        date += timedelta(days=1)
        day_count += 1
        current_sales += 2

    session.commit()


# ---- Queries ----

with Session(engine) as session:
    # a. Number of vehicles sold each month
    print("\na. Vehicles sold each month:")
    month_sales = session.exec(
        select(
            func.strftime("%Y-%m", Sale.sale_date),
            func.sum(Sale.vehicles_sold)
        ).group_by(func.strftime("%Y-%m", Sale.sale_date))
    ).all()

    for month, total in month_sales:
        print(f"{month}: {total} vehicles")

    # b. Vehicles sold to retail customers
    retail_total = session.exec(
        select(func.sum(Sale.vehicles_sold)).where(Sale.customer_type == "retail")
    ).one()

    print(f"\nb. Vehicles sold to retail customers: {retail_total}")

    # c. Vehicles sold to corporate customers
    corporate_total = session.exec(
        select(func.sum(Sale.vehicles_sold)).where(Sale.customer_type == "corporate")
    ).one()

    print(f"c. Vehicles sold to corporate customers: {corporate_total}")

    # d. Vehicles sold between Aug 15 and Sep 15
    aug15 = datetime(2024, 8, 15)
    sep15 = datetime(2024, 9, 15)

    aug_sep_total = session.exec(
        select(func.sum(Sale.vehicles_sold)).where(Sale.sale_date.between(aug15, sep15))
    ).one()

    print(f"d. Vehicles sold from Aug 15 to Sep 15: {aug_sep_total}")