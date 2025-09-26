import adbc_driver_manager
import adbc_driver_postgresql
from adbc_driver_postgresql.dbapi import connect

import polars as pl

print(f"{adbc_driver_manager.__version__ = }")
print(f"{adbc_driver_postgresql.__version__ = }")
print(f"{pl.__version__ = }")

df = pl.DataFrame({"a": 1})
uri = "postgresql://postgres:postgres@localhost:5433"

with connect(uri) as conn, conn.cursor() as cur:
    cur.execute("DROP TABLE IF EXISTS my_schema.new_table")
    cur.execute("DROP TABLE IF EXISTS public.new_table")
    conn.commit()

expected_schema = "my_schema"
df.write_database(f"{expected_schema}.new_table", uri, engine="adbc")

query = """
    SELECT table_schema
    FROM information_schema.tables
    WHERE table_name = 'new_table'
"""
actual_schema = pl.read_database_uri(query, uri, engine="adbc").item()
# Table is in "public" schema, not "my_schema" schema
print(f"{expected_schema = }, {actual_schema = }")
