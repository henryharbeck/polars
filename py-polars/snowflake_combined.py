from adbc_driver_snowflake.dbapi import connect

import polars as pl

sf_uri = "xxx"
conn = connect(sf_uri)

df = pl.DataFrame({"a": ["abcd"]})
rows_written = df.write_database(
    "test",
    conn,
    if_table_exists="replace",
)
print(f"{rows_written = }")

df.write_database(
    "test",
    f"snowflake://{sf_uri}",
    if_table_exists="replace",
    engine="adbc",
)
print(f"{rows_written = }")
