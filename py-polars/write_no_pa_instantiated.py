import adbc_driver_sqlite.dbapi

import polars as pl

df = pl.DataFrame({"a": 1})
with adbc_driver_sqlite.dbapi.connect() as conn:
    o = df.write_database("test", conn)
print(o)
