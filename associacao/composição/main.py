from classes import Cliente

client1 = Cliente('Veronica', 26)
client1.insere_endereco("São Jose dos Campos", "SP")
client1.insere_endereco("Jacareí", "SP")
print(client1.nome)
client1.lista_enderecos()
del client1
print()

client2 = Cliente("Danilo", 23)
client2.insere_endereco("São Jose dos Campos", "SP")
client2.insere_endereco("São Jose dos Campos", "SP")
print(client2.nome)
client2.lista_enderecos()

print("#################################")
