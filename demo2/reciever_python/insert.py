import socket
from clickhouse_driver.client import Client
from Parser import parse_tagged_data


if __name__ == "__main__":

    SOCK = socket.socket()
    PORT = 2003
    SOCK.bind(("", PORT))

    TAGLIST = []

    # connection to clickhouse
    CLIENT = Client("clickhouse")

    for i in range(100):

        SOCK.listen(1)
        conn, addr = SOCK.accept()
        data = conn.recv(512)

        insert_data, Tag_to_add, tags = parse_tagged_data(data)

        if Tag_to_add != [] and Tag_to_add:
            for tag in Tag_to_add:
                TAGLIST.append(tag)
                (
                    CLIENT.execute(
                        "ALTER TABLE events.tmp ADD \
                COLUMN IF NOT EXISTS "
                        + tag
                        + " UInt32 AFTER path"
                    )
                )

        if insert_data:
            (
                CLIENT.execute(
                    "INSERT INTO events.tmp (" + tags + ") VALUES", [insert_data]
                )
            )

    print(CLIENT.execute("SELECT * FROM events.tmp"))
