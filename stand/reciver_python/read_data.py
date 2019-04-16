import socket
from clickhouse_driver.client import Client

sock = socket.socket()
PORT = 2003
sock.bind(("", PORT))
taglist = []

def parse_tag(tag_value):
    tag = tag_value.split('=')[0]
    value = float(tag_value.split('=')[1])
    if tag not in taglist:
        taglist.append(tag)
    return tag, value


if __name__ == "__main__":

    client = Client('clickhouse')
    print(client.execute('CREATE TABLE tmp(\n\
    path String,\n\
    last_volume UInt32\n\
    ) ENGINE = Log;'))
    #for i in range(100):
    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(100)

        udata = data.decode("utf-8")
        data = udata.split()
        print("Data: ",  udata, data)
        if len(data) == 3:
            timestamp = data[2]
            value = data[1]
            tmp = data[0].split(';')
            path = tmp[0]
            for tag_value in tmp[1:]:
                tag, value = parse_tag(tag_value)
            client.execute('INSERT INTO tmp [(path, last_volume)] VALUES (' + path +', '+ value +')')
            print(client.execute('SELECT * FROM tmp'))



