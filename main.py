from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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


def main():
    print(create_and_upload_file())


if __name__ == '__main__':
    main()
