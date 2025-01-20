import os
import shutil

def file_organizer():

    FILES = os.listdir('files')

    try:

        for file in FILES:
            
            file_extensions = f'{file.split('.')[1].lower()}'

            os.makedirs(file_extensions, exist_ok=True)


            shutil.move(f'files/{file}', f'{file_extensions}/{file}')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    file_organizer()