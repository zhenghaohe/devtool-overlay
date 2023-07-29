```python
def filter_locales(search_term, locales):
    """
    Filters the locales based on the search term.

    Args:
        search_term (str): The search term to filter the locales.
        locales (list): The list of locales.

    Returns:
        list: The filtered locales.
    """
    return [locale for locale in locales if search_term.lower() in locale.lower()]
```