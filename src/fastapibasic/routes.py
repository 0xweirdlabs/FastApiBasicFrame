from fastapi import APIRouter, HTTPException, Response
from .datasource import get_item_from_db, get_all_items_from_db
from .transform import transform_item_data, transform_all_items_data

router = APIRouter()


@router.get("/", summary="Lorem Ipsum")
def read_root() -> dict:
    """
    Root endpoint.

    Returns
    -------
    dict
        A greeting message
    """
    return {"Hello": "World"}


@router.get("/items/{item_id}", tags=["Items"], summary="Lorem Ipsum")
def read_item(item_id: int) -> dict:
    """
    Endpoint to retrieve a single item by its ID.

    Parameters
    ----------
    item_id : int
        The ID of the item to retrieve

    Returns
    -------
    dict
        The retrieved item
    """
    item_data = get_item_from_db(item_id)
    if not item_data:
        raise HTTPException(status_code=404, detail="Item not found")
    return transform_item_data(item_data)


@router.get("/items",tags=["Items"], summary="Lorem Ipsum")
def read_items() -> list:
    """
    Endpoint to retrieve all items.

    Returns
    -------
    list
        A list of all items
    """
    items_data = get_all_items_from_db()
    return transform_all_items_data(items_data)


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """
    Endpoint to handle favicon requests.

    Returns
    -------
    Response
        An empty response with status code 204
    """
    return Response(status_code=204)
