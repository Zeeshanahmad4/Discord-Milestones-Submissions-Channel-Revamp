import unittest
from unittest.mock import MagicMock
from src.milestone_manager import MilestoneManager


class TestMilestoneManager(unittest.TestCase):
    def setUp(self):
        self.milestone_manager = MilestoneManager()

    def test_create_milestone(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.milestone_manager.create_milestone('Test milestone')
            mock_print.assert_called_once_with("New milestone created: Test milestone")

    def test_submit_milestones(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.milestone_manager.submit_milestones()
            mock_print.assert_called_once_with("Milestone checklist submitted")

    def test_complete_milestone(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.milestone_manager.complete_milestone('Test milestone')
            mock_print.assert_called_once_with("Milestone completed: Test milestone")

    def test_verify_milestone(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.milestone_manager.verify_milestone('Test milestone')
            mock_print.assert_called_once_with("Milestone verified: Test milestone")


if __name__ == '__main__':
    unittest.main()
