import os

if __name__ == '__main__':
    current_path = os.getcwd()
    print(f"Current path: {current_path}")
    for i in range(61, 100):
        file_name = f"{current_path}\\exercises\\ex{i}.py"
        if os.path.exists(file_name):
            print(f"File {file_name} already exists")
            continue
        print(f"Creating file {file_name}")
        with open(file_name, "w") as exercise_file:
            exercise_file.write(f"def exercise{i}():\n")
            exercise_file.write(f"\traise NotImplementedError(\"Exercise not implemented.\")\n")
            exercise_file.write("\n")
            exercise_file.write("\n")
            exercise_file.write("if __name__ == '__main__':\n")
            exercise_file.write(f"\texercise{i}()\n")
