import polars as pl

pl.read_database_uri("SELECT 1", "sqlite:///:memory:", engine="adbc")
