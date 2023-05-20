import os

if __name__ == '__main__':
    current_path = os.getcwd()
    print(f"Current path: {current_path}")
    for i in range(1, 100):
        file_name = f"{current_path}\\exercises\\ex{i}.py"
        if os.path.exists(file_name):
            print(f"File {file_name} already exists")
            continue
        # with open(f"{current_path}/exercises/", "r") as exercise_file