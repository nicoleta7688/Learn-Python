def validate_str(value, attribute):
    if not isinstance(value, str):
        raise TypeError(f"{attribute} should be str")
    elif value.strip() == "":
        raise ValueError(f"{attribute} should no be empty")

def validate_nr(value, attribute):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{attribute} should be int or float")
    elif value < 0:
        raise ValueError(f"{attribute} should be >= 0")

class Employee():
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_str(value, "name")
        self.__name = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        validate_str(value, "employee_id")
        self.__employee_id = value

    def get_info(self):
        return f"{self.name} ({self.employee_id})"

    def calculate_pay(self):
        raise NotImplementedError("This method should be called by child classes")

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        validate_nr(value, "monthly_salary")
        self.__monthly_salary = value

    def calculate_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        validate_nr(value, "hourly_rate")
        self.__hourly_rate = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        validate_nr(value, "hours_worked")
        self.__hours_worked = value

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales_amount, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        validate_nr(value, "base_salary")
        self.__base_salary = value

    @property
    def sales_amount(self):
        return self.__sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        validate_nr(value, "sales_amount")
        self.__sales_amount = value

    @property
    def commission_rate(self):
        return self.__commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        validate_nr(value, "commission_rate")
        if value > 1:
            raise ValueError("commission_rate must be between 0 and 1")
        self.__commission_rate = value

    def calculate_pay(self):
        return self.base_salary + self.sales_amount * self.commission_rate


def generate_payroll_report(employees):
    employees_report = []
    for employee in employees:
        employees_report.append({
            "employee": employee.get_info(),
            "pay": employee.calculate_pay()
        })

    return employees_report

def main():
    # Employee Payroll tests

    employee = Employee("Anna", "E001")

    assert employee.name == "Anna"
    assert employee.employee_id == "E001"
    assert employee.get_info() == "Anna (E001)"

    try:
        employee.calculate_pay()
        assert False
    except NotImplementedError:
        assert True

    salaried = SalariedEmployee("John", "E002", 3000)

    assert salaried.name == "John"
    assert salaried.employee_id == "E002"
    assert salaried.get_info() == "John (E002)"
    assert salaried.calculate_pay() == 3000

    hourly = HourlyEmployee("Maya", "E003", 20, 80)

    assert hourly.name == "Maya"
    assert hourly.employee_id == "E003"
    assert hourly.get_info() == "Maya (E003)"
    assert hourly.calculate_pay() == 1600

    commission = CommissionEmployee("Leo", "E004", 1000, 5000, 0.1)

    assert commission.name == "Leo"
    assert commission.employee_id == "E004"
    assert commission.get_info() == "Leo (E004)"
    assert commission.calculate_pay() == 1500

    employees = [salaried, hourly, commission]
    report = generate_payroll_report(employees)

    assert report == [
        {"employee": "John (E002)", "pay": 3000},
        {"employee": "Maya (E003)", "pay": 1600},
        {"employee": "Leo (E004)", "pay": 1500}
    ]

    try:
        Employee("", "E001")
        assert False
    except ValueError:
        assert True

    try:
        Employee("Anna", "")
        assert False
    except ValueError:
        assert True

    try:
        SalariedEmployee("John", "E002", -1)
        assert False
    except ValueError:
        assert True

    try:
        HourlyEmployee("Maya", "E003", -20, 80)
        assert False
    except ValueError:
        assert True

    try:
        HourlyEmployee("Maya", "E003", 20, -80)
        assert False
    except ValueError:
        assert True

    try:
        CommissionEmployee("Leo", "E004", -1000, 5000, 0.1)
        assert False
    except ValueError:
        assert True

    try:
        CommissionEmployee("Leo", "E004", 1000, -5000, 0.1)
        assert False
    except ValueError:
        assert True

    try:
        CommissionEmployee("Leo", "E004", 1000, 5000, 1.5)
        assert False
    except ValueError:
        assert True

    try:
        CommissionEmployee("Leo", "E004", 1000, 5000, -0.1)
        assert False
    except ValueError:
        assert True

    print("All Employee Payroll tests passed!")


if __name__ == '__main__':
    main()