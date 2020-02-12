# project mobi
## webserver docker compose file
Run nginx in a container with letsencrypt companion for ssl cetificates. The dockergen container automatically checks for new containers on the nginx-proxy network and changes the nginx configuration. 

We also want apache proxied behind nginx. Ideally all requests nginx can't handle go to apache? So all files would be served from their location and nginx will proxy pass to the container with open ports for the other installed applications.

--> find out how this would work with a cms like october. Does october have a cms built in?

```yaml
version: '3'

services:
  nginx:
    image: nginx:latest
    #container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs
    labels:
      - "com.github.jrcs.letsencrypt_nginx_proxy_companion.nginx_proxy=true"
  
  apache:
    image: httpd
    hostname: fabianvolkers.com
    volumes:
      - html:/var/www/html
      - ./html:/usr/local/apache2/htdocs/
    environment:
      - VIRTUAL_HOST=fabianvolkers.com
      - VIRTUAL_PORT=8080
      - LETSENCRYPT_HOST=fabianvolkers.com
      - LETSENCRYPT_EMAIL=fabian.volkers@gmail.com      
    restart: always
    ports:
      - "8080:80"

  dockergen:
    image: jwilder/docker-gen:latest
    #container_name: nginx-proxy-gen
    depends_on:
      - nginx
    command: -notify-sighup nginx -watch -wait 5s:30s /etc/docker-gen/templates/nginx.tmpl /etc/nginx/conf.d/default.conf
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - ./nginx.tmpl:/etc/docker-gen/templates/nginx.tmpl:ro

  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion
    #container_name: nginx-proxy-le
    depends_on:
      - nginx
      - dockergen
    environment:
      NGINX_PROXY_CONTAINER: nginx
      NGINX_DOCKER_GEN_CONTAINER: dockergen
      DEFAULT_EMAIL: fabian.volkers@gmail.com
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs
      - /var/run/docker.sock:/var/run/docker.sock:ro

volumes:
  conf:
  vhost:
  html:
  certs:

# Do not forget to 'docker network create nginx-proxy' before launch, and to add '--network nginx-proxy' to proxied containers. 

networks:
  default:
    external:
      name: nginx-proxy
```


