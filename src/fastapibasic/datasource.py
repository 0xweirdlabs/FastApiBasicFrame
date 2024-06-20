from .config import settings


def get_item_from_db(item_id: int) -> dict:
    """
    Simulate a database call to get an item by its ID.

    Parameters
    ----------
    item_id : int
        The ID of the item to retrieve

    Returns
    -------
    dict
        The retrieved item
    """
    return {"item_id": item_id, "name": f"Item from {settings.database_url}"}


def get_all_items_from_db() -> list:
    """
    Simulate a database call to get all items.

    Returns
    -------
    list
        A list of all items
    """
    return [
        {"item_id": 1, "name": f"Item 1 from {settings.database_url}"},
        {"item_id": 2, "name": f"Item 2 from {settings.database_url}"}
    ]
