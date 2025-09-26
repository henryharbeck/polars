import adbc_driver_bigquery
import adbc_driver_bigquery.dbapi
import adbc_driver_manager
import adbc_driver_manager.dbapi
import adbc_driver_postgresql.dbapi
import adbc_driver_snowflake.dbapi
import adbc_driver_sqlite.dbapi

sf_uri = "xxxx"
pg_uri = "postgresql://postgres:postgres@localhost:5433"

sf_conn = adbc_driver_snowflake.dbapi.connect(sf_uri)
# sf_cur = sf_conn.cursor()

sqlite_conn = adbc_driver_sqlite.dbapi.connect()
# sqlite_cur = sqlite_conn.cursor()

pg_conn = adbc_driver_postgresql.dbapi.connect(pg_uri)
# pg_cur = pg_conn.cursor()

bq_conn = adbc_driver_bigquery.dbapi.connect(
    {adbc_driver_bigquery.DatabaseOptions.PROJECT_ID.value: "cns-playpen-hh"}
)
# bq_cur = bq_conn.cursor()


def try_execute_query(conn: adbc_driver_manager.dbapi.Connection, query: str) -> bool:
    """Boo."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
    except adbc_driver_manager.Error:
        return False
    else:
        return True


def get_adbc_driver_name_from_conn(conn: adbc_driver_manager.dbapi.Connection) -> str:
    """Boo."""
    if try_execute_query(conn, "SELECT sqlite_version()"):
        return "adbc_driver_sqlite"
    if try_execute_query(conn, "SELECT pg_backend_pid()"):
        return "adbc_driver_postgresql"
    if try_execute_query(conn, "SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO()"):
        return "adbc_driver_snowflake"
    if try_execute_query(conn, "SELECT 1 FROM duckdb_databases();"):
        return "adbc_driver_duckdb"
    if try_execute_query(conn, "SELECT @@project_id"):
        return "adbc_driver_bigquery"
    return "adbc_driver_flightsql"


# g = get_adbc_driver_name_from_conn
# print(g(sf_conn))
# print(g(sqlite_conn))
# print(g(pg_conn))
# print(g(bq_conn))


def is_snowflake_driver(conn: adbc_driver_manager.dbapi.Connection) -> bool:
    """Boo."""
    try:
        import adbc_driver_snowflake

        return (
            "snowflake"
            in conn.adbc_database.get_option(
                adbc_driver_snowflake.DatabaseOptions.HOST.value
            ).lower()
        )
    except (ImportError, adbc_driver_manager.Error):
        return False


print(is_snowflake_driver(sf_conn))
print(is_snowflake_driver(sqlite_conn))
print(is_snowflake_driver(pg_conn))
print(is_snowflake_driver(bq_conn))
