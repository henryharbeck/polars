from adbc_driver_postgresql.dbapi import connect

import polars as pl

uri = "postgresql://postgres:postgres@localhost:5433"
conn = connect(uri)

df = pl.DataFrame({"a": ["abbc"]})
o = df.write_database("test", conn, if_table_exists="replace")
print(o)
