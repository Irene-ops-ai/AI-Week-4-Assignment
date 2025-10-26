# Manual implementation: Sort a list of dictionaries by a given key

def sort_dicts_by_key(data_list, sort_key):
    """
    Sorts a list of dictionaries based on a specified key.

    Parameters:
        data_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: A new list sorted by the given key.
    """
    return sorted(data_list, key=lambda x: x[sort_key])

# Example usage
records = [
    {"name": "Irene", "score": 88},
    {"name": "Jake", "score": 75},
    {"name": "Emily", "score": 92}
]

sorted_records = sort_dicts_by_key(records, "score")
print(sorted_records)
