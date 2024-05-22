import os

dir1 = "backup_Apple/S_9AE48BF4-AC26-473B-9C73-1EA9CB5F4D2A"
dir2 = "backup_Apple/S_C676EA9A-DB38-4063-808C-3DA50C3AF90E"
dir0 = "Home/Documents/applebackup/search-path"

file_catalog = {}

num = int(input("Which directory do you want to open? 1 or 2.\n"))

match num:
    case 1:
        print("ok")
        contend = os.listdir(dir1)
        for caminho, diretorios, arquivos in os.walk(dir1):
            print(caminho)
            print(diretorios)
            print("\n", arquivos)
        for element in contend:
            element_path = os.path.join(dir1, element)
            if os.path.isfile(element_path):
                print("Arquivo:", element)
                print("Local:", element_path)
                print("\n")
            elif os.path.isdir(element_path):
                print("Diretorio: ", element)

    case 2:
        print("ok2")
        contend = os.listdir(dir2)
        for element in contend:
            element_path = os.path.join(dir2, element)
            if os.path.isfile(element_path):
                print("Arquivo: ", element)
            elif os.path.isdir(element_path):
                print("Diretorio: ", element)
    case _:
        exit(1)
