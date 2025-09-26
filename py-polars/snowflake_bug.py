from adbc_driver_snowflake.dbapi import connect

import polars as pl

uri = "xxx"
conn = connect(uri)

df = pl.DataFrame({"a": ["abcd"]})
rows_written = df.write_database("test", conn, if_table_exists="replace")
print(f"{rows_written = }")
