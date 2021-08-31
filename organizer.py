# this is so you can interact with the OS
import os

from shutil import move 

# change all instances of 'danielbernal' to your corresponding user directory on your mac!
user = os.getenv('danielbernal')

root_dir = '/Users/danielbernal/Downloads/'.format(user)

image_dir = '/Users/danielbernal/Downloads/images/'.format(user)

documents_dir = '/Users/danielbernal/Downloads/documents/'.format(user)

others_dir = '/Users/danielbernal/Downloads/others/'.format(user)

software_dir = '/Users/danielbernal/Downloads/softwares/'.format(user)

# category wise file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

def get_non_hidden_files_except_current_file(root_dir): 
  return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]
def move_files(files):
  for file in files:
    # file moved and overwritten if already exists
    if file.endswith(doc_types):
      move(file, '{}/{}'.format(documents_dir, file))
      print('file {} moved to {}'.format(file, documents_dir))
    elif file.endswith(img_types):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(software_types):
      move(file, '{}/{}'.format(software_dir, file))
      print('file {} moved to {}'.format(file, others_dir))
    else:
      move(file, '{}/{}'.format(others_dir, file))
      print('file {} moved to {}'.format(file, others_dir))

if __name__ == "__main__":
  files = get_non_hidden_files_except_current_file(root_dir)

move_files(files)

# create 5 folders in your Downloads folder: softwares, images, documents, others, Log
# open up text editor on Mac and create plain txt file and place it in Log folder
# run this command in your terminal 'python3 organizer.py >>~/Downloads/Log/log.txt'
# then you'll notice all your files were organized just like that and a log was documented in the log.txt file! 

