import os

def add_file_to_txt(output_file, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        output_file.write(f"File: {file_path}\n\n")  # Add file name as a header
        output_file.write(file.read())
        output_file.write("\n\n")  # Add some space after each file's content

def convert_directory_to_single_txt(directory, output_txt_path):
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.py')):  # Add more file types if needed
                    file_path = os.path.join(root, file)
                    add_file_to_txt(output_file, file_path)
                    print(f"Added {file_path} to the text file")

if __name__ == "__main__":
    code_base_directory = r"C:\Users\cinco\Desktop\Quant-Tools" # Replace with the path to your code base
    output_txt = r'C:\Users\cinco\Desktop\quanttoolsReadme.txt'  # Path to save the final text file
    convert_directory_to_single_txt(code_base_directory, output_txt)
