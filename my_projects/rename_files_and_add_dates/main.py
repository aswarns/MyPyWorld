from datetime import  datetime
import os

#date = datetime.now().strftime("%a-%d-%m-%Y")
date = datetime.now().strftime("%Y-%m-%d")

my_dir = os.listdir("files_dir")
for i in my_dir:
    #filenames = "files_dir/"+i
    filenames = os.path.join("files_dir", i)
    #print(filenames)


    with open (filenames, 'r') as my_file:
        content = my_file.read()
        content = len(content.split())

    new_name = f"{filenames[:-4]}-{date}_words_{content}.txt"
    #print(new_name)

    # Rename the original file to the new filename
    os.rename(filenames, new_name)
    print(f"Old name is {filenames}, and new name is {new_name}")

print("File renaming completed!!!!")