from adbc_driver_sqlite.dbapi import connect

import polars as pl

with connect() as conn, conn.cursor() as cursor:
    cursor.execute("SELECT value FROM JSON_EACH('[1, 2, 3, 4, 5]')")
    reader = cursor.fetch_record_batch()
    for batch in reader:
        print(type(batch))
        df = pl.from_arrow(batch)
        print(df)
