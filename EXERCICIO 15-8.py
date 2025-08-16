nome_do_usuario = "leticia"
senha_do_usuario = "123456"

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite a sua senha:  ")

if usuario == nome_do_usuario and senha == senha_do_usuario:
    print("Acesso Liberado! Bem-vindo(a).")

else:
    print("Acesso negado! Usuário ou senha incorretos.")