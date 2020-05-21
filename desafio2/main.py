# ------------------------------------
class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def set_name(self, name):
        self.__name = name

    def set_code(self, code):
        self.__code = code


# ------------------------------------
class Employee:
    def __init__(self, code, name, salary):
        # bloquear instancia individual
        if type(self) == Employee:
            raise TypeError("Instantiate Directly")

        self.__code = code
        self.__name = name
        self.__salary = salary

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_code(self, code):
        self.__code = code

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        pass


# ------------------------------------
class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department("managers", 1)

    def calc_bonus(self):
        return self.get_salary() * 0.15

    def get_departament(self):
        return self.__departament.get_name()

    def set_department(self, nome):
        self.__departament.set_name(nome)

    def get_hours(self):
        return 8


# ------------------------------------
class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department("sellers", 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, plus_sales):
        self.__sales += plus_sales

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.get_name()

    def set_department(self, nome):
        self.__departament.set_name(nome)

    def calc_bonus(self):
        return self.get_sales() * 0.15
