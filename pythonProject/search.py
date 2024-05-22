import utils

# Definição dos diretórios
dir1 = "backup_Apple/S_9AE48BF4-AC26-473B-9C73-1EA9CB5F4D2A"
dir2 = "backup_Apple/S_C676EA9A-DB38-4063-808C-3DA50C3AF90E"

num = int(input("Qual diretório você deseja abrir? 1 ou 2.\n"))

# Usa uma estrutura match-case para selecionar o diretório
match num:
    case 1:
        print("Abrindo o diretório 1...")
        utils.listar_conteudo(dir1)
    case 2:
        print("Abrindo o diretório 2...")
        utils.listar_conteudo(dir2)
    case _:
        print("Opção inválida. Saindo do programa.")
        exit(1)
