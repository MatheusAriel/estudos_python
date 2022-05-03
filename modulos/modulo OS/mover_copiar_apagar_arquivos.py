import os
import shutil

path_original = r'C:\Users\mathe\Downloads\Exercicio_poo_banco'
path_new = path_original + '2'

try:
    os.mkdir(path_new)
except FileExistsError as e:
    pass
    # print(f'A pasta {path_new} já existe.')

for root, dirs, files in os.walk(path_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(path_new, file)
        # print(old_file_path)
        # print(new_file_path)
        if '.txt' in file:
            # shutil.move(old_file_path, new_file_path)
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo: {file} COPIADO com sucesso !!!')

print('\n', '*' * 99, '\n')

# for root, dirs, files in os.walk(path_new):
#     for file in files:
#         if '.txt' in file:
#             path_file = os.path.join(root, file)
#             if '.txt' in file:
#                 path_delete = r'%s' % path_file
#                 os.remove(path_delete)
#                 print(f'Arquivo: {file} DELETADO com sucesso !!!')
