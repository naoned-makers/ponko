import unittest
from unittest.mock import patch, MagicMock

from ponko import *

MockServoKit = MagicMock()
MockPygame = MagicMock()

modules = {
    "adafruit_servokit.ServoKit": MockServoKit,
    "pygame": MockPygame
}
patcher = patch.dict("sys.modules", modules)
patcher.start()

class TestPonko(unittest.TestCase):

    def test_callback_button_1(self):
        button_callback_1(MockServoKit, MockPygame)

if __name__ == '__main__': 
    unittest.main()