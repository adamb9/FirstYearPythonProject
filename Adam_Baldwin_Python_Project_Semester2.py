#Author: Adam Baldwin
#Script Name: Adam_Baldwin_Python_Project_Semester2
#Description: System that reads employee data from a file and allows users to interact with it in various ways.

#This is the menu function. It displays the options that the user has to choose from and loops until they choose a valid option.
def menu_1(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    chosen_option = 0
    while chosen_option < 1 or chosen_option > 8:
        try:
            while True:
                chosen_option = int(input("1. View all employees\n2. View a particular employee\n"
                                         "3. Edit the salary of an employee\n"
                                         "4. Add a new employee\n5. Delete an employee\n"
                                         "6. Give a bonus to each employee, writing the details to a file\n"
                                         "7. Generate a report for management\n8. Quit"))

                #The input above between 1 and 8 decides which functions are run using the if statements below.
                #All of the functions call some of the 5 lists which we created in order to use their data
                if chosen_option == 1:
                    show_all_employees(employee_number_list, first_name_list, last_name_list, email_list, salary_list)
                elif chosen_option == 2:
                    show_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list)
                elif chosen_option == 3:
                    change_salary(employee_number_list, first_name_list, last_name_list, email_list, salary_list)
                elif chosen_option == 4:
                    add_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list)
                elif chosen_option == 5:
                    remove_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list)
                elif chosen_option == 6:
                    employee_bonus(employee_number_list, first_name_list, last_name_list, salary_list)
                elif chosen_option == 7:
                    generate_report(employee_number_list, first_name_list, last_name_list, salary_list)
                elif chosen_option == 8:
                    print("Goodbye!")
                    return employee_number_list, first_name_list, last_name_list, email_list, salary_list
                #Option 8 ends the menu loop and returns the updated lisrs so they can be saved to a file.
        except ValueError:
             print("Please enter whole numbers only please!\n")

#This function loads the data from our "employee.txt" file and adds it to one of 5 seperate lists which contain employee numbers,
#first names, last names, email addresses, and employee's salaries.
def load_data(name_of_file):
    employee_number_list = []
    first_name_list = []
    last_name_list = []
    email_list = []
    salary_list = []
    #The connection to the .txt file is opened here and the while loop keeps looping, adding data from each employee to the correct lists.
    #The if statement below breaks the loop when there is no more data in the file
    connection = open(name_of_file)
    while True:
        line = connection.readline()
        if line == "":
            break
        line_data = line.split(',')
        employee_number_list.append(int(line_data[0]))
        first_name_list.append(line_data[1])
        last_name_list.append(line_data[2])
        email_list.append(line_data[3])
        salary_list.append(float(line_data[4]))
    connection.close()
    #All of the lists are returned so they can be used elsewhere
    return employee_number_list, first_name_list, last_name_list, email_list, salary_list

#This function saves the updated data in the lists after the menu has been exited
#It does this by opening the "employees.txt" file again and writing the elements from the lists into it using a while loop.
def save_data(name_of_file, employee_number_updated, first_name_updated, last_name_updated, email_updated, salary_updated):
    count = 0
    connection = open(name_of_file, "w")
    while count < len(employee_number_updated):
        connection.write("{},{},{},{},{}\n".format(employee_number_updated[count], first_name_updated[count], last_name_updated[count], email_updated[count], salary_updated[count]))
        count += 1

