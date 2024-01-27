import os
path = r"C:\Users\nberk\Desktop\WLU\Year 5\Winter 2024\CP423\Assinment 1\data"
os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"

        read_text_file(file_path)
    print("\n")