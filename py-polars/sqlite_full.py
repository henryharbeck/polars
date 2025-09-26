from importlib.util import find_spec

import adbc_driver_manager

import polars as pl

pyarrow_installed = find_spec("pyarrow")
pyarrow_installed_msg = "with pyarrow" if pyarrow_installed else "without pyarrow"

print(
    f"Running for {adbc_driver_manager.__version__ = }, {pyarrow_installed_msg}",
    end="\n\n",
)

uri = "sqlite:///:memory:"

plain_query = "SELECT value FROM JSON_EACH('[1, 2, 3, 4, 5]') WHERE value > 3"
expected_result = {"value": [4, 5]}
try:
    df = pl.read_database_uri(
        plain_query,
        uri,
        engine="adbc",
    )
    out = df.to_dict(as_series=False)
    assert out == expected_result
    print("Plain query result:", out, end="\n\n")
except pl.exceptions.ModuleUpgradeRequiredError as e:
    print("Plain query result:", e, end="\n\n")


parameterized_query = "SELECT value FROM JSON_EACH('[1, 2, 3, 4, 5]') WHERE value > ?"
params = (1,)
expected_result = {"value": [2, 3, 4, 5]}
try:
    df = pl.read_database_uri(
        parameterized_query,
        uri,
        engine="adbc",
        execute_options={"parameters": params},
    )
    out = df.to_dict(as_series=False)
    assert out == expected_result
    print("Parameterized query result:", out, end="\n\n")
except pl.exceptions.ModuleUpgradeRequiredError as e:
    print("Parameterized query result:", e, end="\n\n")
