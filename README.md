# project mobi
## Table of Contents
1. Intro
2. Services overview
3. Database setup and config
4. Installation with docker-compose
5. Setup

## 1. Intro
All documentation can be found in `./docs`. For the `docker-compose` files please navigate to the respective service's directory (e.g. [mainframe](./mainframe)).

## 2. Services
1. [Mainframe](./docs/nginx.md)
2. [Mass](./docs/nextcloud.md)
3. [Messenger](./docs/mattermost.md)
4. [Monitoring](./docs/grafana.md)
5. [M...]()

## 3. Databases
Configuring the dbs properly is vital. We offer the following db types:
- mariadb
- postgres

for more information please look at the databases [README](docs/databases.md)

## 4. Installation with docker-compose
Clone this repository to wherever you need it. Be it your local dev machine or a production server. 
### Prerequisites
Your domains A records are pointing to your servers domain. If testing locally please add the domains you plan on configuring to your `/etc/hosts` file.

### Mobi mainframe (nginx server)
```bash
docker network create nginx-proxy
cd /mobi/mainframe
docker-compose up -d
```

### Mobi databases
```bash
docker network create database-network
cd /mobi/databases
docker-compose up -d
```

### Mobi mass (nextcloud)
```bash
cd /mobi/mass
docker-compose up -d
```

## 4. Setup


## Besonderheiten


Timezone on macos 
```bash
cd <path/to/yml>
echo "ETC_LOCALTIME=$(readlink /etc/localtime)" >> .env
```