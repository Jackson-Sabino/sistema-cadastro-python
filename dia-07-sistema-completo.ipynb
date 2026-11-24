import json
import os

ARQUIVO = "clientes.json"

# --- CARREGA OS CLIENTES QUE JÁ ESTÃO SALVOS ---
def carregar_clientes():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

# --- SALVA OS CLIENTES NO ARQUIVO ---
def salvar_clientes():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)

clientes = carregar_clientes()
print(f"Sistema iniciado com {len(clientes)} cliente(s) salvos!")

while True:
    print("\n=== SISTEMA DE CADASTRO - DIA 8 ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()

        if nome == "" or telefone == "" or email == "":
            print("❌ Erro: preencha todos os campos!")
            continue

        clientes.append({"nome": nome, "telefone": telefone, "email": email})
        salvar_clientes()
        print("✅ Cliente cadastrado E SALVO no arquivo!")

    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for i, c in enumerate(clientes):
                print(f"{i+1} - {c['nome']} | {c['telefone']} | {c['email']}")

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ").lower()
        achou = False
        for c in clientes:
            if busca in c["nome"].lower():
                print(f"Encontrado: {c['nome']} | {c['telefone']} | {c['email']}")
                achou = True
        if not achou:
            print("Cliente não encontrado.")

    elif opcao == "4":
        for i, c in enumerate(clientes):
            print(f"{i+1} - {c['nome']}")
        try:
            num = int(input("Número do cliente para excluir: ")) - 1
            removido = clientes.pop(num)
            salvar_clientes()
            print(f"✅ {removido['nome']} excluído e arquivo atualizado!")
        except:
            print("❌ Número inválido!")

    elif opcao == "5":
        salvar_clientes()
        print("Saindo... Seus clientes estão salvos!")
        break
    else:
        print("Opção inválida!")
