class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email if email else f"{name}@email.com"

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            return (7 - rest_days) * 8
        else:
            return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment


employeeSalary = EmployeeSalary('Azamat', 6, 2)
print(f'{employeeSalary.name} заработал: {employeeSalary.salary()} тенге')
print(f'Электронная почта: {employeeSalary.email}')
print()
employeeSalary = EmployeeSalary('Artur', 12, 4)
print(f'{employeeSalary.name} заработал: {employeeSalary.salary()} тенге')
print(f'Электронная почта: {employeeSalary.email}')
print()
employeeSalary = EmployeeSalary('Ivan', 80, 0)
print(f'{employeeSalary.name} заработал: {employeeSalary.salary()} тенге')
print(f'Электронная почта: {employeeSalary.email}')

