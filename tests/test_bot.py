import unittest
from unittest.mock import MagicMock
from src.bot import bot


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = bot
        self.bot.send = MagicMock()

    def test_create_milestone(self):
        self.bot.on_ready()
        self.bot.create_milestone('Test milestone')
        self.bot.send.assert_called_once_with('Milestone created: Test milestone')

    def test_submit_milestones(self):
        self.bot.on_ready()
        self.bot.submit_milestones()
        self.bot.send.assert_called_once_with('Milestones submitted successfully.')

    def test_complete_milestone(self):
        self.bot.on_ready()
        self.bot.complete_milestone('Test milestone')
        self.bot.send.assert_called_once_with('Milestone completed: Test milestone')

    def test_verify_milestone(self):
        self.bot.on_ready()
        self.bot.verify_milestone('Test milestone')
        self.bot.send.assert_called_once_with('Milestone verified: Test milestone')

    def test_raise_dispute(self):
        self.bot.on_ready()
        self.bot.raise_dispute('Test milestone', 'Test reason')
        self.bot.send.assert_called_once_with("Dispute raised for milestone: Test milestone - Reason: Test reason")

    def test_release_escrow(self):
        self.bot.on_ready()
        self.bot.release_escrow()
        self.bot.send.assert_called_once_with('Escrow funds released.')


if __name__ == '__main__':
    unittest.main()
