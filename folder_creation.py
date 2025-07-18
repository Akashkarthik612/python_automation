import os
def folder_create(folder_path):
    new_name = "projects"
    if new_name in folder_path:
        return "folder already present"
    else:
        new_folder = os.makedirs(new_name)
        
    return folder_create

x = folder_create(r"E:\i_phone _14_pro")
print(x)