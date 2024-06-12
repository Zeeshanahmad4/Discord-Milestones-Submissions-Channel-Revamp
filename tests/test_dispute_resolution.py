import unittest
from unittest.mock import MagicMock
from src.dispute_resolution import DisputeResolution


class TestDisputeResolution(unittest.TestCase):
    def setUp(self):
        self.dispute_resolution = DisputeResolution()

    def test_raise_dispute(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.dispute_resolution.raise_dispute('Test milestone', 'Test reason')
            mock_print.assert_called_once_with("Dispute raised for milestone: Test milestone - Reason: Test reason")

    def test_resolve_dispute(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.dispute_resolution.resolve_dispute('12345', 'Resolved')
            mock_print.assert_called_once_with("Dispute 12345 resolved: Resolved")


if __name__ == '__main__':
    unittest.main()
