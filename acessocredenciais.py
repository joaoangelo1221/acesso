print("1 - credenciais 1")
print("2 - credenciais 2")
print("3 - credenciais 3")
op1 = 1 
op2 = 2
op3 = 3
usuario1 = "joao"
senha_usuario1 = 123
usuario2 = "angelo"
senha_usuario2 = 1234
op0 = int(input("escolha a credencial"))
if op0 > 3:
    print("opção inexistente")
elif op0 == 1: 
        print("faça login para obter o acesso")
        ap1 = input("digite seu login de usuario:")
        if ap1 != usuario1 and ap1 != usuario2:
            print("acesso negado")
        else:
            ap2 = int(input("digite sua senha: "))
            if ap2 != senha_usuario1 and ap2 != senha_usuario2:
                print("acesso negado")
            else: 
                print("acesso permitido")
                print("informações das credenciais 1: ")
elif op0 == 2: 
        print("faça login para obter o acesso")
        ap1 = input("digite seu login de usuario:")
        if ap1 != usuario1 and ap1 != usuario2:
            print("acesso negado")
        else:
            ap2 = int(input("digite sua senha: "))
            if ap2 != senha_usuario1 and ap2 != senha_usuario2:
                print("acesso negado")
            else: 
                print("acesso permitido")
                print("informações das credenciais 2: ")
elif op0 == 3: 
        print("faça login para obter o acesso")
        ap1 = input("digite seu login de usuario:")
        if ap1 != usuario1 and ap1 != usuario2:
            print("acesso negado")
        else:
            ap2 = int(input("digite sua senha: "))
            if ap2 != senha_usuario1 and ap2 != senha_usuario2:
                print("acesso negado")
            else: 
                print("acesso permitido")
                print("informações das credenciais 3: ")
                