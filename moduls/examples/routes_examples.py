ROUTES_EXAMPLE = """# Example route

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from models.item import Item
# 
# router = APIRouter()
# 
# @router.post("/items/", response_model=Item)
# def create_item(item: Item, db: Session = Depends()):
#     return item
# 
# @router.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int, db: Session = Depends()):
#     return {"id": item_id, "name": "example", "description": "example description"}
"""
