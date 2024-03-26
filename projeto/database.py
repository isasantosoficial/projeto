import sqlite3

def conectar():
    conn = sqlite3.connect('veiculos.db')
    return conn

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Veiculos (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        marca TEXT,
        modelo TEXT,
        ano INTEGER,
        id_motorista INTEGER,
        FOREIGN KEY (id_motorista) REFERENCES Motoristas(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Motoristas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        tipo_habilitacao TEXT
    )
    """)

    conn.commit()
    conn.close()

# Implementar as demais operações de banco de dados conforme os requisitos
