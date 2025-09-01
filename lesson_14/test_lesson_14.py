import unittest
from lesson_14 import TeamLead


class MyTest(unittest.TestCase):

    def test_salary_presence(self):
        team_lead_1 = TeamLead(name="Sasha", salary="5000cf", department="Automation Testing",
                               programming_language="Phyton", team_size="2")
        expected_salary = "5000cf"
        actual_salary = team_lead_1.salary
        self.assertEqual(expected_salary, actual_salary)

    def test_department_presence(self):
        team_lead_1 = TeamLead(name="Sasha", salary="5000cf", department="Automation Testing",
                               programming_language="Phyton", team_size="2")
        expected_department = "Automation Testing"
        actual_department = team_lead_1.department
        self.assertEqual(expected_department, actual_department)