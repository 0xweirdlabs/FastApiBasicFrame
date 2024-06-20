from fastapi import APIRouter, HTTPException, Response
from .datasource import get_item_from_db, get_all_items_from_db
from .transform import transform_item_data, transform_all_items_data

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int):
    item_data = get_item_from_db(item_id)
    if not item_data:
        raise HTTPException(status_code=404, detail="Item not found")
    return transform_item_data(item_data)


@router.get("/items")
def read_items():
    items_data = get_all_items_from_db()
    return transform_all_items_data(items_data)


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)
