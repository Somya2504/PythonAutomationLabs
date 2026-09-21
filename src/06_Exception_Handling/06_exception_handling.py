class InvalidEmployeeError(Exception):
    pass

class IncorrectEmployeeIDError(InvalidEmployeeError):
    pass

class InvalidLeaveDayError(Exception):
    pass

class InsufficientLeaveError(Exception):
    pass

class EmployeeLeave():
    def __init__(self, employee_id, employee_name, leave_balance):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.leave_balance = leave_balance

    def apply_leave(self, requested_days):
        if requested_days <= 0:
            raise InvalidLeaveDayError(
                "Leaves must be greater than Zero"
            )
        if requested_days > self.leave_balance:
            raise InsufficientLeaveError(
                f"Insufficient Leave balance. Available balance =  {self.leave_balance}"
            )

        self.leave_balance -= requested_days
        return self.leave_balance

    def validate_employee(self, entered_employee_id):
        if entered_employee_id <= 0:
            raise InvalidEmployeeError(
                "Employee ID must not be zero"
            )
        if entered_employee_id != self.employee_id:
            raise IncorrectEmployeeIDError(
                f"Employee ID: {entered_employee_id} is unavailable in the Database"
            )

employee_leave = EmployeeLeave(420, "Dharmendhar Pradhan", 15)

try:
    entered_employee_id = int(input("Enter Employee ID: "))
    employee_leave.validate_employee(entered_employee_id)

    requested_days = int(input("Please enter how many days you would like to leave: "))

    remaining_leave_balance = employee_leave.apply_leave(requested_days)

except InvalidEmployeeError as e:
    print(f"Invalid Employee ID: {e}")

except IncorrectEmployeeIDError as e:
    print(f"Incorrect Employee ID: {e}")

except InsufficientLeaveError as e:
    print(f"Insufficient Leaves: {e}")

except InvalidLeaveDayError as e:
    print(f"Invalid Leaves: {e}")

else:
    print("Leave request processed successfully")
    print(f"Remaining Leave balance: {remaining_leave_balance}")

finally:
    print("Leave transaction processing completed.")