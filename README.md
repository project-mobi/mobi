# project mobi <!-- omit in toc -->
## Contents <!-- omit in toc -->
- [1. Intro](#1-intro)
- [2. Services](#2-services)
- [3. Databases](#3-databases)
- [4. Installation with docker-compose](#4-installation-with-docker-compose)
  - [Prerequisites](#prerequisites)
    - [Create docker networks](#create-docker-networks)
  - [Mobi mainframe (nginx server)](#mobi-mainframe-nginx-server)
  - [Mobi databases](#mobi-databases)
  - [Mobi mass (nextcloud)](#mobi-mass-nextcloud)
- [4. Setup](#4-setup)
- [Besonderheiten](#besonderheiten)
- [Table of Contents](#table-of-contents)

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

#### Create docker networks
```bash
docker network create nginx-proxy
```

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

## Table of Contents
1. [Webserver with nginx and letsencrypt](./nginx.md)
2. [Databases](./databases.md)
3. [Nextcloud](./nextcloud.md)
4. [Mattermost](./mattermost.md)

We use a series of networks and containers communicating with eachother the achieve the full suite of services we offer. The core setup consists of an nginx container with a letsencrypt companion on the `nginx-proxy network`. Every container with an opened port and a supplied FQDN will be connected to this network and traffic to the internet is opened.



For a more detailed overview visit the services own docs page.
