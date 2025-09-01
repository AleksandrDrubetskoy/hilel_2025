class Employee:

    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department


class Developer(Employee):

    def __init__(self, name, salary, programming_language, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name=name, salary=salary, department=department, programming_language=programming_language)
        self.team_size = team_size

    def __str__(self):
        return (f"Team Lead has name: {self.name}, salary: {self.salary}, "
                f"department: {self.department}, programming language: {self.programming_language},"
                f" team size: {self.team_size}")


team_lead_1 = TeamLead(name="Sasha", salary="5000cf", department="Automation Testing", programming_language="Phyton",
                       team_size="2")
print(team_lead_1)
