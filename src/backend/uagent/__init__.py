from typing import List, Dict
from uagents import Model

class Query(Model):
    text: str

class Results(Model):
    text: str
    results: List

class Choice(Model):
    choice: int
    results: List

class Product(Model):
    text: str
    result: Dict
