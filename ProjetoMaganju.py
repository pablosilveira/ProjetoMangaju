def listar_quartos(quarto):
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***    QUARTOS CADASTRADOS     ***")
    print("**********************************")
    dados = ["Numero","Pessoa","Tipo","Nome"]
    for i in quarto:
        for x in range(len(i)):
            print(" "+dados[x]+": "+i[x])

def quarto_cadastro(quarto):
    continuar = "s"
    while continuar == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***     CADASTRO DE QUARTOS    ***")
          print("**********************************")
          numero = input("NUMERO DE QUARTOS:")
          pessoa = input("QUANTAS PESSOAS POR QUARTO:")
          tipo = input("TIPO DE QUARTO:")
          nome = input("NOME DAS PESSOAS DO QUARTO:")
          quarto.append([numero,pessoa,tipo,nome])
          continuar = str.lower (input("Continuar? [S/N]:"))

def listar_equipamento(equipamento):
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***  EQUIPAMENTOS CADASTRADOS  ***")
    print("**********************************")
    dados = ["Nome","Tipo","Funcao","Data","Proprietario"]
    for i in equipamento:
        for x in range(len(i)):
            print(" "+dados[x]+": "+i[x])

def equipamento_cadastro(equipamento):
    continuar = "s"
    while continuar == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***  CADASTRO DE EQUIPAMENTOS  ***")
          print("**********************************")
          nome = input("NOME DO EQUIPAMENTO:")
          tipo = input("TIPO DE EQUIPAMENTO:")
          funcao = input("FUNÇÂO DO EQUIPAMENTO:")
          data = input("DATA DA ENTREGA DO EQUIPAMENTO:")
          proprietario = input("PROPRIETÁRIO DO EQUIPAMENTO:")
          equipamento.append([nome,tipo,funcao,data,proprietario])
          continuar = str.lower (input("Continuar? [S/N]:"))

def remove_equipamento(equipamento):
    data= input("Digite a Data da Entrega do Equipamento a ser Removido:")
    for i in equipamento:
        if i [3] == data:
            equipamento.remove(i)
            print("Equipamento Removido!")
            break     

def cadastrar_equipamento(equipamento):
    opcao = ""
    while opcao != "5":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("***  CADASTRO DE EQUIPAMENTOS  ***")
         print("**********************************")
         print("[1] EQUIPAMENTOS               ***")
         print("**********************************")
         print("[2] LISTAR EQUIPAMENTOS        ***")
         print("**********************************")
         print("[3] QUARTOS                    ***")
         print("**********************************")
         print("[4] LISTAR QUARTOS             ***")
         print("**********************************")
         print("[5] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")

         if opcao == "1":
             equipamento_cadastro(equipamento)
         
         elif opcao == "2":
             listar_equipamento(equipamento)
     
         elif opcao == "3":
             quarto_cadastro(quarto)

         elif opcao == "4":
             listar_quartos(quarto)

         elif opcao == "5":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")

def listar_aluno(alunos):
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***   RESIDENTES CADASTRADOS   ***")
    print("**********************************")
    dados = ["Nome","Rg","Cpf","Data","Cidade","Estado","Nacionalidade","Matricula","Curso","Fone","Email"]
    for i in alunos:
        for x in range(len(i)):
            print(" "+dados[x]+": "+i[x])

def cadastrar_aluno(alunos):
    continuar = "s"
    while continuar == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***   CADASTRO DE RESIDENTES   ***")
          print("**********************************")
          nome = input("NOME DO ALUNO:")
          rg = input("RG:")
          cpf = input("CPF:")
          data = input("DATA DE NASCIMENTO:")
          sexo = input("SEXO:")
          cidade = input("CIDADE:")
          estado = input("ESTADO:")
          nacionalidade = input("NACIONALIDADE:")
          matricula = input("MATRICULA:")
          curso = input("CURSO:")
          fone = input("FONE:")
          email = input("EMAIL:")
          alunos.append([nome,rg,cpf,data,cidade,estado,nacionalidade,matricula,curso,fone,email])
          continuar = str.lower (input("Continuar? [S/N]:"))

def cadastrar_residente(alunos):
    opcao = ""
    while opcao != "3":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("[1] CADASTRAR ALUNOS           ***")
         print("**********************************")
         print("[2] LISTAR ALUNOS              ***")
         print("**********************************")
         print("[3] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")

         if opcao == "1":
             cadastrar_aluno(alunos)
     
         elif opcao == "2":
             listar_aluno(alunos)

         elif opcao == "3":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")


def remove_aluno(alunos):
    matricula= input("Digite o numero da Matricula:")
    for i in alunos:
        if i [7] == matricula:
            alunos.remove(i)
            print("Aluno Removido!")
            break

      



def exibir_menuprincipal(alunos,equipamento):
    opcao = ""
    while opcao != "5":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("****        BEM VINDO          ***")
         print("**********************************")
         print("[1] CADASTRAR RESIDENTES       ***")
         print("**********************************")
         print("[2] CADASTRAR EQUIPAMENTOS     ***")
         print("**********************************")
         print("[3] REMOVER RESIDENTE          ***")
         print("**********************************")
         print("[4] REMOVER EQUIPAMENTO        ***")
         print("**********************************")
         print("[5] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")


         if opcao == "1":
             cadastrar_residente(alunos)
     
         elif opcao == "2":
             cadastrar_equipamento(equipamento)

         elif opcao == "3":
             remove_aluno(alunos)

         elif opcao == "4":
             remove_equipamento(equipamento)

         elif opcao == "5":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")


quarto = []
equipamento = []
alunos = []
exibir_menuprincipal(alunos,equipamento)
