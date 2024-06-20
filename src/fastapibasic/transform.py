def transform_item_data(item_data):
    # Mock function to transform item data
    return {"id": item_data["item_id"], "item_name": item_data["name"]}

def transform_all_items_data(items_data):
    # Mock function to transform a list of items
    return [{"id": item["item_id"], "item_name": item["name"]} for item in items_data]
