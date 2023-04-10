import shutil
import os.path

# File extensions and which folder they belong to
FILE_EXTENSIONS = {
    'jpeg': 'Image',
    'jpg': 'Image',
    'img': 'Image',
    'gif': 'Image',
    'png': 'Image',
    'webn': 'Image',
    'txt': 'Document',
    'csv': 'Document',
    'pdf': 'Document',
    'doc': 'Document',
    'docx': 'Document',
    'exe': 'App',
    'py': 'Python',
    'html': 'Web',
    'css': 'Web',
    'mp3': 'Audio',
    'wav': 'Audio',
    'zip': 'Archives',
    'rar': 'Archives',
    'mp4': 'Video',
}


# func to get file name
def get_file(root):
    for file in os.listdir(root):
        if not os.path.isfile(os.path.join(root, file)):
            continue

        yield file


# function to create a folder according to file type (if this folder does not already exist)
def create_folder(root, extension):
    folder_name = FILE_EXTENSIONS.get(extension, 'Other')
    if os.path.exists(os.path.join(root, folder_name)):
        return folder_name

    os.mkdir(os.path.join(root, folder_name))
    return folder_name


folder_path = input("Enter the path of the folder: ")

if not os.path.exists(folder_path):
    raise ValueError("Folder does not exist")

for file_name in get_file(folder_path):
    folder = create_folder(folder_path, file_name.split('.')[-1])
    new_path = os.path.join(folder_path, folder)
    shutil.move(os.path.join(folder_path, file_name), os.path.join(new_path, file_name))
