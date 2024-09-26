from fastapi import APIRouter, Depends
from enum import Enum
from pydantic import BaseModel
from src.api import auth

"""
version 1 additions
"""
import sqlalchemy
from src import database as db

""" put in every method with "/plan" """

"""
with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(sql_to_execute))
"""

router = APIRouter(
    prefix="/bottler",
    tags=["bottler"],
    dependencies=[Depends(auth.get_api_key)],
)

class PotionInventory(BaseModel):
    potion_type: list[int]
    quantity: int

@router.post("/deliver/{order_id}")
def post_deliver_bottles(potions_delivered: list[PotionInventory], order_id: int):
    """ """
    print(f"potions delievered: {potions_delivered} order_id: {order_id}")

    return "OK"

@router.post("/plan")
def get_bottle_plan():
    """
    Go from barrel to bottle.
    """

    # Each bottle has a quantity of what proportion of red, blue, and
    # green potion to add.
    # Expressed in integers from 1 to 100 that must sum up to 100.

    # "potion_type": [r, g, b, d],
    # "quantity": "integer"

    # Initial logic: bottle all barrels into green potions.

    sql = "SELECT num_green_ml FROM global-inventory"
    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(sql)).scalar()

    # each potion bottle is 100 ml
    can_bottle = result//100 #// is an operator that divides and rounds down to nearest whole 
    
    if can_bottle == 0:
        return []
    else:
        return [
                {
                    "potion_type": [0, 100, 0, 0],
                    "quantity": can_bottle,
                }
            ]

if __name__ == "__main__":
    print(get_bottle_plan())