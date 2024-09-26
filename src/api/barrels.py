from fastapi import APIRouter, Depends
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
    prefix="/barrels",
    tags=["barrels"],
    dependencies=[Depends(auth.get_api_key)],
)

class Barrel(BaseModel):
    sku: str

    ml_per_barrel: int
    potion_type: list[int]
    price: int

    quantity: int

@router.post("/deliver/{order_id}")
def post_deliver_barrels(barrels_delivered: list[Barrel], order_id: int):
    """ 
    where you actually change values in database
    """
    print(f"barrels delievered: {barrels_delivered} order_id: {order_id}")

    return "OK"

# Gets called once a day
@router.post("/plan")
def get_wholesale_purchase_plan(wholesale_catalog: list[Barrel]):
    """ 
    logic for if you have enough gold for barrels, don't change values in database

    pseudocode:
    if # if potions in inventory is less than 10:
        purchase a new small green potion barrel

    """
    print(wholesale_catalog)

    return [
        {
            "sku": "SMALL_GREEN_BARREL",
            "quantity": 1,
        }
    ]

