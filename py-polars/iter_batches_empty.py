import sqlite3

import polars as pl

conn = sqlite3.connect(":memory:", detect_types=True)

q1 = "SELECT 1 AS a, 2 AS b"
q2 = "SELECT 1 AS a, 2 AS b WHERE FALSE"
# print(pl.read_database(q1, conn))
# shape: (1, 2)
# ┌─────┬─────┐
# │ a   ┆ b   │
# │ --- ┆ --- │
# │ i64 ┆ i64 │
# ╞═════╪═════╡
# │ 1   ┆ 2   │
# └─────┴─────┘

# print(pl.read_database(q2, conn))
# shape: (0, 2)
# ┌──────┬──────┐
# │ a    ┆ b    │
# │ ---  ┆ ---  │
# │ null ┆ null │
# ╞══════╪══════╡
# └──────┴──────┘

# q1_batches = list(pl.read_database(q1, conn, iter_batches=True, batch_size=1))
# print(q1_batches)
# [shape: (1, 2)
# ┌─────┬─────┐
# │ a   ┆ b   │
# │ --- ┆ --- │
# │ i64 ┆ i64 │
# ╞═════╪═════╡
# │ 1   ┆ 2   │
# └─────┴─────┘]
# q1_combined = pl.concat(q1_batches)


q2_batches = list(pl.read_database(q2, conn, iter_batches=True, batch_size=1))
print(q2_batches)
# []

q2_combined = pl.concat(q2_batches)
# ValueError: cannot concat empty list
