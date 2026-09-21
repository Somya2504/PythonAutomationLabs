# read mode
def read_employee_file():
    with open("employee_data.txt", "r") as file:
        content = file.read()
        print(content)

read_employee_file()
print("*" * 50)

def read_employee_lines():
    with open("employee_data.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            print(f"Employee: {line.strip()}")

read_employee_lines()
print("*" * 50)

def read_employee_lines_2():
    with open("employee_data.txt", "r") as file:
        for line in file:
            print(f"Employee: {line.strip()}")
read_employee_lines_2()
print("*" * 50)

# write mode

def write_employee_data():
    with open("employee_test.txt", "w") as file:
        file.write("423,Sagar,110000\n")
        file.write("424,Faruk,20000\n")
        file.write("425,Brijesh,30000\n")
        file.write("426,Nathanial,30000\n")
        file.write("427,Bijhitha,45000\n")

    with open("employee_test.txt", "a") as file:       #'a' will append the new data
        file.write("428,Steve,210000\n")

write_employee_data()

# # file creation mode
# def create_employee_batch_file():
#     with open("employee_batch.txt", "x") as file:
#         print("Employee Batch file created successfully")
#
# create_employee_batch_file()
#
# # writelines()
# def write_multiple_employees():
#     with open("employee_batch.txt", "a") as file:
#         employees = [
#             "501,Sangeeta,110000\n",
#             "502,Sweta,225000\n",
#             "503,Anjali,55000\n",
#             "504,Akankhya,135000\n"
#         ]
#         file.writelines(employees)
# write_multiple_employees()

#File Handling + Exception Handling
def create_employee_batch_file():
    employees = [
            "501,Sangeeta,110000\n",
            "502,Sweta,225000\n",
            "503,Anjali,55000\n",
            "504,Akankhya,135000\n"
        ]
    try:
        with open("employee_batch_file.txt", "x") as file:
            file.writelines(employees)
    except FileExistsError:
        print("File already exists")
    else:
        print("File created")
    finally:
        print("File creation process completed.")
create_employee_batch_file()

print("*" * 50)

# JSON file handling
import json
def read_employee_data_json_file():
    with open("employee_data.json",'r') as file:        # read from JSON file
        read_json_file = json.load(file)
        print(read_json_file)
        print(read_json_file["name"])
        print(read_json_file["salary"])
read_employee_data_json_file()

print("*" * 50)

def dump_employee_data_json_file():
    employee_data ={
        "employee_id": 572,
        "name": "Vijay Malaya",
        "salary": 3200000,
        "department": "Department of Aviation"
    }
    with open("employee_data.json",'w') as file:        # write or overwrite the JSON file
        json.dump(employee_data,file, indent=4)         #human-readable test data/config files, use:indent=4
dump_employee_data_json_file()

def read_employee_data_1_json_file():
    with open("employee_data_1.json",'r') as file:
        read_json_file_1 = json.load(file)
        print(read_json_file_1)
        print("*" * 20)

        employees_details = read_json_file_1["employees"]
        for employee in employees_details:
            if employee["salary"] >= 75000:
                print(f"Employee ID: {employee["employee_id"]}")
                print(f"Name: {employee["name"]}")
                print(f"Salary: {employee["salary"]}")
                print(f"Department: {employee["department"]}")
                print("*" * 20)
            else:
                print(
                    f"Employee ID: {employee["employee_id"]} |"
                    f"Name: {employee["name"]} |"
                    f"Salary: {employee["salary"]} |"
                    f"Department: {employee["department"]}"
                )
                print("*" * 20)
read_employee_data_1_json_file()

def update_employee_data_1_json_file():
    with open("employee_data_1.json",'r') as file:
        employees_info = json.load(file)
    employees= employees_info["employees"]

    for employee in employees:
            if employee["employee_id"]== 502:
                employee["salary"] = 85000

    with open("employee_data_1.json", "w") as file:
        json.dump(employees_info, file, indent=4)
update_employee_data_1_json_file()


