### Graphite -> Clickhouse demo

#### What is it?

This demo does the following:
- Generates some graphite data
- Sends it to [graphite-clickhouse](https://github.com/lomik/graphite-clickhouse)
- Via graphite-clickhouse stores it to Clickhouse database
- Takes snapshot of the database via grafana-api

Thanks to [preconfigured docker-compose](https://github.com/lomik/graphite-clickhouse-tldr), that was used as a start point.

#### What should I do?

Do the following steps:
- `docker-compose up`
- `bash generator.sh` (for generating data)
- `bash image.sh` (for taking snapshot)

You can look at the result in the `snapshots` folder.

Also, you can access Grafana via opening [localhost:3000](http://localhost:3000) in your browser. Login/password: admin/admin.
