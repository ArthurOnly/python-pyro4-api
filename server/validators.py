def validate_user(data: dict) -> bool:
    try:
        return {'username': data["username"], "email": data["email"]}
    except:
        return None