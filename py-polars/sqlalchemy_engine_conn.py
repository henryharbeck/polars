from sqlalchemy import create_engine

import polars as pl

uri = "sqlite:///:memory:"
engine = create_engine(uri)
conn = engine.connect()

query = "SELECT 1"


df = pl.DataFrame({"a": 1})

pl.read_database(query, engine)
pl.read_database(query, conn)

df.write_database("test1", uri)
df.write_database("test2", conn)
df.write_database("test3", engine)
