## databases
to reduce overhead we should limit ourselves to one instance of each db type required. 

### mariadb
This means however that we need to find a way to restart the mysql container, adding a new db in the process.

Ideally, we create a mariadb network on which every container with need for db access is connected. We then need, similar to dockergen container for nginx, a service that checks if new containers are connected to the network and creates / imports DBs based on env vars in docker-compose file.

#### Better security
the mariadb network would simultaneously ensure that the database cannot be connected to from the internet. It currently is on the nginx network, not sure what that entails. Adminer would run on db network as well as nginx network. 

env var
```python
MYSQL_DATABASES=[nextcloud, october]
MYSQL_USERS=[nextcloud, october]
MYSQL_PASSWORDS=[passwordfornextcloud, passwordforoctober]
#sql dump file
for db in MYSQL_DATABASES:
  print(f'mysql CREATE DATABASE {db} IF DOES NOT EXIST;)
```
#### Configuration via environment variables
every container that needs a db gets these env vars. These are then used by the dockergen for dbs to automatically create / allow access to the specified database.
```yaml
environment:
  - MYSQL_HOST=db
  - MYSQL_USER=nextcloud
  - MYSQL_PASSWORD=sV7CbxGCtNkZWhC9PLlExJ04
  - MYSQL_DATABASE=nextcloud_db 
```

### option 0
either configure on mariadb container directly, this would mean creating a loop around this part of the `docker_setup_db()` function
```bash
	# Creates a custom database and user if specified
	if [ -n "$MYSQL_DATABASE" ]; then
		mysql_note "Creating database ${MYSQL_DATABASE}"
		docker_process_sql --database=mysql <<<"CREATE DATABASE IF NOT EXISTS \`$MYSQL_DATABASE\` ;"
	fi

	if [ -n "$MYSQL_USER" ] && [ -n "$MYSQL_PASSWORD" ]; then
		mysql_note "Creating user ${MYSQL_USER}"
		docker_process_sql --database=mysql <<<"CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD' ;"

		if [ -n "$MYSQL_DATABASE" ]; then
			mysql_note "Giving user ${MYSQL_USER} access to schema ${MYSQL_DATABASE}"
			docker_process_sql --database=mysql <<<"GRANT ALL ON \`$MYSQL_DATABASE\`.* TO '$MYSQL_USER'@'%' ;"
		fi

		docker_process_sql --database=mysql <<<"FLUSH PRIVILEGES ;"
	fi
}
```

or we execute an add database command on the container for every newly added container to the db network


#### option 1
gracefully stop the container, edit/add a `.sh`, `.sql` or `.sql.gz` file to `/docker-entrypoint-initdb.d` to add the new databases, restart the container


#### option 2
add the new db to the running mysql instance, save sql dump file and use that as the new "init" file for mariadb container. Removing volumes should not lead to data lass

