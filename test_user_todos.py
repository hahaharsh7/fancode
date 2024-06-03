import unittest
from unittest.mock import patch
from main import get_users, get_todos, get_fancode_users, calculate_completed_tasks_percentage, is_fancode_city

class TestUserTodos(unittest.TestCase):

    @patch('main.get_users')
    @patch('main.get_todos')
    def setUp(self, mock_get_users, mock_get_todos):
        self.users = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "address": {
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                }
            },
            {
                "id": 2,
                "name": "Ervin Howell",
                "address": {
                    "geo": {
                        "lat": "-45.0",
                        "lng": "70.0"
                    }
                }
            }
        ]
        self.todos = [
            {"userId": 1, "id": 1, "completed": True},
            {"userId": 1, "id": 2, "completed": False},
            {"userId": 2, "id": 3, "completed": True}
        ]
        mock_get_users.return_value = self.users
        mock_get_todos.return_value = self.todos

    def test_is_fancode_city(self):
        self.assertTrue(is_fancode_city(-37.3159, 81.1496))
        self.assertFalse(is_fancode_city(-45.0, 70.0))

    def test_get_fancode_users(self):
        fancode_users = get_fancode_users(self.users)
        self.assertEqual(len(fancode_users), 1)
        self.assertEqual(fancode_users[0]['name'], "Leanne Graham")

    def test_calculate_completed_tasks_percentage(self):
        percentage = calculate_completed_tasks_percentage(self.todos, 1)
        self.assertEqual(percentage, 50.0)

    def test_main_output(self):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("User Leanne Graham has completed 50.00% of their tasks.")

if __name__ == '__main__':
    unittest.main()
