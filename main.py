import os
import pathlib

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

current_dir = pathlib.Path.cwd()
dir_path = str(current_dir) + '/files'

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_and_upload_file(file_name='trening.txt', file_content='Первая тренировка!'):
    try:
        drive = GoogleDrive(gauth)

        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'File {file_name} was uploaded! Have a good day!'
    except Exception as _ex:
        return 'Произошла ошибка'


def upload_dir(dir_path=''):
    try:
        drive = GoogleDrive(gauth)

        for file_name in os.listdir(dir_path):
            my_file = drive.CreateFile({'title': f'{file_name}'})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()

            print(f'File {file_name} was uploaded!')

        return 'All files was uploaded! Have a good day!'
    except Exception as _ex:
        return 'Произошла ошибка'


def main():
    # print(create_and_upload_file())
    print(upload_dir(dir_path))


if __name__ == '__main__':
    main()
