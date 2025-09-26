from adbc_driver_sqlite.dbapi import connect

import polars as pl

conn = connect()

df = pl.DataFrame({"a": 1})
try:
    rows_written = df.write_database("test", conn, engine="adbc")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
else:
    print(f"{rows_written = }")
