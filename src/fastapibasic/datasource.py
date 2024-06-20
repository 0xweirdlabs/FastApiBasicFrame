from .config import settings

def get_item_from_db(item_id: int):
    # Mock function to simulate a database call using settings.database_url
    return {"item_id": item_id, "name": f"Item from {settings.database_url}"}

def get_all_items_from_db():
    # Mock function to simulate a database call using settings.database_url
    return [
        {"item_id": 1, "name": f"Item 1 from {settings.database_url}"},
        {"item_id": 2, "name": f"Item 2 from {settings.database_url}"}
    ]
