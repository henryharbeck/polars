from importlib.util import find_spec

import adbc_driver_manager

import polars as pl

pyarrow_installed = find_spec("pyarrow")
pyarrow_installed_msg = "with pyarrow" if pyarrow_installed else "without pyarrow"

print(
    f"Running for {adbc_driver_manager.__version__ = }, {pyarrow_installed_msg}",
    end="\n\n",
)

uri = "postgresql://postgres:postgres@localhost:5433"

plain_query = "SELECT * FROM GENERATE_SERIES(1, 5) AS s WHERE s > 3"
try:
    df = pl.read_database_uri(
        plain_query,
        uri,
        engine="adbc",
    )
    out = df.to_dict(as_series=False)
    expected_result = {"s": [4, 5]}
    assert out == expected_result
    print("plain query result:", out, end="\n\n")
except pl.exceptions.ModuleUpgradeRequiredError as e:
    print("plain query result:", e, sep="\n", end="\n\n")

parameterized_query = "SELECT * FROM GENERATE_SERIES(1, 5) AS s WHERE s > $1"
try:
    df = pl.read_database_uri(
        parameterized_query,
        uri,
        engine="adbc",
        execute_options={"parameters": (1,)},
    )
    out = df.to_dict(as_series=False)
    expected_result = {"s": [2, 3, 4, 5]}
    assert out == expected_result
    print("parameterized query result:", out, end="\n\n")
except pl.exceptions.ModuleUpgradeRequiredError as e:
    print("parameterized query result:", e, sep="\n", end="\n\n")
