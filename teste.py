with open("meu_modulo5/teste.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

try: 
    arquivo = open("meu_modulo5/teste.txt","w")
    arquivo.write('isso mesmo\n')
    print(conteudo)
finally:
    arquivo.close()