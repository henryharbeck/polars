from __future__ import annotations

import io
from typing import TYPE_CHECKING, Any

import pyarrow.ipc
import pytest

import polars as pl
from polars.interchange.protocol import CompatLevel
from polars.testing.asserts.frame import assert_frame_equal

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def foods_ipc_path(io_files_path: Path) -> Path:
    return io_files_path / "foods1.ipc"


def test_row_index(foods_ipc_path: Path) -> None:
    df = pl.read_ipc(foods_ipc_path, row_index_name="row_index", use_pyarrow=False)
    assert df["row_index"].to_list() == list(range(27))

    df = (
        pl.scan_ipc(foods_ipc_path, row_index_name="row_index")
        .filter(pl.col("category") == pl.lit("vegetables"))
        .collect()
    )

    assert df["row_index"].to_list() == [0, 6, 11, 13, 14, 20, 25]

    df = (
        pl.scan_ipc(foods_ipc_path, row_index_name="row_index")
        .with_row_index("foo", 10)
        .filter(pl.col("category") == pl.lit("vegetables"))
        .collect()
    )

    assert df["foo"].to_list() == [10, 16, 21, 23, 24, 30, 35]


def test_is_in_type_coercion(foods_ipc_path: Path) -> None:
    out = (
        pl.scan_ipc(foods_ipc_path)
        .filter(pl.col("category").is_in(("vegetables", "ice cream")))
        .collect()
    )
    assert out.shape == (7, 4)
    out = (
        pl.scan_ipc(foods_ipc_path)
        .select(pl.col("category").alias("cat"))
        .filter(pl.col("cat").is_in(["vegetables"]))
        .collect()
    )
    assert out.shape == (7, 1)


def test_row_index_schema(foods_ipc_path: Path) -> None:
    assert (
        pl.scan_ipc(foods_ipc_path, row_index_name="id")
        .select(["id", "category"])
        .collect()
    ).dtypes == [pl.UInt32, pl.String]


def test_glob_n_rows(io_files_path: Path) -> None:
    file_path = io_files_path / "foods*.ipc"
    df = pl.scan_ipc(file_path, n_rows=40).collect()

    # 27 rows from foods1.ipc and 13 from foods2.ipc
    assert df.shape == (40, 4)

    # take first and last rows
    assert df[[0, 39]].to_dict(as_series=False) == {
        "category": ["vegetables", "seafood"],
        "calories": [45, 146],
        "fats_g": [0.5, 6.0],
        "sugars_g": [2, 2],
    }


def test_ipc_list_arg(io_files_path: Path) -> None:
    first = io_files_path / "foods1.ipc"
    second = io_files_path / "foods2.ipc"

    df = pl.scan_ipc(source=[first, second]).collect()
    assert df.shape == (54, 4)
    assert df.row(-1) == ("seafood", 194, 12.0, 1)
    assert df.row(0) == ("vegetables", 45, 0.5, 2)


def test_scan_ipc_local_with_async(
    monkeypatch: Any,
    io_files_path: Path,
) -> None:
    monkeypatch.setenv("POLARS_VERBOSE", "1")
    monkeypatch.setenv("POLARS_FORCE_ASYNC", "1")

    assert_frame_equal(
        pl.scan_ipc(io_files_path / "foods1.ipc").head(1).collect(),
        pl.DataFrame(
            {
                "category": ["vegetables"],
                "calories": [45],
                "fats_g": [0.5],
                "sugars_g": [2],
            }
        ),
    )


def test_sink_ipc_compat_level_22930() -> None:
    df = pl.DataFrame({"a": ["foo"]})

    f1 = io.BytesIO()
    f2 = io.BytesIO()

    df.lazy().sink_ipc(f1, compat_level=CompatLevel.oldest(), engine="in-memory")
    df.lazy().sink_ipc(f2, compat_level=CompatLevel.oldest(), engine="streaming")

    f1.seek(0)
    f2.seek(0)

    t1 = pyarrow.ipc.open_file(f1)
    assert "large_string" in str(t1.schema)
    assert_frame_equal(pl.DataFrame(t1.read_all()), df)

    t2 = pyarrow.ipc.open_file(f2)
    assert "large_string" in str(t2.schema)
    assert_frame_equal(pl.DataFrame(t2.read_all()), df)


def test_scan_file_info_cache(
    capfd: Any, monkeypatch: Any, foods_ipc_path: Path
) -> None:
    monkeypatch.setenv("POLARS_VERBOSE", "1")
    a = pl.scan_ipc(foods_ipc_path)
    b = pl.scan_ipc(foods_ipc_path)

    a.join(b, how="cross").explain()

    captured = capfd.readouterr().err
    assert "FILE_INFO CACHE HIT" in captured
