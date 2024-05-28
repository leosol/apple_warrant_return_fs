import os
import json

mapping_file_path = "backup_Apple/FileInfoList.txt"


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
            print("Arquivo:", elemento)
            print("Caminho Completo:", caminho_completo)
            print("\n")


def carregar_mapeamento(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        f = open("test.json")
        mapeamento_l = json.load(f)
        xml = ""
        for a in mapeamento_l:
            print(a["id"])
            for b in a:
                if b == "fields":
                    for c in a[b]:
                        if c == "encryptedAttributes":
                            xml = a[b][c]
                            print(xml)
    return mapeamento_l
