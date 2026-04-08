class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
     def __init__(self, name, salary, programming_language):
         Employee.__init__(self, name, salary)
         self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size, programming_language):
        Manager.__init__(self, name, salary, department)
        self.programming_language = programming_language
        self.team_size = team_size

def team_lead_attributes():
    team_lead = TeamLead('Olena', 2000, 'Test', 10, 'Python')

    assert hasattr(team_lead, 'name')
    assert hasattr(team_lead, 'salary')
    assert hasattr(team_lead, 'department')
    assert hasattr(team_lead, 'team_size')
    assert hasattr(team_lead, 'programming_language')


team_lead_attributes()

