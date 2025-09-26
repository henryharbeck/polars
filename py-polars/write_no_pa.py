import adbc_driver_sqlite

import polars as pl

a = adbc_driver_sqlite

df = pl.DataFrame({"a": 1})
o = df.write_database("test", "sqlite:///:memory:", engine="adbc")
print(o)
