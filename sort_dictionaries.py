# Manual Implementation
def sort_dictionaries_manual(dict_list, key):
    """
    Sort a list of dictionaries by a specific key.
    Args:
        dict_list: List of dictionaries
        key: Key to sort by
    Returns:
        Sorted list of dictionaries
    """
    return sorted(dict_list, key=lambda x: x[key])

# AI-Suggested Implementation (Simulated GitHub Copilot)
def sort_dictionaries_ai(dict_list, key):
    """
    Sort a list of dictionaries by a specific key with error handling.
    Args:
        dict_list: List of dictionaries
        key: Key to sort by
    Returns:
        Sorted list of dictionaries
    Raises:
        KeyError: If key is not found in any dictionary
    """
    try:
        from operator import itemgetter
        return sorted(dict_list, key=itemgetter(key))
    except KeyError:
        raise KeyError(f"Key '{key}' not found in one or more dictionaries")

# Test
data = [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 20}]
print("Manual:", sort_dictionaries_manual(data, 'age'))
print("AI:", sort_dictionaries_ai(data, 'age'))