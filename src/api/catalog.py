from fastapi import APIRouter
from src import database as db

router = APIRouter()

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


@router.get("/catalog/", tags=["catalog"])
def get_catalog():
    """
    Each unique item combination must have only a single price.
    """

    """
    inside return[]:
    {
        "sku": "string", /* Matching regex ^[a-zA-Z0-9_]{1,20}$ */
        "name": "string",
        "quantity": "integer", /* Between 1 and 10000 */
        "price": "integer", /* Between 1 and 500 */
        "potion_type": [r, g, b, d] /* r, g, b, d are integers that add up to exactly 100 */
    }
    seperate multiple entries with comma (,)
    """
    
    """
    .scalar returns info as integer -> if doesn't work use another function
    """
    sql = "SELECT num_green_potions FROM global-inventory"
    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(sql)).scalar()

    return [
            {
                "sku": "GREEN_POTION_0",
                "name": "green potion",
                "quantity": result,
                "price": 50,
                "potion_type": [0, 100, 0, 0],
            }
        ]





    