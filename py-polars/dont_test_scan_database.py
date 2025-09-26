import polars as pl

df = (
    pl.scan_database_uri("test", "postgresql://postgres:postgres@localhost:5433")
    # .filter(
    # comment
    # pl.col("f0_") > 1500,
    # comment
    # pl.col("frollo_app_user") == "true",
    # )
    # .filter((pl.col("f0_") ^ pl.col("f0_")).is_not_null()) # Get this to work maybe?
    # .filter(~pl.col("f0_").is_in([1477, 16])) # Fix?
    .filter(pl.col("f0_").is_in([1477, 16]))
    .select("canstar_app_user", "web_user")
    .collect()
)
print(df)
