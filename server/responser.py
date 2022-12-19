def response(data: dict, success = True, metadata = {}):
    return {
        'data': data,
        'success': success,
        'metadata': metadata
    }