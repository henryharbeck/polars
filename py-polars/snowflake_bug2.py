import polars as pl

uri = "xxxx"

df = pl.DataFrame({"a": ["abcd"]})
rows_written = df.write_database(
    "test2",
    f"snowflake://{uri}",
    if_table_exists="replace",
    engine="adbc",
)
print(rows_written)
