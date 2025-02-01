from dataclasses import dataclass
from typing import List

@dataclass 
class Tag:
    id: int = None
    name: str = None

@dataclass 
class Category:
    id: int = None
    name: str = None

@dataclass 
class Pet:
    id: int = None
    name: str = None
    category: Category = None
    photoUrls: List[str] = None
    tags: List[Tag] = None
    status: str = None