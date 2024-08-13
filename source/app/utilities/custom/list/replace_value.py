def replace_value ( list, to_replace, replace_with ):

    return [ replace_with if item == to_replace else item for item in list ]
