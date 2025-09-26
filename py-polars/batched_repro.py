import sqlite3

import polars as pl

conn = sqlite3.connect(":memory:", detect_types=True)
# df = pl.read_database("SELECT 1", conn)
batches = pl.read_database(
    "SELECT 1 as val",
    conn,
    iter_batches=True,
    batch_size=1,
    schema_overrides={"val": pl.UInt8},
)
df: pl.DataFrame = pl.concat(batches)
print(df)
