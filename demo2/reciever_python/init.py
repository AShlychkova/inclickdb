from clickhouse_driver.client import Client


def init(table_name="events"):
    """
    :param table_name:name of table for mecrics
    :return: ok

    to_do: add checks
    """

    # connection to clickhous
    client = Client("clickhouse")

    # creating database and table
    print(client.execute("CREATE DATABASE IF NOT EXISTS " + table_name))
    print(
        client.execute(
            "CREATE TABLE IF NOT EXISTS events.tmp(\n \
            timestmp UInt32, \n \
            last_volume UInt32, \n \
            path String \n \
        ) ENGINE MergeTree() PARTITION BY\
         timestmp ORDER BY timestmp SETTINGS index_granularity=8192;"
        )
    )
    return "created: events.tmp"


if __name__ == "__main__":
    print(init())
