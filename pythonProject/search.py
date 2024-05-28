from pythonProject.utils import listar_conteudo, carregar_mapeamento

mapping_file_path = "FileInfoList.txt"

dir1 = "backup_Apple/S_9AE48BF4-AC26-473B-9C73-1EA9CB5F4D2A"
dir2 = "backup_Apple/S_C676EA9A-DB38-4063-808C-3DA50C3AF90E"
caminho_json = 'test.json'

num = int(input("Qual diretório você deseja abrir? 1 ou 2.\n"))


match num:
    case 1:
        print("Abrindo o diretório 1...")
        listar_conteudo(dir1)

    case 2:
        print("Abrindo o diretório 2...")
        listar_conteudo(dir2)
        mapeamento = carregar_mapeamento(caminho_json)
    case _:
        print("Opção inválida, abrindo os 2 diretorios...")
        listar_conteudo(dir1)
        listar_conteudo(dir2)
