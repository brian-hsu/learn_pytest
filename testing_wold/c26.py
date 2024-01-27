import unittest
from my_tasks import Task

class TestTask(unittest.TestCase):

    def test_task_equality(self):
        t1 = Task("Make Sandwich", "James")
        t2 = Task("Do Something", "Smith")
        self.assertNotEqual(t1, t2)

    def test_dict_equality(self):
        t1_dict = Task("Make Sandwich", "Smith").to_dict()
        t2_dict = Task("Make Sandwich", "Smith").to_dict()
        self.assertEqual(t1_dict, t2_dict)

if __name__ == '__main__':
    unittest.main()




