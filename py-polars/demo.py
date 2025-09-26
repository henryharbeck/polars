import polars as pl

df = pl.DataFrame({"a": 1})
try:
    rows_written = df.write_database("test", "sqlite:///:memory:", engine="adbc")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
else:
    print(f"{rows_written = }")
