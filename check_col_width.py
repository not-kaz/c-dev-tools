import os

def calculate_column_width(file_path, max_width):
    problematic_lines = []
    
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            column_width = 0
            for char in line:
                if char == '\t':  # Assuming tab width is 4 spaces
                    column_width += 8
                elif char == ' ':
                    column_width += 1
                elif char == '\n':
                    continue
                else:
                    column_width += len(char)
            
            if column_width > max_width:
                problematic_lines.append((file_path, line_num, column_width))
    
    return problematic_lines

def check_files(directory, max_width):
    problematic_lines = []
    
    for file_name in os.listdir(directory):
        if file_name.endswith(('.c', '.h')):
            file_path = os.path.join(directory, file_name)
            lines = calculate_column_width(file_path, max_width)
            problematic_lines.extend(lines)
    
    return problematic_lines

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    max_width = input("Enter the maximum column width: ")
    try:
        max_width = int(max_width)
    except ValueError:
        print("Invalid input for maximum column width. Please enter an integer.")
        return
    
    problematic_lines = check_files(directory, max_width)
    if problematic_lines:
        print("Column width exceeds the maximum limit in the following files:")
        for file_path, line_num, column_width in problematic_lines:
            print(f"{file_path}, Line {line_num}, Count {column_width}")
    else:
        print("Column width is within the specified limit in all files.")

if __name__ == "__main__":
    main()
