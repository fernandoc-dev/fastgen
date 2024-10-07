SQLALCHEMY_REPOSITORY_EXAMPLE = """# Example CRUD repository with SQLAlchemy

# This file would be named item.py in the repositories directory

# from sqlalchemy.orm import Session
# from models.item import Item
# 
# def get_item_by_id(db: Session, item_id: int):
#     return db.query(Item).filter(Item.id == item_id).first()
# 
# def create_item(db: Session, item: Item):
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item
"""

SQLMODEL_REPOSITORY_EXAMPLE = """# Example CRUD repository with SQLModel

# This file would be named item.py in the repositories directory

# from sqlmodel import Session, select
# from models.item import Item
# 
# def get_item_by_id(db: Session, item_id: int):
#     statement = select(Item).where(Item.id == item_id)
#     return db.exec(statement).first()
# 
# def create_item(db: Session, item: Item):
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item
"""
