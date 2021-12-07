import shutil

# open('teste.txt', 'w')  - Cria um arquivo "teste.txt" com o acesso "w" para escrita
# Se o arquivo já existir ele abre o arquivo, caso contrário ele cria e abre o arquivo.

# arquivo = open('teste.txt', 'w')    # criamos a variável "arquivo" para podermos escrever no arquivo.
#arquivo = open('teste.txt', 'a')

# (CUIDADO) o "write" em conjunto com o atributo 'w' especificado no método "open" sobrescreve o que tem escrito no arquivo!!
# Utilizar o "write" em conjunto com o atributo 'a' especificado no método "open" não sobrescreve o que tem escrito no arquivo!!
#arquivo.write('minha segunda linha\n')

#arquivo.close()     # fecha o arquivo

def escrever_arquivo(caminho, texto):
    arq = open(caminho, 'w')
    arq.write(texto)
    arq.close()

def atualizar_arquivo(caminho, texto):
    arq = open(caminho, 'a')
    arq.write(texto)
    arq.close()

def ler_arquivo(caminho):
    arq = open(caminho, 'r')
    texto = arq.read()
    print(texto)

def media_notas(caminho):
    arq = open(caminho, 'r')
    aluno_nota = arq.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        if len(x) > 1:
            aluno = x.split(',')
            nome = aluno[0]
            aluno.pop(0)
            #print(aluno)
            media = lambda notas: sum([int(i) for i in notas]) / 4
            #media = (int(aluno[1]) + int(aluno[2]) + int(aluno[3]) + int(aluno[4])) / 4
            #print('O aluno {} teve média {}.'.format(nome, media(aluno)))
            lista_media.append({nome:media(aluno)})
        
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/PROJETOS/DIO/Python/Notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/PROJETOS/DIO/Python/')

if __name__ == '__main__':
    #diretorio = 'C:/PROJETOS/DIO/Python/teste.txt'
    diretorio = 'notas.txt'
    #escrever_arquivo(diretorio, "Rafael,10,10,5,5\n")
    #atualizar_arquivo(diretorio, "Felipe,7,8,5,6\n")
    #atualizar_arquivo(diretorio, "Galleani,7,8,5,6\n")
    #atualizar_arquivo(diretorio, "Cesar,7,9,3,8\n")
    #ler_arquivo(diretorio)

    lista_media = media_notas(diretorio)
    print(lista_media)

    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
