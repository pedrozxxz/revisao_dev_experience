alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    idade = input("Digite a idade do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip()

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso!\n")

def listar_alunos():
    if not alunos:
        print("\nNenhum aluno cadastrado ainda.\n")
    else:
        print("\nLista de Alunos:")
        for i, aluno in enumerate(alunos, 1):
            print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
        print()

def pesquisar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"\n🔎 Aluno encontrado:")
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}\n")
            encontrado = True
            break

    if not encontrado:
        print(f"\n❌ Nenhum aluno com o nome '{nome_busca}' foi encontrado.\n")

def menu():
    while True:
        print("\n Sistema de Cadastro de Alunos")
        print("1 → Cadastrar aluno")
        print("2 → Listar todos os alunos")
        print("3 → Pesquisar aluno por nome")
        print("4 → Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            pesquisar_aluno()
        elif opcao == "4":
            print("\n👋 Saindo do sistema... Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida, tente novamente.\n")

menu()