
nginx_yml = '''
  # Nginx reverse proxy container
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
  
'''

apache_yml = '''
  # apache webserver behind Nginx reverse proxy
  apache:
    image: httpd
    hostname: {domain_name}
    volumes:
      - html:/var/www/html
      - ./html:/usr/local/apache2/htdocs/
    environment:
      - VIRTUAL_HOST={domain_name}
      - VIRTUAL_PORT=8080
      - LETSENCRYPT_HOST={domain_name}
      - LETSENCRYPT_EMAIL={webmaster_email}
    restart: always
    ports:
      - "8080:80"

'''

dockergen_yml = '''
  # Container for automatically generating nginx configuration files for active containers based on template 
  dockergen:
    image: jwilder/docker-gen:latest
    depends_on:
      - nginx
    command: -notify-sighup {nginx_container_name} -watch -wait 5s:30s /etc/docker-gen/templates/nginx.tmpl /etc/nginx/conf.d/default.conf
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - ./nginx.tmpl:/etc/docker-gen/templates/nginx.tmpl:ro

'''

letsencrypt_yml = '''
  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion
    #container_name: nginx-proxy-le
    depends_on:
      - nginx
      - dockergen
    environment:
      NGINX_PROXY_CONTAINER: {nginx_container_name}
      NGINX_DOCKER_GEN_CONTAINER: {dockergen_container_name}
      DEFAULT_EMAIL: {webmaster_email}
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs
      - /var/run/docker.sock:/var/run/docker.sock:ro
'''

services = [nginx_yml, apache_yml.format(domain_name="fabianvolkers.com", webmaster_email="webmaster@fabianvolkers.com"), dockergen_yml, letsencrypt_yml]
compose_file = '''
version: '3'

services:

{active_services}

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

print(compose_file.format(active_services=''.join(services)))