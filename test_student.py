import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


# Raw
'''
class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')
    
    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        student = Student('John', 'Doe')
        
        self.assertEqual(student.email, 'john.doe@email.com')
'''

# With setup and tear down metods
class TestStudent(unittest.TestCase):

    # Only added for showcasing
    @classmethod
    def setUpClass(cls):
        print("set up class")


    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    # Only added for showcasing
    @classmethod
    def tearDownClass(cls):
        print("tear down Class")


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
    

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    
    def test_apply_extension(self):
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extention(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


    def test_course_schedule_success(self):
        print('test_course_schedule_success')
        with patch ("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    
    def test_course_schedule_fail(self):
        print('test_course_schedule_fail')
        with patch ("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == '__main__':
    unittest.main()
