from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modèle de données
class Item(BaseModel):
    text: str
    is_done: bool = False

# Liste en mémoire pour stocker les items
items: List[Item] = []

# Endpoint racine
@app.get("/")
def root():
    return {"Hello": "World"}

# Créer un nouvel item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Obtenir un item par son ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Lister les items avec une limite facultative
@app.get("/items", response_model=List[Item])
def list_items(limit: int = 10):
    return items[:limit]
