import requests 
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict
from typing import list
import csv

@dataclass 
class Car: 
    link: str
    full_name: str
    discription: str
    year: int
    mileage_km: str
    engine_capacity: str
    fuel_type: str 
    price_pln: int
