import unittest
from functools import partial

from policy import polEval
from parser import parseTextPol, CheckLengthV1


class TestPol(unittest.TestCase):
    testPolicy = {
            "OR": [
                {"AND": [True, False, True]},
                {"AND": [True, True]},
                ],
            }

    longerThan10 = partial(CheckLengthV1, minLength=10)
    testPolicyLength = {
            "OR": [
                {"AND": [longerThan10]},
                ],
            }

    def test_Poleval(self):
        val = polEval(self.testPolicy, "password")
        if not val:
            self.fail()

    def test_PolLength(self):
        val = polEval(self.testPolicyLength, "password20")
        if not val:
            self.fail()


    def test_checkLengthV1(self):
        pol1 = parseTextPol("CheckLengthV1 10")
        if polEval(pol1, "password"):
            self.fail()
        if not polEval(pol1, "password10"):
            self.fail()


    def test_checkSpecialsV1(self):
        pol2 = parseTextPol("CheckLengthV1 10; CheckSpecialsV1 2")
        if polEval(pol2, "password"):
            self.fail()
        if polEval(pol2, "password20"):
            self.fail()
        if polEval(pol2, "LongButWrongBecauseItNeedsTwoSpecialspassword20!"):
            self.fail()
        if not polEval(pol2, "!password20&/"):
            self.fail()

    def test_checkCombinedConventionalAndPassphrase(self):
        pol3 = parseTextPol("CheckLengthV1 10; CheckSpecialsV1 2\nCheckLengthV1 20")
        if polEval(pol3, "password"):
            self.fail()
        if polEval(pol3, "password20"):
            self.fail()
        if not polEval(pol3, "LongButWrongBecauseItNeedsTwoSpecialIsNowOkspassword20!"):
            self.fail()
        if not polEval(pol3, "!password20&/"):
            self.fail()
