import os


def listar_conteudo(diretorio):
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return

    conteudo = os.listdir(diretorio)
    for elemento in conteudo:
        caminho_completo = os.path.join(diretorio, elemento)
        if os.path.isfile(caminho_completo):
            print("Arquivo:", elemento)
            print("Caminho:", caminho_completo)
            print("\n")
        elif os.path.isdir(caminho_completo):
            print("Diretório:", elemento)
            print("Caminho Completo:", caminho_completo)
            print("\n")
