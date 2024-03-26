from lib.funcoes import *

def menu_principal():
    print("----- MENU PRINCIPAL -----")
    print("1. Cadastrar veículo")
    print("2. Consultar veículos")
    print("3. Cadastrar motorista")
    print("4. Consultar motoristas")
    print("0. Sair")

def main():
    criar_tabelas()
    while True:
        menu_principal()
        opcao = input("Digite a opção desejada: ")
        if opcao == "0":
            print("Sistema encerrado.")
            break
        elif opcao == "1":
            tipo = input("Digite o tipo do veículo (carro, caminhão, motocicleta): ")
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = int(input("Digite o ano do veículo: "))
            id_motorista = int(input("Digite o ID do motorista responsável: "))
            cadastrar_veiculo(tipo, marca, modelo, ano, id_motorista)
        elif opcao == "2":
            consultar_veiculos()
        elif opcao == "3":
            nome = input("Digite o nome do motorista: ")
            idade = int(input("Digite a idade do motorista: "))
            tipo_habilitacao = input("Digite o tipo de habilitação do motorista (carro, caminhão, motocicleta): ")
            cadastrar_motorista(nome, idade, tipo_habilitacao)
        elif opcao == "4":
            consultar_motoristas()
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()
