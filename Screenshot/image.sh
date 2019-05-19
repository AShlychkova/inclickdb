#!/bin/sh

key=$(cat grafana-key/key.txt)
curl 'http://localhost:3000/render/\
d-solo/JE7rYbjmz/dh?orgId=\
1&panelId=\
2&width=\
1000&height=500' -H 'Authorization: Bearer '$key --compressed > ./snapshots/output.png
