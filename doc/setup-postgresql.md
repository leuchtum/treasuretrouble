# Setup the PostgreSQL

## For MacOS

https://wiki.postgresql.org/wiki/Homebrew

```shell
$ brew services start postgresql # or "brew services run postgresql" to have it not restart at boot time or the pg_ctl command it mentions
```

Check if postgresql is up and running

```shell
$ pg_isready
/tmp:5432 - accepting connections
```

## Tutorials

https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/
