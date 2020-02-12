# Documentation page
## Table of Contents
1. Webserver with nginx and letsencrypt
2. Databases
3. Nextcloud
4. Mattermost

We use a series of networks and containers communicating with eachother the achieve the full suite of services we offer. The core setup consists of an nginx container with a letsencrypt companion on the `nginx-proxy network`. Every container with an opened port and a supplied FQDN will be connected to this network and traffic to the internet is opened.



For a more detailed overview visit the services own docs page.