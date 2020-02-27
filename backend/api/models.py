# These are all the api resources

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class HostingPlan:
    id: int
    name: str

@dataclass
class ServiceComponent():
    name: str
    volumes: List[Volume]

@dataclass
class Service:
    name: str
    components: List[ServiceComponent]

@dataclass
class Organisation:
    id: int
    name: str
    services: List[Service]


## Service specific classes
@dataclass
class Volume:
    name: str
    source: str
    dest: str

@dataclass
class Webserver(Service):
    required: True
    components: [Nginx, Dockergen, Letsencrypt, *Apache]

@dataclass    
class Dockergen(ServiceComponent):
    required: True
    nginx_container: str


@dataclass    
class Nginx(ServiceComponent):
    required: True

@dataclass    
class Letsencrypt(ServiceComponent):
    required: True
    nginx_container: str
    dockergen_container: str
    webmaster_email: str

@dataclass
class Apache(ServiceComponent):
    required: False
    domain_name: str
    webmaster_email: str
    

    

