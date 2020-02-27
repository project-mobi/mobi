# These are all the api resources

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class HostingPlan:
    id: int
    name: str
    
@dataclass
class Service:
    name: str

@dataclass
class Organisation:
    id: int
    name: str
    services: List[Service]



