# AI-suggested version from Copilot

def sort_list_of_dicts(data, key_name):
    try:
        return sorted(data, key=lambda item: item.get(key_name, 0))
    except (TypeError, KeyError) as e:
        print(f"Error sorting data: {e}")
        return data

# Example usage
people = [
    {"name": "Irene", "score": 88},
    {"name": "Jake", "score": 75},
    {"name": "Emily", "score": 92}
]

print(sort_list_of_dicts(people, "score"))
