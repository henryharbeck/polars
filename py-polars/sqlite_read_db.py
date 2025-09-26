from importlib.util import find_spec

import adbc_driver_manager
from adbc_driver_sqlite.dbapi import connect

import polars as pl

pyarrow_installed = find_spec("pyarrow")
pyarrow_installed_msg = "with pyarrow" if pyarrow_installed else "without pyarrow"

print(
    f"Running for {adbc_driver_manager.__version__ = }, {pyarrow_installed_msg}",
    end="\n\n",
)

# Will test passing both a connection and a cursor
conn = connect()
cursor = conn.cursor()

plain_query = "SELECT value FROM JSON_EACH('[1, 2, 3, 4, 5]') WHERE value > 3"
for obj in (conn, cursor):
    try:
        df = pl.read_database(plain_query, obj)
        out = df.to_dict(as_series=False)
        print("Plain query result:", out, end="\n\n")
    except pl.exceptions.ModuleUpgradeRequiredError as e:  # noqa: PERF203
        print("Plain query result:", e, end="\n\n")


parameterized_query = "SELECT value FROM JSON_EACH('[1, 2, 3, 4, 5]') WHERE value > ?"
for obj in (conn, cursor):
    try:
        df = pl.read_database(
            parameterized_query,
            obj,
            execute_options={"parameters": (1,)},
        )
        out = df.to_dict(as_series=False)
        print("Parameterised query result:", out, end="\n\n")
    except pl.exceptions.ModuleUpgradeRequiredError as e:  # noqa: PERF203
        print("Parameterised query result:", e, end="\n\n")
