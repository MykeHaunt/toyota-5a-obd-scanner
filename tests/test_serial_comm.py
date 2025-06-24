import unittest
from src.serial_comm import read_codes, clear_codes

class TestSerialComm(unittest.TestCase):
    def test_simulation_read(self):
        codes = read_codes(port='', baudrate=0, simulation=True)
        self.assertIsInstance(codes, list)

    def test_simulation_clear(self):
        self.assertTrue(clear_codes(port='', baudrate=0, simulation=True))

if __name__ == '__main__':
    unittest.main()
