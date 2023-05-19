import os

def renamer(file_list,directory):
    print(file_list)
    index=1
    for file_name in file_list:
        if file_name[0] == ".":
            continue  # Skip .DS_Store file
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            extension = file_name.split(".")[-1].upper()
            if extension == "JPEG":
                extension="JPG"
            new_file_name = "IMG_{}.{}".format(index,extension)
            original_file_path= os.path.join(directory,file_name)
            new_file_path= os.path.join(directory, new_file_name)
            if os.path.exists(new_file_path):
                print("Skipping {}: File already exists".format(new_file_path))
                continue
            print(new_file_path)
            os.rename(original_file_path, new_file_path)
            index+=1


def directory(directory):
    file_list= os.listdir(directory)
    file_list.sort()
    for item in file_list:
        if "." not in item:
            file_list.remove(item)
    renamer(file_list,directory)
    



def main():
    directory("/Users/david/Desktop/HTML/Jane_Smiths_Website/images")
if __name__== "__main__":
    main()
