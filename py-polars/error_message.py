import polars as pl

df = pl.DataFrame({"a": 1})
connection_uri = "sqlite:///:memory:"

try:
    df.write_database("test", connection_uri, engine="adbc")
except Exception as e:
    print(f"{type(e).__name__}: {e}")

connection_uri = "mysql:///:memory:"

try:
    df.write_database("test", connection_uri, engine="adbc")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
