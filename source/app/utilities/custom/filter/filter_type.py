def filter_type ( type ):

    if type in [ 'number', 'string', 'boolean', 'Object' ]:

        return f"<color:gray>{{{type}}}</color>"

    elif type is None:

        return ''

    else:

        return f"{{{type}}}"
