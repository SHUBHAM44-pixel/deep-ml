def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    dict = {}
    for i in range(len(order)):
        dict[order[i]] = i
    t = []
    
    
    for i in range(len(values)):
        
        if values[i] not in dict.keys():
            t.append(-1)
        else:
            t.append(dict[values[i]])
    return t

    pass