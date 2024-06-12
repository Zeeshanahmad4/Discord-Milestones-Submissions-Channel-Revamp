import unittest
from unittest.mock import MagicMock
from src.escrow import Escrow


class TestEscrow(unittest.TestCase):
    def setUp(self):
        self.escrow = Escrow()

    def test_hold_funds(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.escrow.hold_funds(100)
            mock_print.assert_called_once_with("Funds held in escrow: 100")

    def test_release_funds(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.escrow.release_funds()
            mock_print.assert_called_once_with("Funds released from escrow")


if __name__ == '__main__':
    unittest.main()
