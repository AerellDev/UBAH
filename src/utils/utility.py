import os

def clearConsoleWindows():
    os.system('cls')


def deleteIsiFolder(folder_path):
    # Mengambil daftar file dan folder dalam folder_path
    file_list = os.listdir(folder_path)
    # Menghapus semua file dan folder dalam folder_path
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)