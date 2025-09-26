from sqlalchemy import create_engine, select, text

import polars as pl

engine = create_engine("duckdb:///:memory:")

with engine.connect() as conn:
    stmt = select(1)
    df = pl.read_database(stmt, connection=conn)
    print(df)

    stmt = text("SELECT 1")
    df = pl.read_database(stmt, connection=conn)
    print(df)
