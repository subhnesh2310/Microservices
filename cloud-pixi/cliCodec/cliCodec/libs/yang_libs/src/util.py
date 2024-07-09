

def listify(data):
    if isinstance(data, dict):
        data = [data]
    return data