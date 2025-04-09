# test_bios.py
import unittest
from bios_sim import verify_password

class TestBIOSPassword(unittest.TestCase):
    def test_correct_password(self):
        self.assertEqual(verify_password("abc123"), "ACCESS GRANTED")

    def test_wrong_password(self):
        self.assertEqual(verify_password("wrong"), "WRONG PASSWORD")

    def test_locked_state(self):
        self.assertEqual(verify_password("abc123", tries_left=0), "LOCKED")

    def test_case_sensitivity(self):
        self.assertEqual(verify_password("ABC123"), "WRONG PASSWORD")

if __name__ == '__main__':
    unittest.main()