#This function lists all employees and their respective data using a while loop with a counter
#When the counter no longer is less then the length of the list, the while loop breaks.
def show_all_employees(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    count = 0
    while count < len(employee_number_list):
        print(employee_number_list[count], first_name_list[count], last_name_list[count], email_list[count], salary_list[count], "\n")
        count += 1

#This function asks the user for an employee number and displays their data.
def show_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    count = 0
    employee_found = 0
    #Below is validation for the users input of the employee number. It ensures they enter whole numbers.
    while True:
        try:
            requested_employee = int(input("Please enter an employee number:"))
            break
        except ValueError:
            print("Please enter whole numbers only!")
    #Here we use another while loop with a counter to print the data of the correct employee in an ordered fashion.
    while count < len(employee_number_list):
        if requested_employee == employee_number_list[count]:
            print(employee_number_list[count], first_name_list[count], last_name_list[count], email_list[count], salary_list[count], "\n")
            employee_found += 1
        count += 1
    #The employee_found variable is used to account for when the user enters the employee number of an employee that doesn't exist.
    if employee_found != 1:
        print("This employee doesn't exist! \n")

#This function allows the user to change the salary of an employee based on their employee_number.
def change_salary(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    count = 0
    employee_found = 0
    #Below is the validation to ensure that the user's input is a whole number
    while True:
        try:
            requested_employee = int(input("Please enter an employee number:"))
            break
        except ValueError:
            print("Please enter whole numbers only!")
    #Here the code loops through the employee number list in order to find the correct employee whose salary we want to change
    #When the correct employee is found, their current salary is displayed and the user picks the employee's new salary.
    while count < len(employee_number_list):
        if requested_employee == employee_number_list[count]:
            print("The employee's current salary is €{}".format(salary_list[count]))
            while True:
                try:
                    new_salary = float(input("What would you like the new salary to be?"))
                    break
                except ValueError:
                    print("Please enter numbers only!")
            #This is where the correct salary is changed in the salary_list
            salary_list[count] = new_salary
            print(employee_number_list[count], first_name_list[count], last_name_list[count], email_list[count], salary_list[count], "\n")
            employee_found += 1
        count += 1
    #Again, this ensures that the user selects a valid employee number that exists
    if employee_found != 1:
        print("This employee doesn't exist! \n")

#This function takes the first and last name of a new employee and generates them a unique employee number and email address.
#This data is then added to the correct lists and returned
def add_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    #We need to import random in order to generate a random employee number
    import random
    first_name = str(input("What is the first name of this employee?"))
    last_name = str(input("What is the surname of this employee?"))
    #This is to validate that the user enters only numbers as the employee's salary
    while True:
        try:
            salary = float(input("What is this employee's salary?"))
            break
        except ValueError:
            print("Please enter numbers only!")

   #This generates a random number between 10000 and 99999. It needs to be between these numbers in order for it to be a 5-digit number
    employee_no = random.randint(10000, 99999)
    #The code below ensures the number isn't already in use by another employee
    while employee_no in employee_number_list:
        employee_no = random.randint(10000, 99999)
    #The email address is unique because it contains the employee's name and number, which is unique to each employee.
    email = ("{}.{}{}@cit.ie".format(first_name, last_name, employee_no))

    #This is where the data is added to each list
    employee_number_list.append(employee_no)
    first_name_list.append(first_name)
    last_name_list.append(last_name)
    email_list.append(email)
    salary_list.append(salary)

    return employee_number_list, first_name_list, last_name_list, email_list, salary_list

#This function asks for an employee number of an employee which is being removed.
#It then loops and removes the data of this employee from all of the lists
def remove_employee(employee_number_list, first_name_list, last_name_list, email_list, salary_list):
    count = 0
    employee_found = 0
    #This is validation to ensure the employee number is a whole number.
    while True:
        try:
            removed_employee = int(input("Please enter the employee number of the removed employee:"))
            break
        except ValueError:
            print("Please enter whole numbers only!")
    #This code is used to check through the employee number list file and "pop" all of the data in the lists relating to this employee
    while count < len(employee_number_list):
        if removed_employee == employee_number_list[count]:
            print("Employee {} has been removed!".format(removed_employee))
            employee_number_list.pop(count)
            first_name_list.pop(count)
            last_name_list.pop(count)
            email_list.pop(count)
            salary_list.pop(count)
            employee_found += 1
        count += 1
    #This is here in case the employee doesn't exist in the list
    if employee_found != 1:
        print("This employee doesn't exist! \n")
    return employee_number_list, first_name_list, last_name_list, email_list, salary_list

#This function asks the user for a percentage bonus which they wish to give to employees.
#This bonus is then worked out for each employee and sent to a file with their employee numbers and names.
def employee_bonus(employee_number_list, first_name_list, last_name_list, salary_list):
    count = 0
    #This validates that the input is a number
    while True:
        try:
            bonus = float(input("Please enter the percentage bonus you would like to give every employee:"))
            break
        except ValueError:
            print("Please enter numbers only!")
    #The bonus file is created here to write to
    bonus_file = open("bonus.txt", "w")
    #This loops through each employee and calculates how much money their bonus is. It is then saved to the file.
    while count < len(employee_number_list):
        extra_money = salary_list[count] * (bonus/100)
        bonus_file.write("Employee: {} {} {}   Bonus: €{:.2f}\n".format(employee_number_list[count], first_name_list[count], last_name_list[count], extra_money))
        count += 1
    #The bonus file is closed here
    bonus_file.close()

#This function generates a report which includes the average salary and the largest salary and it's recipient
def generate_report(employee_number_list, first_name_list, last_name_list, salary_list):
    count = 0
    #The report file is created here to write to
    report_file = open("report.txt", "w")
    #The average salary is calculated using the sum() function on the salary list and dividing it by the number of elements in the list
    avg_salary = sum(salary_list) / len(salary_list)
    #The average salary is written to the file here
    report_file.write("Average Salary: {:.2f}\n".format(avg_salary))
    #The largest salary is obtained using the max() function
    largest_salary = max(salary_list)
    #The person who has the largest salary is found by looping through the salary list to find and adding the correct person to the bonus file
    #This will also add more than one person if they both have the largest salaries.
    while count < len(employee_number_list):
        if salary_list[count] == largest_salary:
            report_file.write("Largest Salary: {} {} {} {}\n".format(employee_number_list[count], first_name_list[count], last_name_list[count], salary_list[count]))
        count += 1
    #The file is closed
    report_file.close()


def main():
    #The name of the data file is "employee.txt"
    filename = "employees.txt"
    #The 5 lists are loaded into the variables below using the load_data and the file above
    employee_numbers, first_names, last_names, emails, salaries = load_data(filename)
    #The lists above are loaded into the menu function and then the menu returns the updated versions of these lists
    employee_number_updated, first_name_updated, last_name_updated, email_updated, salary_updated = menu_1(employee_numbers, first_names, last_names, emails, salaries)
    #The updated lists are loaded into the save data function to be saved to the "employees.txt" file.
    save_data(filename, employee_number_updated, first_name_updated, last_name_updated, email_updated, salary_updated)

#The main() function is executed
main()