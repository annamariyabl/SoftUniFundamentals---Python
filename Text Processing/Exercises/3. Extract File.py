file = input().split("\\")
for i in file:
    if '.' in i:
        file_name, file_extension = i.split(".")
        print(f'File name: {file_name}')
        print(f'File extension: {file_extension}')