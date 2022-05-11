import os
from PIL import Image


def main(images_folder, new_width=500, excluir=False):
    if not os.path.isdir(images_folder):
        raise NotADirectoryError(f'Erro: {images_folder} não é um diretório')

    for root, dirs, files in os.walk(images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_CONVERTED'
            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            #     continue

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo: {new_file_full_path} já existe')
                continue

            # isso evita converter uma arquivo já convertido
            if converted_tag in file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            exif = img_pillow.getexif()
            # print(f'Data da criação {exif.get(36867) }')

            width, heigth = img_pillow.size

            new_heigth = round((new_width * heigth) / width)
            new_image = img_pillow.resize((new_width, new_heigth), Image.LANCZOS)
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=65,
                # exif=img_pillow.info['exif']
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()

            if excluir:
                os.remove(file_full_path)


if __name__ == '__main__':
    images_folder = 'imagens'
    main(images_folder, 150)
