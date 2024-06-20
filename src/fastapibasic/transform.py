def transform_item_data(item_data: dict) -> dict:
    """
    Transform item data into the desired format.

    Parameters
    ----------
    item_data : dict
        The original item data

    Returns
    -------
    dict
        The transformed item data
    """
    return {"id": item_data["item_id"], "item_name": item_data["name"]}


def transform_all_items_data(items_data: list) -> list:
    """
    Transform a list of items into the desired format.

    Parameters
    ----------
    items_data : list
        The original list of items

    Returns
    -------
    list
        The transformed list of items
    """
    return [{"id": item["item_id"], "item_name": item["name"]} for item in items_data]
