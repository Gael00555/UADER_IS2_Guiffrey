import unittest
import math
from rpn import RPNError, run


class TestRPN(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(run("3 4 +"), 7)
        self.assertEqual(run("5 1 2 + 4 * + 3 -"), 14)

    def test_errors_basic(self):
        with self.assertRaises(RPNError):
            run("3 0 /")
        with self.assertRaises(RPNError):
            run("+")
        with self.assertRaises(RPNError):
            run("2 a +")

    def test_constants(self):
        self.assertAlmostEqual(run("pi"), math.pi)
        self.assertAlmostEqual(run("e"), math.e)

    def test_functions(self):
        self.assertEqual(run("9 sqrt"), 3)
        self.assertAlmostEqual(run("100 log"), 2)
        self.assertAlmostEqual(run("1 ln"), 0)

    def test_trig(self):
        self.assertAlmostEqual(run("0 sin"), 0)
        self.assertAlmostEqual(run("0 cos"), 1)
        self.assertAlmostEqual(run("1 atan"), 45, places=1)

    def test_inverse_trig(self):
        self.assertAlmostEqual(run("0 asin"), 0)
        self.assertAlmostEqual(run("1 acos"), 0)

    def test_stack(self):
        self.assertEqual(run("5 dup +"), 10)
        self.assertEqual(run("3 4 swap -"), 1)
        self.assertEqual(run("5 6 drop"), 5)

    def test_memory(self):
        self.assertEqual(run("5 sto00 rcl00"), 5)
        with self.assertRaises(RPNError):
            run("rcl99")

    def test_extra(self):
        self.assertEqual(run("2 3 y^x"), 8)
        self.assertEqual(run("2 1/x"), 0.5)
        self.assertEqual(run("2 10x"), 100)

    def test_errors_extra(self):
        with self.assertRaises(RPNError):
            run("-1 sqrt")
        with self.assertRaises(RPNError):
            run("ln -1")

    def test_final_error(self):
        with self.assertRaises(RPNError):
            run("3 4")

    # =========================
    # TESTS NUEVOS (CLAVE)
    # =========================

    def test_dup_empty(self):
        with self.assertRaises(RPNError):
            run("dup")

    def test_log_error(self):
        with self.assertRaises(RPNError):
            run("0 log")

    def test_ln_error(self):
        with self.assertRaises(RPNError):
            run("-1 ln")


if __name__ == "__main__":
    unittest.main()