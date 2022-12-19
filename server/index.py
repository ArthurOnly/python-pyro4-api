import Pyro4
from users import Users

us = Users()

def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(us)
    ns.register('users', str(uri))
    print(f'Ready to listen: '+"PYRONAME:users")
    daemon.requestLoop()

if __name__ == '__main__':
    start_server()
