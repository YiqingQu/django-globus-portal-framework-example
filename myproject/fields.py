

def formatted_search_results(result):
    """
    Create a curated list of the results we want to see on the search page.
    """
    entry = result[0]
    result_fields = ['size', 'type']
    return [{
        'field': field,
        'title': field.capitalize(),
        'value': entry.get(field),
    } for field in result_fields]
