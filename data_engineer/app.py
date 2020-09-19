import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://data_engineer:data_engineer@localhost:5432/data_engineer"
)

if __name__ == "__main__":

    # insert records
    df = pd.DataFrame(
        {
            "first_name": ["Jose", "Maria", "Antonio", "Pedro", "Carlos"],
            "last_name": ["Silva", "Alves", "Cardoso", "Silva", "Rodrigues"],
            "email": [
                "jose@email.com",
                "maria@email.com",
                "antonio@email.com",
                "pedro@email.com",
                "carlos@email.com",
            ],
        }
    )
    df.to_sql("customers", con=engine, index=False, if_exists="replace")

    # show records
    conn = engine.connect()
    dataFrame = pd.read_sql('select * from "customers"', conn)
    conn.close()

    print(dataFrame)
