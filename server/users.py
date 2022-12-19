from validators import validate_user
from responser import response
from uuid import uuid4
import Pyro4

class Users:
    _users = []
    _auto_increment_count = 1
    _instance = None

    def __init__(self):
        self._users = []

    @Pyro4.expose
    def index(self):
        return response(self._users)

    @Pyro4.expose
    def create(self, data):
        user = validate_user(data)

        if user:
            user["id"] = self._auto_increment_count
            self._auto_increment_count += 1
            self._users.append(user)
            return response(user, True)
        return response('', False)

    @Pyro4.expose
    def delete(self, id):
        new_users = []
        found = False
        for user in self._users:
            if user["id"] == id:
                found = True
            else:
                new_users.append(user)
        self._users = new_users
        return response('', found)
