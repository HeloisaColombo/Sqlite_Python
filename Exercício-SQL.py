# Importação da biblioteca sqlite
import sqlite3

#Conexao do banco com o arquivo Python
conexao = sqlite3.connect('wemakers-exercicio')

cursor = conexao.cursor()

#Criação da tabela alunos
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#Inserção de registros na tabela alunos
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1, "Heloísa", 25, "Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2, "Vitor", 27, "Analise de sistemas")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3, "Guilherme", 27, "Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4, "Felipe", 18, "Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5, "Olinda", 58, "Letras")')

#Seleção de todos os registros de alunos

dados_alunos=(cursor.execute('SELECT * FROM alunos'))
for usuario in dados_alunos:
    print(usuario)

#Selecionar todos os alunos com mais de 20 anos

dados_alunos_idade=(cursor.execute('SELECT * FROM alunos WHERE idade>20'))
for usuario in dados_alunos_idade:
    print(usuario)

#Selecionar todos os alunos da Engenharia em ordem alfabética

dados_alunos_eng=(cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome'))
for usuario in dados_alunos_eng:
    print(usuario)

#Contar número de linhas na tabela

##Contagem das linhas
contagem=(cursor.execute('SELECT COUNT(*) FROM alunos'))

##Resultado da query como tupla
resultado = cursor.fetchone()

##Acesso ao resultado, na posição 1
print(resultado[0])

#Atualizando a idade de um aluno especifico

cursor.execute('UPDATE alunos SET idade = 23 WHERE nome = "Felipe"')

#Removendo um aluno pelo id

cursor.execute('DELETE FROM alunos WHERE id = 5')

#Criação da tabela clientes
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

#Inserção de registros na tabela clientes
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1, "Heloísa", 25, 8547)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (2, "Olinda", 58, 10258)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (3, "Jorge", 57, 7800)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (4, "Vitor", 36, 2000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (5, "Pablo", 18, 500)')

#Seleção do nome e da idade dos clientes com mais de 30 anos

dados_clientes_idade=(cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30'))
for usuario in dados_clientes_idade:
    print(usuario)

#Saldo médio dos clientes
clientes_saldo=(cursor.execute('SELECT AVG(saldo) FROM clientes'))

##Resultado da query como tupla
resultado_clientes = cursor.fetchone()

##Acesso ao resultado, na posição 1
print(f"O saldo médio dos clientes é de R${resultado_clientes[0]}.")

#Cliente com saldo máximo

clientes_saldo=(cursor.execute('SELECT MAX(saldo) FROM clientes'))

##Resultado da query como tupla
resultado_maximo = cursor.fetchone()
#Armazenamento do saldo maximo
saldo_max = resultado_maximo[0]

#Subconsulta para encontrar o dono do saldo máximo
clientes_saldo=(cursor.execute('SELECT nome FROM clientes WHERE saldo IN(SELECT MAX(saldo) FROM clientes)'))
nome_maximo = cursor.fetchone()

##Acesso ao resultado, na posição 1, e print da resposta
print(f"O saldo máximo dos clientes é de R${saldo_max}, que pertence ao cliente {nome_maximo[0]}.")

#Contagem de quantos clientes tem saldo superior a 1000

contagem_clientes = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
resultado_clientes=cursor.fetchone()
print(resultado_clientes[0])

#Atualizando o saldo de um cliente especifico

cursor.execute('UPDATE clientes SET saldo = 4658 WHERE id = 4')

#Removendo cliente pelo ID
cursor.execute("DELETE FROM clientes WHERE id=5")

#Criação da tabela compras

cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT)')

#Inserção de registros na tabela compras

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Mochila M", 130)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 1, "Estojo P", 50)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 2, "Uniforme P", 250)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 4, "Apostilas 9º semestre", 900)')

compras_consolidado = cursor.execute('SELECT nome, produto, valor FROM compras LEFT JOIN clientes ON clientes.id=compras.cliente_id')
for usuario in compras_consolidado:
   print(usuario)

#Envio das modificacoes
conexao.commit()
#Encerramento da conexao
conexao.close
