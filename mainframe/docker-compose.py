compose_file = '''
version: '3'

services:
  # nginx reverse proxy
  nginx:
    image: nginx:latest
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
    hostname: {hostname}
    volumes:
      - html:/var/www/html
      - ./html:/usr/local/apache2/htdocs/
    environment:
      - VIRTUAL_HOST={domain_name}
      - VIRTUAL_PORT=8080
      - LETSENCRYPT_HOST={domain_name}
      - LETSENCRYPT_EMAIL=webmaster@{domain_name}
    restart: always
    ports:
      - "8080:80"

  dockergen:
    image: jwilder/docker-gen:latest
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
      - NGINX_PROXY_CONTAINER=nginx
      - NGINX_DOCKER_GEN_CONTAINER=dockergen
      - DEFAULT_EMAIL=webmaster@projectmobi.io
      - NGINX_WEB=nginx
      - DOCKER_GEN=dockergen
      - LETS_ENCRYPT=letsencrypt    
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
'''