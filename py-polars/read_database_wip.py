from adbc_driver_sqlite.dbapi import connect

import polars as pl

with connect() as conn, conn.cursor() as cursor:
    cursor.execute("SELECT 1")
    arrow = cursor.fetch_arrow()
    df = pl.from_arrow(arrow)
    print(df)
