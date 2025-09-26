import duckdb

import polars as pl

conn = duckdb.connect()
print(pl.read_database("SELECT 1", conn))
