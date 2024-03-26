from database import *

def cadastrar_veiculo(tipo, marca, modelo, ano, id_motorista):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Veiculos (tipo, marca, modelo, ano, id_motorista) VALUES (?, ?, ?, ?, ?)",
                   (tipo, marca, modelo, ano, id_motorista))
    conn.commit()
    conn.close()
    print("Veículo cadastrado com sucesso!")

def consultar_veiculos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Veiculos")
    veiculos = cursor.fetchall()
    conn.close()

    if veiculos:
        print("----- VEÍCULOS CADASTRADOS -----")
        for veiculo in veiculos:
            print(f"ID: {veiculo[0]}, Tipo: {veiculo[1]}, Marca: {veiculo[2]}, Modelo: {veiculo[3]}, Ano: {veiculo[4]}, ID Motorista: {veiculo[5]}")
    else:
        print("Nenhum veículo cadastrado.")

def cadastrar_motorista(nome, idade, tipo_habilitacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Motoristas (nome, idade, tipo_habilitacao) VALUES (?, ?, ?)",
                   (nome, idade, tipo_habilitacao))
    conn.commit()
    conn.close()
    print("Motorista cadastrado com sucesso!")

def consultar_motoristas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Motoristas")
    motoristas = cursor.fetchall()
    conn.close()

    if motoristas:
        print("----- MOTORISTAS CADASTRADOS -----")
        for motorista in motoristas:
            print(f"ID: {motorista[0]}, Nome: {motorista[1]}, Idade: {motorista[2]}, Tipo de Habilitação: {motorista[3]}")
    else:
        print("Nenhum motorista cadastrado.")

# Implementar as demais funções conforme os requisitos
