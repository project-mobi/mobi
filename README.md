# project mobi <!-- omit in toc -->
## Contents <!-- omit in toc -->
- [1. Intro](#1-intro)
- [2. Services](#2-services)
  - [2.1. mobi mainframe](#21-mobi-mainframe)
  - [2.2. mobi mass](#22-mobi-mass)
  - [2.3. mobi messenger](#23-mobi-messenger)
  - [2.4. mobi monitoring](#24-mobi-monitoring)
  - [2.5. authentication](#25-authentication)
- [3. Databases](#3-databases)
- [4. Installation with docker-compose](#4-installation-with-docker-compose)
  - [4.1. Prerequisites](#41-prerequisites)
    - [4.1.1. Install docker-compose](#411-install-docker-compose)
    - [4.1.2. Clone GitHub repository](#412-clone-github-repository)
    - [4.1.3. Create docker networks](#413-create-docker-networks)
  - [4.2. Mobi mainframe (nginx server)](#42-mobi-mainframe-nginx-server)
    - [4.2.1. Configuring the compose file.](#421-configuring-the-compose-file)
    - [4.2.2. Run docker-compose](#422-run-docker-compose)
  - [4.3. mobi authenticator](#43-mobi-authenticator)
    - [4.3.1. Configuring the compose file](#431-configuring-the-compose-file)
    - [4.3.2. Run docker-compose](#432-run-docker-compose)
  - [4.4. Mobi mass (nextcloud)](#44-mobi-mass-nextcloud)
- [5. Direct integration with online management platform](#5-direct-integration-with-online-management-platform)
- [6. Exceptions](#6-exceptions)

---
## 1. Intro
All documentation can be found the respective service's directory (e.g. [mainframe](./mainframe)).

---
## 2. Services
### 2.1. mobi mainframe
webserver for the cloud environment. Includes letsencrypt and nginx reverse proxy with automated config generation for active containers.

Click [here](./mainframe/README.md) for documentation.

### 2.2. mobi mass
Nextcloud instance running behind nginx proxy from [mainframe](#21-mobi-mainframe).

Click [here](./mass/README.md) for documentation.

### 2.3. mobi messenger
Mattermost instance running behind nginx proxy from [mainframe](#21-mobi-mainframe).

Click [here](./messenger/README.md) for documentation.

### 2.4. mobi monitoring
monitoring suite, accessible to customer and us. Includes adminer for database management, prometheus as a data source and grafana for monitoring. We should include alerting as well.

Click [here](./monitoring/README.md) for documentation.

### 2.5. authentication
single-sign-on solution for all services running with the option to connect external services.

Click [here](./auth/README.md) for documentation.

---
## 3. Databases
Configuring the databases properly is vital. We offer the following db types:
- mariadb
- postgres

for more information please look at the databases [README](./backend/databases.md)

---
## 4. Installation with docker-compose
the easiest way to get an instance of mobi up and running is using docker-compose

### 4.1. Prerequisites
Your domains A records are pointing to your servers domain. If testing locally please add the domains you plan on configuring to your `/etc/hosts` file.

#### 4.1.1. Install docker-compose
```bash
$ sudo apt-get install docker-compose
```

#### 4.1.2. Clone GitHub repository
Clone this repository to wherever you need it. Be it your local dev machine or a production server. 
```bash
$ git clone https://github.com/project-mobi/mobi.git
$ cd mobi
```

#### 4.1.3. Create docker networks
We use a series of networks and containers communicating with eachother to achieve the full suite of services we offer. The core setup consists of an nginx container with a letsencrypt companion on the `nginx-proxy network`. Every container with an opened port and a supplied FQDN will be connected to this network and traffic to the internet is opened.

For a more detailed overview visit the services own docs page.

```bash
docker network create nginx-proxy
```

### 4.2. Mobi mainframe (nginx server)
#### 4.2.1. Configuring the compose file. 
Replace the following placeholder values in the docker-compose.yml file
- domain_name
- webmaster_email
- nginx_container_name
- dockergen_container_name
>In the future this will be automated by a python script connected to a web frontend.

#### 4.2.2. Run docker-compose 
```bash
$ docker network create nginx-proxy
$ cd ./mainframe
$ docker-compose up -d
```
### 4.3. mobi authenticator
#### 4.3.1. Configuring the compose file
#### 4.3.2. Run docker-compose
```bash
cd ./auth
docker-compose up -d
```
<!--
### 4.3. Mobi databases
```bash
docker network create database-network
cd ./databases
docker-compose up -d
```
-->
### 4.4. Mobi mass (nextcloud)
```bash
cd ./mass
docker-compose up -d
```

---
## 5. Direct integration with online management platform
We can manage our docker containers through the docker api or one of the SDKs. This saves us from generating docker-compose files and writing shell scripts to start them. It also mitigates the issue of having sensitive information (e.g. passwords and emailaddresses) stored in the docker compose files.

---
## 6. Exceptions


Timezone on macos 
```bash
cd <path/to/yml>
echo "ETC_LOCALTIME=$(readlink /etc/localtime)" >> .env
```



