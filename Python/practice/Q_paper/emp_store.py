fileName = "emp.txt"

with open(fileName,'w') as file:
    file.write("Your name is Chhagan Kumawat")

    file.write("\nYour address is Pune")

print(f"'{fileName}' created successfully")

# def write_file(fileName,data):
#     with open(fileName,'w') as file:
#         file.write(data + '\n')

# if __name__ == "__main__":
#     num = int(input("Enter Number of employee: "))
#     for i in range(1,num +1):
#         name = input(f"Enter employee name: {i} ")
#         address = input(f"Enter address: {i}")
#         data = f"\n{name} \n{address}"
#         write_file(fileName,data)
# print("Data written successfully")

# def display_alternate_records(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#             for i in range(0, len(lines), 2):
#                 print(lines[i].strip())
#     except FileNotFoundError:
#         print(f"File '{file_name}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     file_name = "emp.txt"
#     display_alternate_records(file_name)
