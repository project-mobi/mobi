# project mobi
## mattermost docker compose file
```yaml
version: '3.7'  


services:
    # Detailed below



networks:
  mattermost_network:
  # network with nginx webserver container
  internet_network:
```

### mattermost
#### Mattermost db
```yaml
  mattermost-db:
    build: db
    read_only: true
    restart: unless-stopped
    networks:
      - mattermost_network
    volumes:
      - ./volumes/db/var/lib/postgresql/data:/var/lib/postgresql/data
      - /etc/localtime:/etc/localtime:ro
    environment:
      - POSTGRES_USER=mattermost
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=mattermost
    # uncomment the following to enable backup
    #  - AWS_ACCESS_KEY_ID=XXXX
    #  - AWS_SECRET_ACCESS_KEY=XXXX
    #  - WALE_S3_PREFIX=s3://BUCKET_NAME/PATH
    #  - AWS_REGION=us-east-1
```
#### mattermost app
```yaml
services:

  # [...]
  
  mattermost-app:
    build: app
      # change `build:app` to `build:` and uncomment following lines for team edition or change UID/GID
      # context: app
      # args:
      #   - edition=team
      #   - PUID=1000
      #   - PGID=1000
    restart: unless-stopped
    networks:
      - internet_network
      - mattermost_network
    volumes:
      - ./volumes/app/mattermost/config:/mattermost/config:rw
      - ./volumes/app/mattermost/data:/mattermost/data:rw
      - ./volumes/app/mattermost/logs:/mattermost/logs:rw
      - ./volumes/app/mattermost/plugins:/mattermost/plugins:rw
      - ./volumes/app/mattermost/client-plugins:/mattermost/client/plugins:rw
      - /etc/localtime:/etc/localtime:ro
    environment:
      # set same as db credentials and dbname
      - MM_USERNAME=mattermost
      - MM_PASSWORD=secret
      - MM_DBNAME=mattermost


      # use the credentials you've set above, in the format:
      # MM_SQLSETTINGS_DATASOURCE=postgres://${MM_USERNAME}:${MM_PASSWORD}@db:5432/${MM_DBNAME}?sslmode=disable&connect_timeout=10
      - MM_SQLSETTINGS_DATASOURCE=postgres://mattermost:secret@db:5432/mattermost?sslmode=disable&connect_timeout=10

      # in case your config is not in default location
      #- MM_CONFIG=/mattermost/config/config.json


```
##### additional environment variables
```yaml
    environment:
      # for different port / address
      - APP_HOST=localhost
      - APP_PORT_NUMBER=8081

      # for different db host / port
      - DB_HOST=localhost
      - DB_PORT_NUMBER=3306

      # for mysql db
      - MM_SQLSETTINGS_DRIVERNAME=mysql
      - MM_SQLSETTINGS_DATASOURCE=MM_USERNAME:MM_PASSWORD@tcp(DB_HOST:DB_PORT_NUMBER)/MM_DBNAME?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s
```
