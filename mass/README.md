# project mobi - nextcloud

## core setup
nextcloud nicely autoconfigs when the following env vars are supplied. The autoconfig script is only deployed on fresh install. When install failed, reset containers and volumes with `docker-compose down -v` and try again. It is possible that setup of mariadb container takes longer than nextcloud app retries installs. If this is the case, again reset everything with `docker-compose down -v` and try creating only db container first `docker-compose up -f docker-compose.yml db`. Afterwards `ctrl + c` to quit and attempt full docker-compose by entering command `docker-compose up -d`


### For db
creates database and user for nextcloud
- MYSQL_ROOT_PASSWORD=ofKwGisLeTMU5j6mIMCpGoL9
- MYSQL_USER=nextcloud
- MYSQL_PASSWORD=sV7CbxGCtNkZWhC9PLlExJ04
- MYSQL_DATABASE=nextcloud_db

### for app
```yaml
environment:
  - NEXTCLOUD_ADMIN_USER=nextcloud_admin
  - NEXTCLOUD_ADMIN_PASSWORD=sV7CbxGCtNkZWhC9PLlExJ04
  - NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.fabianvolkers.com
  - NEXTCLOUD_UPDATE=1
  - MYSQL_HOST=db
  - MYSQL_USER=nextcloud
  - MYSQL_PASSWORD=sV7CbxGCtNkZWhC9PLlExJ04
  - MYSQL_DATABASE=nextcloud_db 
```
config file
```php
  /**
  * When generating URLs, Nextcloud attempts to detect whether the server is
  * accessed via ``https`` or ``http``. However, if Nextcloud is behind a proxy
  * and the proxy handles the ``https`` calls, Nextcloud would not know that
  * ``ssl`` is in use, which would result in incorrect URLs being generated.
  * Valid values are ``http`` and ``https``.
  */
  'overwriteprotocol' => 'https',
```

sample [config file](https://github.com/nextcloud/server/blob/master/config/config.sample.php#L451)
#### for nginx proxy & letsencrypt
lets our proxy know to issue a new certificate and change nginx configuration
- VIRTUAL_HOST=nextcloud.fabianvolkers.com
- LETSENCRYPT_HOST=nextcloud.fabianvolkers.com
- LETSENCRYPT_EMAIL=fabian.volkers@gmail.com

## additional features to be enabled
these features can be enabled / configured after installation --> maybe thorugh occ command?
### collabora
### encryption
### sso / oauth


## docker compose file
```yaml
version: '3.7'  


services:
    # Detailed below

volumes:
  nextcloud:
  db:

networks:
  nextcloud_network:
  internet_network:

### nextcloud
#### nextcloud app
```yaml
services:

  # [...]

 nextcloud-app:
    image: nextcloud:latest
    container_name: nextcloud-app
    networks:
      - nextcloud_network
      - internet_network
    depends_on:
      - letsencrypt
      - proxy
      - nextcloud-db
    volumes:
      - nextcloud:/var/www/html
      - ./app/config:/var/www/html/config
      - ./app/custom_apps:/var/www/html/custom_apps
      - ./app/data:/var/www/html/data
      - ./app/themes:/var/www/html/themes
    environment:
      - VIRTUAL_HOST=nextcloud.example.com
      - LETSENCRYPT_HOST=nextcloud.example.com
      - LETSENCRYPT_EMAIL=admin@example.com
    restart: unless-stopped
```
#### nextcloud db
```yaml
services:

  # [...]

  nextcloud-db:
    image: mariadb
    container_name: nextcloud-mariadb
    networks:
      - nextcloud_network
    volumes:
      - db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=secret
      - MYSQL_PASSWORD=mysql
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
    restart: unless-stopped
```





 


