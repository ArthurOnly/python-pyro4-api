import Pyro4

user_controller = Pyro4.Proxy(f"PYRONAME:users")

def interface():
    print("------------------")
    print("1 - Listar        ")
    print("2 - Cadastrar     ")
    print("3 - Deletar       ")
    print("99 - Sair         ")

def handle_choice(choice):
    if choice == 1:
        print(user_controller.index())
    elif choice == 2:
        print(handle_create())
    elif choice == 3:
        print(handle_delete())
    elif choice == 99:
        return True
    return False

def handle_list():
    return user_controller.index()

def handle_create():
    username = input("Insira um username: ")
    email = input("Insira um email: ")
    return user_controller.create({'username': username, 'email': email})

def handle_delete():
    id = int(input("Insira um ID: "))
    return user_controller.delete(id)

def start():
    while True:
        interface()
        choice = int(input("Selecione uma opção: "))
        is_exit = handle_choice(choice)
        if is_exit:
            break

if __name__ == '__main__':
    start()