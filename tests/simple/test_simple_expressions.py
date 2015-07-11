# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Tests for module simple.simple_expressions."""

import unittest
import os

from simple.simple_expressions import Add, And, Boolean, Divide, \
    GreaterThan, LessThan, Multiply, Number, Not, Or, Subtract, Variable


class ExpressionTests(unittest.TestCase):

    """Tests for module simple.simple_expressions."""

    def __init__(self, *args):
        """Test fixture constructor."""
        super().__init__(*args)
        self.__devnull = open(os.devnull, "w")
        self.__root = os.path.dirname(__file__)
        self.__data_dir = os.path.join(self.__root, "data")

    def __del__(self):
        """Test fixture destructor."""
        if self.__devnull is not None:
            self.__devnull.close()
            self.__devnull = None

    # -------------------------------------------------------------------------+
    # setup, teardown, noop
    # -------------------------------------------------------------------------+

    def setUp(self):  # noqa
        """Create data used by the test cases."""
        import tempfile

        self.tempDirPath = tempfile.TemporaryDirectory()
        return

    def tearDown(self):   # noqa
        """Cleanup data used by the test cases."""
        self.tempDirPath.cleanup()
        self.tempDirPath = None

    def test_noop(self):
        """Excercise tearDown and setUp methods without side effects.

        This test does nothing itself. It is useful to test the tearDown()
        and setUp() methods in isolation (without side effects).

        """
        return

    # -------------------------------------------------------------------------+
    # Add expression tests
    # -------------------------------------------------------------------------+

    def test_add_eq(self):
        """Check Add.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)
        a2n = Add(n1, n2)
        a2b = Add(bt, bf)
        a2v = Add(vx, vy)
        a2e = Add(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_add_evaluate(self):
        """Check Add.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)

        # check the results
        #
        self.assertEqual(Number(1 + 2), a1ne)
        self.assertEqual(Number(True + False), a1be)
        self.assertEqual(Number(5.2 + 3.4), a1ve)
        self.assertEqual(Number((1 + 2) + (5.2 + 3.4)), a1ee)

    def test_add_init(self):
        """Check Add.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a2n = Add(n2, n1)
        a2b = Add(bf, bt)
        a2v = Add(vy, vx)
        a3 = Add(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_add_ne(self):
        """Check Add.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)
        a2n = Add(n1, n2)
        a2b = Add(bt, bf)
        a2v = Add(vx, vy)
        a2e = Add(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_add_repr(self):
        """Check Add.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 + 2»", repr(a1n))
        self.assertEqual("«true + false»", repr(a1b))
        self.assertEqual("«x + y»", repr(a1v))
        self.assertEqual("«1 + 2 + x + y»", repr(a1e))

    def test_add_str(self):
        """Check Add.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 + 2", str(a1n))
        self.assertEqual("true + false", str(a1b))
        self.assertEqual("x + y", str(a1v))
        self.assertEqual("1 + 2 + x + y", str(a1e))

    def test_add_to_python(self):
        """Check Add.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Add(n1, n2)
        a1b = Add(bt, bf)
        a1v = Add(vx, vy)
        a1e = Add(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) + (2)", a1np)
        self.assertEqual("(True) + (False)", a1bp)
        self.assertEqual("(e['x']) + (e['y'])", a1vp)
        self.assertEqual("((1) + (2)) + ((e['x']) + (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # And expression tests
    # -------------------------------------------------------------------------+

    def test_and_eq(self):
        """Check And.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)
        a2n = And(n1, n2)
        a2b = And(bt, bf)
        a2v = And(vx, vy)
        a2e = And(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_and_evaluate(self):
        """Check And.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)
        a1b2 = And(bt, bt)
        a1b3 = And(bf, bf)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)
        a1b2e = a1b2.evaluate(env)
        a1b3e = a1b3.evaluate(env)

        # check the results
        #
        self.assertEqual(Boolean(1 and 2), a1ne)
        self.assertEqual(Boolean(True and False), a1be)
        self.assertEqual(Boolean(5.2 and 3.4), a1ve)
        self.assertEqual(Boolean((1 and 2) and (5.2 and 3.4)), a1ee)
        self.assertEqual(Boolean(True and True), a1b2e)
        self.assertEqual(Boolean(False and False), a1b3e)

    def test_and_init(self):
        """Check And.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a2n = And(n2, n1)
        a2b = And(bf, bt)
        a2v = And(vy, vx)
        a3 = And(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_and_ne(self):
        """Check And.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)
        a2n = And(n1, n2)
        a2b = And(bt, bf)
        a2v = And(vx, vy)
        a2e = And(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_and_repr(self):
        """Check And.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 && 2»", repr(a1n))
        self.assertEqual("«true && false»", repr(a1b))
        self.assertEqual("«x && y»", repr(a1v))
        self.assertEqual("«1 && 2 && x && y»", repr(a1e))

    def test_and_str(self):
        """Check And.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 && 2", str(a1n))
        self.assertEqual("true && false", str(a1b))
        self.assertEqual("x && y", str(a1v))
        self.assertEqual("1 && 2 && x && y", str(a1e))

    def test_and_to_python(self):
        """Check And.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = And(n1, n2)
        a1b = And(bt, bf)
        a1v = And(vx, vy)
        a1e = And(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) and (2)", a1np)
        self.assertEqual("(True) and (False)", a1bp)
        self.assertEqual("(e['x']) and (e['y'])", a1vp)
        self.assertEqual("((1) and (2)) and ((e['x']) and (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # Boolean tests
    # -------------------------------------------------------------------------+

    def test_boolean_eq(self):
        """Check Boolean.__eq__()."""
        # Booleans of various values
        #
        b1t = Boolean(True)
        b1f = Boolean(False)
        b2t = Boolean(True)
        b2f = Boolean(False)

        # Check equality with itself
        #
        self.assertTrue(b1t == b1t)
        self.assertTrue(b1f == b1f)

        # Check equality with same value different object
        #
        self.assertTrue(b1t == b2t)
        self.assertTrue(b1f == b2f)

        # Check equality with different value
        #
        self.assertFalse(b1t == b1f)
        self.assertFalse(b1f == b1t)

    def test_boolean_evaluate(self):
        """Check Boolean.evaluate()."""
        # Booleans of various values
        #
        b1t = Boolean(True)
        b1f = Boolean(False)

        # Evaluate the boolean objects
        #
        env = {}
        b1te = b1t.evaluate(env)
        b1fe = b1f.evaluate(env)

        # Check the results
        #
        self.assertEqual(b1t, b1te)
        self.assertEqual(b1f, b1fe)

    def test_boolean_init(self):
        """Check Boolean.__init__()."""
        # Booleans of various values
        #
        b1t = Boolean(True)
        b1f = Boolean(False)

        # Check the initialization
        #
        self.assertTrue(b1t.value)
        self.assertFalse(b1f.value)

    def test_boolean_ne(self):
        """Check Boolean.__ne__()."""
        # Booleans of various values
        #
        b1t = Boolean(True)
        b1f = Boolean(False)
        b2t = Boolean(True)
        b2f = Boolean(False)

        # Check inequality with itself
        #
        self.assertFalse(b1t != b1t)
        self.assertFalse(b1f != b1f)

        # Check inequality with same value different object
        #
        self.assertFalse(b1t != b2t)
        self.assertFalse(b1f != b2f)

        # Check inequality with different value
        #
        self.assertTrue(b1t != b1f)
        self.assertTrue(b1f != b1t)

    def test_boolean_repr(self):
        """Check Boolean.__repr__()."""
        # Some numbers of various value
        #
        b1t = Boolean(True)
        b1f = Boolean(False)

        # Check representations
        #
        self.assertEqual("«true»", repr(b1t))
        self.assertEqual("«false»", repr(b1f))

    def test_boolean_str(self):
        """Check Boolean.__str__()."""
        # Some numbers of various value
        #
        b1t = Boolean(True)
        b1f = Boolean(False)

        # Check value strings
        #
        self.assertEqual("true", str(b1t))
        self.assertEqual("false", str(b1f))

    def test_boolean_to_python(self):
        """Check Boolean.to_python()."""
        # Some numbers of various value
        #
        b1t = Boolean(True)
        b1f = Boolean(False)

        # Produce python code strings
        #
        b1tp = b1t.to_python(0)
        b1fp = b1f.to_python(0)

        # Check python code strings
        #
        self.assertEqual("True", b1tp)
        self.assertEqual("False", b1fp)

    # -------------------------------------------------------------------------+
    # Divide expression tests
    # -------------------------------------------------------------------------+

    def test_divide_eq(self):
        """Check Divide.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)
        a2n = Divide(n1, n2)
        a2b = Divide(bt, bf)
        a2v = Divide(vx, vy)
        a2e = Divide(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_divide_evaluate(self):
        """Check Divide.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        with self.assertRaises(ZeroDivisionError):
            a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)

        # check the results
        #
        self.assertEqual(Number(1 / 2), a1ne)
        self.assertEqual(Number(5.2 / 3.4), a1ve)
        self.assertEqual(Number((1 / 2) / (5.2 / 3.4)), a1ee)

    def test_divide_init(self):
        """Check Divide.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a2n = Divide(n2, n1)
        a2b = Divide(bf, bt)
        a2v = Divide(vy, vx)
        a3 = Divide(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_divide_ne(self):
        """Check Divide.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)
        a2n = Divide(n1, n2)
        a2b = Divide(bt, bf)
        a2v = Divide(vx, vy)
        a2e = Divide(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_divide_repr(self):
        """Check Divide.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 / 2»", repr(a1n))
        self.assertEqual("«true / false»", repr(a1b))
        self.assertEqual("«x / y»", repr(a1v))
        self.assertEqual("«1 / 2 / x / y»", repr(a1e))

    def test_divide_str(self):
        """Check Divide.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 / 2", str(a1n))
        self.assertEqual("true / false", str(a1b))
        self.assertEqual("x / y", str(a1v))
        self.assertEqual("1 / 2 / x / y", str(a1e))

    def test_divide_to_python(self):
        """Check Divide.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Divide(n1, n2)
        a1b = Divide(bt, bf)
        a1v = Divide(vx, vy)
        a1e = Divide(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) / (2)", a1np)
        self.assertEqual("(True) / (False)", a1bp)
        self.assertEqual("(e['x']) / (e['y'])", a1vp)
        self.assertEqual("((1) / (2)) / ((e['x']) / (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # GreaterThan expression tests
    # -------------------------------------------------------------------------+

    def test_greaterthan_eq(self):
        """Check GreaterThan.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)
        a2n = GreaterThan(n1, n2)
        a2q = GreaterThan(n1, n3)
        a2b = GreaterThan(bt, bf)
        a2v = GreaterThan(vx, vy)
        a2e = GreaterThan(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1q == a1q)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1q == a2q)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1q == a1n)
        self.assertFalse(a1b == a1q)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_greaterthan_evaluate(self):
        """Check GreaterThan.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)
        a2n = GreaterThan(n2, n1)
        a2q = GreaterThan(n3, n1)
        a2b = GreaterThan(bf, bt)
        a2v = GreaterThan(vy, vx)
        a2e = GreaterThan(a1v, a1n)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1qe = a1q.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)
        a2ne = a2n.evaluate(env)
        a2qe = a2q.evaluate(env)
        a2be = a2b.evaluate(env)
        a2ve = a2v.evaluate(env)
        a2ee = a2e.evaluate(env)

        # check the results
        #
        self.assertEqual(Boolean(1 > 2), a1ne)
        self.assertEqual(Boolean(1 > 1), a1qe)
        self.assertEqual(Boolean(True > False), a1be)
        self.assertEqual(Boolean(5.2 > 3.4), a1ve)
        self.assertEqual(Boolean((1 > 2) > (5.2 > 3.4)), a1ee)
        self.assertEqual(Boolean(2 > 1), a2ne)
        self.assertEqual(Boolean(1 > 1), a2qe)
        self.assertEqual(Boolean(False > True), a2be)
        self.assertEqual(Boolean(3.4 > 5.2), a2ve)
        self.assertEqual(Boolean((5.2 > 3.4) > (1 > 2)), a2ee)

    def test_greaterthan_init(self):
        """Check GreaterThan.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(n1, a1q.left)
        self.assertEqual(n3, a1q.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(a1n, a1e.left)
        self.assertEqual(a1v, a1e.right)

    def test_greaterthan_ne(self):
        """Check GreaterThan.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)
        a2n = GreaterThan(n1, n2)
        a2q = GreaterThan(n1, n3)
        a2b = GreaterThan(bt, bf)
        a2v = GreaterThan(vx, vy)
        a2e = GreaterThan(a1n, a1v)

        # Check inequality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1q != a1q)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)

        # Check inequality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1q != a2q)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check inequality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1q != a1n)
        self.assertTrue(a1b != a1q)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_greaterthan_repr(self):
        """Check GreaterThan.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 > 2»", repr(a1n))
        self.assertEqual("«1 > 1»", repr(a1q))
        self.assertEqual("«true > false»", repr(a1b))
        self.assertEqual("«x > y»", repr(a1v))
        self.assertEqual("«1 > 2 > x > y»", repr(a1e))

    def test_greaterthan_str(self):
        """Check GreaterThan.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 > 2", str(a1n))
        self.assertEqual("1 > 1", str(a1q))
        self.assertEqual("true > false", str(a1b))
        self.assertEqual("x > y", str(a1v))
        self.assertEqual("1 > 2 > x > y", str(a1e))

    def test_greaterthan_to_python(self):
        """Check GreaterThan.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = GreaterThan(n1, n2)
        a1q = GreaterThan(n1, n3)
        a1b = GreaterThan(bt, bf)
        a1v = GreaterThan(vx, vy)
        a1e = GreaterThan(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1qp = a1q.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) > (2)", a1np)
        self.assertEqual("(1) > (1)", a1qp)
        self.assertEqual("(True) > (False)", a1bp)
        self.assertEqual("(e['x']) > (e['y'])", a1vp)
        self.assertEqual("((1) > (2)) > ((e['x']) > (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # LessThan expression tests
    # -------------------------------------------------------------------------+

    def test_lessthan_eq(self):
        """Check LessThan.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)
        a2n = LessThan(n1, n2)
        a2q = LessThan(n1, n3)
        a2b = LessThan(bt, bf)
        a2v = LessThan(vx, vy)
        a2e = LessThan(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1q == a1q)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1q == a2q)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1q == a1n)
        self.assertFalse(a1b == a1q)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_lessthan_evaluate(self):
        """Check LessThan.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)
        a2n = LessThan(n2, n1)
        a2q = LessThan(n3, n1)
        a2b = LessThan(bf, bt)
        a2v = LessThan(vy, vx)
        a2e = LessThan(a1v, a1n)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1qe = a1q.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)
        a2ne = a2n.evaluate(env)
        a2qe = a2q.evaluate(env)
        a2be = a2b.evaluate(env)
        a2ve = a2v.evaluate(env)
        a2ee = a2e.evaluate(env)

        # check the results
        #
        self.assertEqual(Boolean(1 < 2), a1ne)
        self.assertEqual(Boolean(1 < 1), a1qe)
        self.assertEqual(Boolean(True < False), a1be)
        self.assertEqual(Boolean(5.2 < 3.4), a1ve)
        self.assertEqual(Boolean((1 < 2) < (5.2 < 3.4)), a1ee)
        self.assertEqual(Boolean(2 < 1), a2ne)
        self.assertEqual(Boolean(1 < 1), a2qe)
        self.assertEqual(Boolean(False < True), a2be)
        self.assertEqual(Boolean(3.4 < 5.2), a2ve)
        self.assertEqual(Boolean((5.2 < 3.4) < (1 < 2)), a2ee)

    def test_lessthan_init(self):
        """Check LessThan.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(n1, a1q.left)
        self.assertEqual(n3, a1q.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(a1n, a1e.left)
        self.assertEqual(a1v, a1e.right)

    def test_lessthan_ne(self):
        """Check LessThan.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)
        a2n = LessThan(n1, n2)
        a2q = LessThan(n1, n3)
        a2b = LessThan(bt, bf)
        a2v = LessThan(vx, vy)
        a2e = LessThan(a1n, a1v)

        # Check inequality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1q != a1q)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)

        # Check inequality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1q != a2q)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check inequality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1q != a1n)
        self.assertTrue(a1b != a1q)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_lessthan_repr(self):
        """Check LessThan.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 < 2»", repr(a1n))
        self.assertEqual("«1 < 1»", repr(a1q))
        self.assertEqual("«true < false»", repr(a1b))
        self.assertEqual("«x < y»", repr(a1v))
        self.assertEqual("«1 < 2 < x < y»", repr(a1e))

    def test_lessthan_str(self):
        """Check LessThan.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 < 2", str(a1n))
        self.assertEqual("1 < 1", str(a1q))
        self.assertEqual("true < false", str(a1b))
        self.assertEqual("x < y", str(a1v))
        self.assertEqual("1 < 2 < x < y", str(a1e))

    def test_lessthan_to_python(self):
        """Check LessThan.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        n3 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = LessThan(n1, n2)
        a1q = LessThan(n1, n3)
        a1b = LessThan(bt, bf)
        a1v = LessThan(vx, vy)
        a1e = LessThan(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1qp = a1q.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) < (2)", a1np)
        self.assertEqual("(1) < (1)", a1qp)
        self.assertEqual("(True) < (False)", a1bp)
        self.assertEqual("(e['x']) < (e['y'])", a1vp)
        self.assertEqual("((1) < (2)) < ((e['x']) < (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # Multiply expression tests
    # -------------------------------------------------------------------------+

    def test_multiply_eq(self):
        """Check Multiply.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)
        a2n = Multiply(n1, n2)
        a2b = Multiply(bt, bf)
        a2v = Multiply(vx, vy)
        a2e = Multiply(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_multiply_evaluate(self):
        """Check Multiply.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)

        # check the results
        #
        self.assertEqual(Number(1 * 2), a1ne)
        self.assertEqual(Number(True * False), a1be)
        self.assertEqual(Number(5.2 * 3.4), a1ve)
        self.assertEqual(Number((1 * 2) * (5.2 * 3.4)), a1ee)

    def test_multiply_init(self):
        """Check Multiply.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a2n = Multiply(n2, n1)
        a2b = Multiply(bf, bt)
        a2v = Multiply(vy, vx)
        a3 = Multiply(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_multiply_ne(self):
        """Check Multiply.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)
        a2n = Multiply(n1, n2)
        a2b = Multiply(bt, bf)
        a2v = Multiply(vx, vy)
        a2e = Multiply(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_multiply_repr(self):
        """Check Multiply.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 * 2»", repr(a1n))
        self.assertEqual("«true * false»", repr(a1b))
        self.assertEqual("«x * y»", repr(a1v))
        self.assertEqual("«1 * 2 * x * y»", repr(a1e))

    def test_multiply_str(self):
        """Check Multiply.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 * 2", str(a1n))
        self.assertEqual("true * false", str(a1b))
        self.assertEqual("x * y", str(a1v))
        self.assertEqual("1 * 2 * x * y", str(a1e))

    def test_multiply_to_python(self):
        """Check Multiply.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Multiply(n1, n2)
        a1b = Multiply(bt, bf)
        a1v = Multiply(vx, vy)
        a1e = Multiply(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) * (2)", a1np)
        self.assertEqual("(True) * (False)", a1bp)
        self.assertEqual("(e['x']) * (e['y'])", a1vp)
        self.assertEqual("((1) * (2)) * ((e['x']) * (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # Not expression tests
    # -------------------------------------------------------------------------+

    def test_not_eq(self):
        """Check Not.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)
        a2z = Not(n0)
        a21 = Not(n1)
        a2bt = Not(bt)
        a2bf = Not(bf)
        a2vx = Not(vx)
        a2vy = Not(vy)
        a2e = Not(a1vx)

        # Check equality with itself
        #
        self.assertTrue(a1z == a1z)
        self.assertTrue(a11 == a11)
        self.assertTrue(a1bt == a1bt)
        self.assertTrue(a1bf == a1bf)
        self.assertTrue(a1vx == a1vx)
        self.assertTrue(a1vy == a1vy)
        self.assertTrue(a1e == a1e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1z == a2z)
        self.assertTrue(a11 == a21)
        self.assertTrue(a1bt == a2bt)
        self.assertTrue(a1bf == a2bf)
        self.assertTrue(a1vx == a2vx)
        self.assertTrue(a1vy == a2vy)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1z == a1e)
        self.assertFalse(a11 == a1z)
        self.assertFalse(a1bt == a11)
        self.assertFalse(a1bf == a1bt)
        self.assertFalse(a1vx == a1bf)
        self.assertFalse(a1vy == a1vx)
        self.assertFalse(a1e == a1vy)

    def test_not_evaluate(self):
        """Check Not.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ze = a1z.evaluate(env)
        a11e = a11.evaluate(env)
        a1bte = a1bt.evaluate(env)
        a1bfe = a1bf.evaluate(env)
        a1vxe = a1vx.evaluate(env)
        a1vye = a1vy.evaluate(env)
        a1ee = a1e.evaluate(env)

        # check the results
        #
        self.assertEqual(Boolean(not 0), a1ze)
        self.assertEqual(Boolean(not 1), a11e)
        self.assertEqual(Boolean(not True), a1bte)
        self.assertEqual(Boolean(not False), a1bfe)
        self.assertEqual(Boolean(not env['x']), a1vxe)
        self.assertEqual(Boolean(not env['y']), a1vye)
        self.assertEqual(Boolean(not not env['x']), a1ee)

    def test_not_init(self):
        """Check Not.__init__()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)

        # Check the initialization
        #
        self.assertEqual(n0, a1z.value)
        self.assertEqual(n1, a11.value)
        self.assertEqual(bt, a1bt.value)
        self.assertEqual(bf, a1bf.value)
        self.assertEqual(vx, a1vx.value)
        self.assertEqual(vy, a1vy.value)
        self.assertEqual(Not(vx), a1e.value)

    def test_not_ne(self):
        """Check Not.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)
        a2z = Not(n0)
        a21 = Not(n1)
        a2bt = Not(bt)
        a2bf = Not(bf)
        a2vx = Not(vx)
        a2vy = Not(vy)
        a2e = Not(a1vx)

        # Check equality with itself
        #
        self.assertFalse(a1z != a1z)
        self.assertFalse(a11 != a11)
        self.assertFalse(a1bt != a1bt)
        self.assertFalse(a1bf != a1bf)
        self.assertFalse(a1vx != a1vx)
        self.assertFalse(a1vy != a1vy)
        self.assertFalse(a1e != a1e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1z != a2z)
        self.assertFalse(a11 != a21)
        self.assertFalse(a1bt != a2bt)
        self.assertFalse(a1bf != a2bf)
        self.assertFalse(a1vx != a2vx)
        self.assertFalse(a1vy != a2vy)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1z != a1e)
        self.assertTrue(a11 != a1z)
        self.assertTrue(a1bt != a11)
        self.assertTrue(a1bf != a1bt)
        self.assertTrue(a1vx != a1bf)
        self.assertTrue(a1vy != a1vx)
        self.assertTrue(a1e != a1vy)

    def test_not_repr(self):
        """Check Not.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)

        # Check representations
        #
        self.assertEqual("«!0»", repr(a1z))
        self.assertEqual("«!1»", repr(a11))
        self.assertEqual("«!true»", repr(a1bt))
        self.assertEqual("«!false»", repr(a1bf))
        self.assertEqual("«!x»", repr(a1vx))
        self.assertEqual("«!y»", repr(a1vy))
        self.assertEqual("«!!x»", repr(a1e))

    def test_not_str(self):
        """Check Not.__str__()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)

        # Check representations
        #
        self.assertEqual("!0", str(a1z))
        self.assertEqual("!1", str(a11))
        self.assertEqual("!true", str(a1bt))
        self.assertEqual("!false", str(a1bf))
        self.assertEqual("!x", str(a1vx))
        self.assertEqual("!y", str(a1vy))
        self.assertEqual("!!x", str(a1e))

    def test_not_to_python(self):
        """Check Not.to_python()."""
        # Initialize some numbers, bools, values
        #
        n0 = Number(0)
        n1 = Number(1)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1z = Not(n0)
        a11 = Not(n1)
        a1bt = Not(bt)
        a1bf = Not(bf)
        a1vx = Not(vx)
        a1vy = Not(vy)
        a1e = Not(a1vx)

        # Produce python code strings
        #
        a1zp = a1z.to_python(0)
        a11p = a11.to_python(0)
        a1btp = a1bt.to_python(0)
        a1bfp = a1bf.to_python(0)
        a1vxp = a1vx.to_python(0)
        a1vyp = a1vy.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("not (0)", a1zp)
        self.assertEqual("not (1)", a11p)
        self.assertEqual("not (True)", a1btp)
        self.assertEqual("not (False)", a1bfp)
        self.assertEqual("not (e['x'])", a1vxp)
        self.assertEqual("not (e['y'])", a1vyp)
        self.assertEqual("not (not (e['x']))", a1ep)

    # -------------------------------------------------------------------------+
    # Number tests
    # -------------------------------------------------------------------------+

    def test_number_eq(self):
        """Check Number.__eq__()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Another set of numbers of the same value as the previous set
        #
        nzb = Number(0)
        n1b = Number(1)
        nm1b = Number(-1)
        n3b = Number(3.0)
        nm3b = Number(-3.0)
        n127b = Number(12.7)
        nm127b = Number(-12.7)

        # Check equality with itself
        #
        self.assertTrue(nz == nz)
        self.assertTrue(n1 == n1)
        self.assertTrue(nm1 == nm1)
        self.assertTrue(n3 == n3)
        self.assertTrue(nm3 == nm3)
        self.assertTrue(n127 == n127)
        self.assertTrue(nm127 == nm127)

        # Check equality with same value but different objects
        #
        self.assertTrue(nz == nzb)
        self.assertTrue(n1 == n1b)
        self.assertTrue(nm1 == nm1b)
        self.assertTrue(n3 == n3b)
        self.assertTrue(nm3 == nm3b)
        self.assertTrue(n127 == n127b)
        self.assertTrue(nm127 == nm127b)

        # Check equality with different value
        #
        self.assertFalse(nz == nm127)
        self.assertFalse(n1 == nz)
        self.assertFalse(nm1 == n1)
        self.assertFalse(n3 == nm1)
        self.assertFalse(nm3 == n3)
        self.assertFalse(n127 == nm3)
        self.assertFalse(nm127 == n127)

    def test_number_evaluate(self):
        """Check Number.evaluate()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Evaluate the number objects
        #
        env = {}
        nze = nz.evaluate(env)
        n1e = n1.evaluate(env)
        nm1e = nm1.evaluate(env)
        n3e = n3.evaluate(env)
        nm3e = nm3.evaluate(env)
        n127e = n127.evaluate(env)
        nm127e = nm127.evaluate(env)

        # Check the results
        #
        self.assertEqual(nz, nze)
        self.assertEqual(n1, n1e)
        self.assertEqual(nm1, nm1e)
        self.assertEqual(n3, n3e)
        self.assertEqual(nm3, nm3e)
        self.assertEqual(n127, n127e)
        self.assertEqual(nm127, nm127e)

    def test_number_init(self):
        """Check Number.__init__()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Check the initialization
        #
        self.assertEqual(0, nz.value)
        self.assertEqual(1, n1.value)
        self.assertEqual(-1, nm1.value)
        self.assertEqual(3.0, n3.value)
        self.assertEqual(-3.0, nm3.value)
        self.assertEqual(12.7, n127.value)
        self.assertEqual(-12.7, nm127.value)

    def test_number_ne(self):
        """Check Number.__ne__()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Another set of numbers of the same value as the previous set
        #
        nzb = Number(0)
        n1b = Number(1)
        nm1b = Number(-1)
        n3b = Number(3.0)
        nm3b = Number(-3.0)
        n127b = Number(12.7)
        nm127b = Number(-12.7)

        # Check inequality with itself
        #
        self.assertFalse(nz != nz)
        self.assertFalse(n1 != n1)
        self.assertFalse(nm1 != nm1)
        self.assertFalse(n3 != n3)
        self.assertFalse(nm3 != nm3)
        self.assertFalse(n127 != n127)
        self.assertFalse(nm127 != nm127)

        # Check inequality with same value but different objects
        #
        self.assertFalse(nz != nzb)
        self.assertFalse(n1 != n1b)
        self.assertFalse(nm1 != nm1b)
        self.assertFalse(n3 != n3b)
        self.assertFalse(nm3 != nm3b)
        self.assertFalse(n127 != n127b)
        self.assertFalse(nm127 != nm127b)

        # Check inequality with different value
        #
        self.assertTrue(nz != nm127)
        self.assertTrue(n1 != nz)
        self.assertTrue(nm1 != n1)
        self.assertTrue(n3 != nm1)
        self.assertTrue(nm3 != n3)
        self.assertTrue(n127 != nm3)
        self.assertTrue(nm127 != n127)

    def test_number_repr(self):
        """Check Number.__repr__()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Check representations
        #
        self.assertEqual("«0»", repr(nz))
        self.assertEqual("«1»", repr(n1))
        self.assertEqual("«-1»", repr(nm1))
        self.assertEqual("«3.0»", repr(n3))
        self.assertEqual("«-3.0»", repr(nm3))
        self.assertEqual("«12.7»", repr(n127))
        self.assertEqual("«-12.7»", repr(nm127))

    def test_number_str(self):
        """Check Number.__str__()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Check value strings
        #
        self.assertEqual("0", str(nz))
        self.assertEqual("1", str(n1))
        self.assertEqual("-1", str(nm1))
        self.assertEqual("3.0", str(n3))
        self.assertEqual("-3.0", str(nm3))
        self.assertEqual("12.7", str(n127))
        self.assertEqual("-12.7", str(nm127))

    def test_number_to_python(self):
        """Check Number.to_python()."""
        # Some numbers of various value
        #
        nz = Number(0)
        n1 = Number(1)
        nm1 = Number(-1)
        n3 = Number(3.0)
        nm3 = Number(-3.0)
        n127 = Number(12.7)
        nm127 = Number(-12.7)

        # Produce python code strings
        #
        nzp = nz.to_python(0)
        n1p = n1.to_python(0)
        nm1p = nm1.to_python(0)
        n3p = n3.to_python(0)
        nm3p = nm3.to_python(0)
        n127p = n127.to_python(0)
        nm127p = nm127.to_python(0)

        # Check python code strings
        #
        self.assertEqual("0", nzp)
        self.assertEqual("1", n1p)
        self.assertEqual("-1", nm1p)
        self.assertEqual("3.0", n3p)
        self.assertEqual("-3.0", nm3p)
        self.assertEqual("12.7", n127p)
        self.assertEqual("-12.7", nm127p)

    # -------------------------------------------------------------------------+
    # Or expression tests
    # -------------------------------------------------------------------------+

    def test_or_eq(self):
        """Check Or.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)
        a2n = Or(n1, n2)
        a2b = Or(bt, bf)
        a2v = Or(vx, vy)
        a2e = Or(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_or_evaluate(self):
        """Check Or.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)
        a1b2 = Or(bt, bt)
        a1b3 = Or(bf, bf)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)
        a1b2e = a1b2.evaluate(env)
        a1b3e = a1b3.evaluate(env)

        # check the results
        #
        self.assertEqual(Boolean(1 or 2), a1ne)
        self.assertEqual(Boolean(True or False), a1be)
        self.assertEqual(Boolean(5.2 or 3.4), a1ve)
        self.assertEqual(Boolean((1 or 2) or (5.2 or 3.4)), a1ee)
        self.assertEqual(Boolean(True or True), a1b2e)
        self.assertEqual(Boolean(False or False), a1b3e)

    def test_or_init(self):
        """Check Or.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a2n = Or(n2, n1)
        a2b = Or(bf, bt)
        a2v = Or(vy, vx)
        a3 = Or(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_or_ne(self):
        """Check Or.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)
        a2n = Or(n1, n2)
        a2b = Or(bt, bf)
        a2v = Or(vx, vy)
        a2e = Or(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_or_repr(self):
        """Check Or.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 || 2»", repr(a1n))
        self.assertEqual("«true || false»", repr(a1b))
        self.assertEqual("«x || y»", repr(a1v))
        self.assertEqual("«1 || 2 || x || y»", repr(a1e))

    def test_or_str(self):
        """Check Or.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 || 2", str(a1n))
        self.assertEqual("true || false", str(a1b))
        self.assertEqual("x || y", str(a1v))
        self.assertEqual("1 || 2 || x || y", str(a1e))

    def test_or_to_python(self):
        """Check Or.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Or(n1, n2)
        a1b = Or(bt, bf)
        a1v = Or(vx, vy)
        a1e = Or(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) or (2)", a1np)
        self.assertEqual("(True) or (False)", a1bp)
        self.assertEqual("(e['x']) or (e['y'])", a1vp)
        self.assertEqual("((1) or (2)) or ((e['x']) or (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # Subtract expression tests
    # -------------------------------------------------------------------------+

    def test_subtract_eq(self):
        """Check Subtract.__eq__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)
        a2n = Subtract(n1, n2)
        a2b = Subtract(bt, bf)
        a2v = Subtract(vx, vy)
        a2e = Subtract(a1n, a1v)

        # Check equality with itself
        #
        self.assertTrue(a1n == a1n)
        self.assertTrue(a1b == a1b)
        self.assertTrue(a1v == a1v)
        self.assertTrue(a1e == a1e)
        self.assertTrue(a2n == a2n)
        self.assertTrue(a2b == a2b)
        self.assertTrue(a2v == a2v)
        self.assertTrue(a2e == a2e)

        # Check equality with same value but different objects
        #
        self.assertTrue(a1n == a2n)
        self.assertTrue(a1b == a2b)
        self.assertTrue(a1v == a2v)
        self.assertTrue(a1e == a2e)

        # Check equality with different value
        #
        self.assertFalse(a1n == a1e)
        self.assertFalse(a1b == a1n)
        self.assertFalse(a1v == a1b)
        self.assertFalse(a1e == a1v)

    def test_subtract_evaluate(self):
        """Check Subtract.evaluate()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        a1ne = a1n.evaluate(env)
        a1be = a1b.evaluate(env)
        a1ve = a1v.evaluate(env)
        a1ee = a1e.evaluate(env)

        # check the results
        #
        self.assertEqual(Number(1 - 2), a1ne)
        self.assertEqual(Number(True - False), a1be)
        self.assertEqual(Number(5.2 - 3.4), a1ve)
        self.assertEqual(Number((1 - 2) - (5.2 - 3.4)), a1ee)

    def test_subtract_init(self):
        """Check Subtract.__init__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a2n = Subtract(n2, n1)
        a2b = Subtract(bf, bt)
        a2v = Subtract(vy, vx)
        a3 = Subtract(a1n, a2v)

        # Check the initialization
        #
        self.assertEqual(n1, a1n.left)
        self.assertEqual(n2, a1n.right)
        self.assertEqual(bt, a1b.left)
        self.assertEqual(bf, a1b.right)
        self.assertEqual(vx, a1v.left)
        self.assertEqual(vy, a1v.right)
        self.assertEqual(n2, a2n.left)
        self.assertEqual(n1, a2n.right)
        self.assertEqual(bf, a2b.left)
        self.assertEqual(bt, a2b.right)
        self.assertEqual(vy, a2v.left)
        self.assertEqual(vx, a2v.right)
        self.assertEqual(a1n, a3.left)
        self.assertEqual(a2v, a3.right)

    def test_subtract_ne(self):
        """Check Subtract.__ne__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)
        a2n = Subtract(n1, n2)
        a2b = Subtract(bt, bf)
        a2v = Subtract(vx, vy)
        a2e = Subtract(a1n, a1v)

        # Check equality with itself
        #
        self.assertFalse(a1n != a1n)
        self.assertFalse(a1b != a1b)
        self.assertFalse(a1v != a1v)
        self.assertFalse(a1e != a1e)
        self.assertFalse(a2n != a2n)
        self.assertFalse(a2b != a2b)
        self.assertFalse(a2v != a2v)
        self.assertFalse(a2e != a2e)

        # Check equality with same value but different objects
        #
        self.assertFalse(a1n != a2n)
        self.assertFalse(a1b != a2b)
        self.assertFalse(a1v != a2v)
        self.assertFalse(a1e != a2e)

        # Check equality with different value
        #
        self.assertTrue(a1n != a1e)
        self.assertTrue(a1b != a1n)
        self.assertTrue(a1v != a1b)
        self.assertTrue(a1e != a1v)

    def test_subtract_repr(self):
        """Check Subtract.__repr__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)

        # Check representations
        #
        self.assertEqual("«1 - 2»", repr(a1n))
        self.assertEqual("«true - false»", repr(a1b))
        self.assertEqual("«x - y»", repr(a1v))
        self.assertEqual("«1 - 2 - x - y»", repr(a1e))

    def test_subtract_str(self):
        """Check Subtract.__str__()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)

        # Check representations
        #
        self.assertEqual("1 - 2", str(a1n))
        self.assertEqual("true - false", str(a1b))
        self.assertEqual("x - y", str(a1v))
        self.assertEqual("1 - 2 - x - y", str(a1e))

    def test_subtract_to_python(self):
        """Check Subtract.to_python()."""
        # Initialize some numbers, bools, values
        #
        n1 = Number(1)
        n2 = Number(2)
        bt = Boolean(True)
        bf = Boolean(False)
        vx = Variable('x')
        vy = Variable('y')

        # Initialize some expressions
        #
        a1n = Subtract(n1, n2)
        a1b = Subtract(bt, bf)
        a1v = Subtract(vx, vy)
        a1e = Subtract(a1n, a1v)

        # Produce python code strings
        #
        a1np = a1n.to_python(0)
        a1bp = a1b.to_python(0)
        a1vp = a1v.to_python(0)
        a1ep = a1e.to_python(0)

        # Check python code strings
        #
        self.assertEqual("(1) - (2)", a1np)
        self.assertEqual("(True) - (False)", a1bp)
        self.assertEqual("(e['x']) - (e['y'])", a1vp)
        self.assertEqual("((1) - (2)) - ((e['x']) - (e['y']))", a1ep)

    # -------------------------------------------------------------------------+
    # Variable tests
    # -------------------------------------------------------------------------+

    # NOTE: yes, some of the names used in these tests are probably not
    #       going to be legal. However, the simple engine just maps any
    #       string to a variable. It is the parser that enforces language
    #       rules about variable name format.
    #

    def test_variable_eq(self):
        """Check Variable.__eq__()."""
        # Some Variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Another set of numbers of the same value as the previous set
        #
        vxb = Variable('x')
        vab = Variable('abcde')
        vnb = Variable('1two')
        vub = Variable('one_two')
        vcb = Variable('OneTwo')
        vsb = Variable('one two')

        # Check equality with itself
        #
        self.assertTrue(vx == vx)
        self.assertTrue(va == va)
        self.assertTrue(vn == vn)
        self.assertTrue(vu == vu)
        self.assertTrue(vc == vc)
        self.assertTrue(vs == vs)

        # Check equality with same value but different objects
        #
        self.assertTrue(vx == vxb)
        self.assertTrue(va == vab)
        self.assertTrue(vn == vnb)
        self.assertTrue(vu == vub)
        self.assertTrue(vc == vcb)
        self.assertTrue(vs == vsb)

        # Check equality with different value
        #
        self.assertFalse(vx == vs)
        self.assertFalse(va == vx)
        self.assertFalse(vn == va)
        self.assertFalse(vu == vn)
        self.assertFalse(vc == vu)
        self.assertFalse(vs == vc)

    def test_variable_evaluate(self):
        """Check Variable.evaluate()."""
        # Some variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Evaluate the number objects
        #
        env = dict([
            ('x', Boolean(True)),
            ('abcde', Number(2.7)),
            ('1two', Number(-12)),
            ('one_two', Boolean(False)),
            ('OneTwo', Number(10)),
            ('one two', Number(3.0))])
        vxe = vx.evaluate(env)
        vae = va.evaluate(env)
        vne = vn.evaluate(env)
        vue = vu.evaluate(env)
        vce = vc.evaluate(env)
        vse = vs.evaluate(env)

        # Check the results
        #
        self.assertEqual(Boolean(True), vxe)
        self.assertEqual(Number(2.7), vae)
        self.assertEqual(Number(-12), vne)
        self.assertEqual(Boolean(False), vue)
        self.assertEqual(Number(10), vce)
        self.assertEqual(Number(3.0), vse)

    def test_variable_init(self):
        """Check Variable.__init__()."""
        # Some variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Check the initialization
        #
        self.assertEqual('x', vx.name)
        self.assertEqual('abcde', va.name)
        self.assertEqual('1two', vn.name)
        self.assertEqual('one_two', vu.name)
        self.assertEqual('OneTwo', vc.name)
        self.assertEqual('one two', vs.name)

    def test_variable_ne(self):
        """Check Variable.__ne__()."""
        # Some Variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Another set of numbers of the same value as the previous set
        #
        vxb = Variable('x')
        vab = Variable('abcde')
        vnb = Variable('1two')
        vub = Variable('one_two')
        vcb = Variable('OneTwo')
        vsb = Variable('one two')

        # Check inequality with itself
        #
        self.assertFalse(vx != vx)
        self.assertFalse(va != va)
        self.assertFalse(vn != vn)
        self.assertFalse(vu != vu)
        self.assertFalse(vc != vc)
        self.assertFalse(vs != vs)

        # Check inequality with same value but different objects
        #
        self.assertFalse(vx != vxb)
        self.assertFalse(va != vab)
        self.assertFalse(vn != vnb)
        self.assertFalse(vu != vub)
        self.assertFalse(vc != vcb)
        self.assertFalse(vs != vsb)

        # Check inequality with different value
        #
        self.assertTrue(vx != vs)
        self.assertTrue(va != vx)
        self.assertTrue(vn != va)
        self.assertTrue(vu != vn)
        self.assertTrue(vc != vu)
        self.assertTrue(vs != vc)

    def test_variable_repr(self):
        """Check Variable.__repr__()."""
        # Some Variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Check representations
        #
        self.assertEqual("«x»", repr(vx))
        self.assertEqual("«abcde»", repr(va))
        self.assertEqual("«1two»", repr(vn))
        self.assertEqual("«one_two»", repr(vu))
        self.assertEqual("«OneTwo»", repr(vc))
        self.assertEqual("«one two»", repr(vs))

    def test_variable_str(self):
        """Check Variable.__str__()."""
        # Some Variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Check name strings
        #
        self.assertEqual("x", str(vx))
        self.assertEqual("abcde", str(va))
        self.assertEqual("1two", str(vn))
        self.assertEqual("one_two", str(vu))
        self.assertEqual("OneTwo", str(vc))
        self.assertEqual("one two", str(vs))

    def test_variable_to_python(self):
        """Check Variable.to_python()."""
        # Some Variables of various names
        #
        vx = Variable('x')
        va = Variable('abcde')
        vn = Variable('1two')
        vu = Variable('one_two')
        vc = Variable('OneTwo')
        vs = Variable('one two')

        # Produce python code strings
        #
        vxp = vx.to_python(0)
        vap = va.to_python(0)
        vnp = vn.to_python(0)
        vup = vu.to_python(0)
        vcp = vc.to_python(0)
        vsp = vs.to_python(0)

        # Check python code strings
        #
        self.assertEqual("e['x']", vxp)
        self.assertEqual("e['abcde']", vap)
        self.assertEqual("e['1two']", vnp)
        self.assertEqual("e['one_two']", vup)
        self.assertEqual("e['OneTwo']", vcp)
        self.assertEqual("e['one two']", vsp)
