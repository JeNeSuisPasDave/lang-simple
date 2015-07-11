# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Tests for module simple.simple_statements."""

import unittest
import os

from simple.simple_statements import Assign, If, Sequence, While
from simple.simple_expressions import Add, Boolean, GreaterThan, LessThan, \
    Number, Subtract, Variable


class StatementTests(unittest.TestCase):

    """Tests for module simple.simple_statements."""

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
    # Assign statement tests
    # -------------------------------------------------------------------------+

    def test_assign_eq(self):
        """Check Assign.__eq__()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)
        be1 = Assign('a', e1)
        be2 = Assign('b', e2)
        be3 = Assign('c', e3)
        be4 = Assign('d', e4)

        # Check equality with itself
        #
        self.assertTrue(ae1 == ae1)
        self.assertTrue(ae2 == ae2)
        self.assertTrue(ae3 == ae3)
        self.assertTrue(ae4 == ae4)

        # Check equality with same value but different objects
        #
        self.assertTrue(ae1 == be1)
        self.assertTrue(ae2 == be2)
        self.assertTrue(ae3 == be3)
        self.assertTrue(ae4 == be4)

        # Check equality with different value
        #
        self.assertFalse(ae1 == ae2)
        self.assertFalse(ae2 == ae3)
        self.assertFalse(ae3 == ae4)
        self.assertFalse(ae4 == ae1)

    def test_assign_evaluate(self):
        """Check Assign.evaluate()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        ae1e = ae1.evaluate(env)
        ae2e = ae2.evaluate(env)
        ae3e = ae3.evaluate(env)
        ae4e = ae4.evaluate(env)

        # check the results
        #
        self.assertEqual(Number(1 + 2), ae1e['a'])
        self.assertEqual(Number(5.2 + 3.4), ae2e['b'])
        self.assertEqual(Boolean(1 > 2), ae3e['c'])
        self.assertEqual(Boolean(5.2 > 3.4), ae4e['d'])

    def test_assign_init(self):
        """Check Assign.__init__()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)

        # Check the initialization
        #
        self.assertEqual('a', ae1.name)
        self.assertEqual(e1, ae1.expression)
        self.assertEqual('b', ae2.name)
        self.assertEqual(e2, ae2.expression)
        self.assertEqual('c', ae3.name)
        self.assertEqual(e3, ae3.expression)
        self.assertEqual('d', ae4.name)
        self.assertEqual(e4, ae4.expression)

    def test_assign_ne(self):
        """Check Assign.__ne__()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)
        be1 = Assign('a', e1)
        be2 = Assign('b', e2)
        be3 = Assign('c', e3)
        be4 = Assign('d', e4)

        # Check equality with itself
        #
        self.assertFalse(ae1 != ae1)
        self.assertFalse(ae2 != ae2)
        self.assertFalse(ae3 != ae3)
        self.assertFalse(ae4 != ae4)

        # Check equality with same value but different objects
        #
        self.assertFalse(ae1 != be1)
        self.assertFalse(ae2 != be2)
        self.assertFalse(ae3 != be3)
        self.assertFalse(ae4 != be4)

        # Check equality with different value
        #
        self.assertTrue(ae1 != ae2)
        self.assertTrue(ae2 != ae3)
        self.assertTrue(ae3 != ae4)
        self.assertTrue(ae4 != ae1)

    def test_assign_repr(self):
        """Check Assign.__repr__()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)

        # Check representations
        #
        self.assertEqual("«a = 1 + 2;»", repr(ae1))
        self.assertEqual("«b = x + y;»", repr(ae2))
        self.assertEqual("«c = 1 > 2;»", repr(ae3))
        self.assertEqual("«d = x > y;»", repr(ae4))

    def test_assign_str(self):
        """Check Assign.__str__()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)

        # Check value string
        #
        self.assertEqual("a = 1 + 2;", str(ae1))
        self.assertEqual("b = x + y;", str(ae2))
        self.assertEqual("c = 1 > 2;", str(ae3))
        self.assertEqual("d = x > y;", str(ae4))

    def test_assign_to_python(self):
        """Check Assign.to_python()."""
        # Initialize some numbers, bools, variables, expressions
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)

        # Initialize some statements
        #
        ae1 = Assign('a', e1)
        ae2 = Assign('b', e2)
        ae3 = Assign('c', e3)
        ae4 = Assign('d', e4)

        # Produce python code strings
        #
        ae1p = ae1.to_python(0)
        ae2p = ae2.to_python(0)
        ae3p = ae3.to_python(0)
        ae4p = ae4.to_python(0)

        # Check python code strings
        #
        self.assertEqual("e['a'] = (1) + (2)", ae1p)
        self.assertEqual("e['b'] = (e['x']) + (e['y'])", ae2p)
        self.assertEqual("e['c'] = (1) > (2)", ae3p)
        self.assertEqual("e['d'] = (e['x']) > (e['y'])", ae4p)

    # -------------------------------------------------------------------------+
    # If statement tests
    # -------------------------------------------------------------------------+

    def test_if_eq(self):
        """Check If.__eq__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s5, s6)
        sa3 = If(e3, sa1, sa2)
        sa4 = If(e4, sa1, sa2)
        sb1 = If(e3, s1, s2)
        sb2 = If(e4, s5, s6)
        sb3 = If(e3, sb1, sb2)
        sb4 = If(e4, sb1, sb2)

        # Check equality with itself
        #
        self.assertTrue(sa1 == sa1)
        self.assertTrue(sa2 == sa2)
        self.assertTrue(sa3 == sa3)
        self.assertTrue(sa4 == sa4)

        # Check equality with same value but different objects
        #
        self.assertTrue(sa1 == sb1)
        self.assertTrue(sa2 == sb2)
        self.assertTrue(sa3 == sb3)
        self.assertTrue(sa4 == sb4)

        # Check equality with different value
        #
        self.assertFalse(sa1 == sa4)
        self.assertFalse(sa2 == sa1)
        self.assertFalse(sa3 == sa2)
        self.assertFalse(sa4 == sa3)

    def test_if_evaluate(self):
        """Check If.evaluate()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s3, s4)
        sa3 = If(Boolean(True), s5, s6)
        sa4 = If(Boolean(False), s5, s6)
        sa5 = If(e3, s5, s6)
        sa6 = If(e4, sa1, sa2)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        sa1e = sa1.evaluate(env)
        sa2e = sa2.evaluate(env)
        sa3e = sa3.evaluate(env)
        sa4e = sa4.evaluate(env)
        sa5e = sa5.evaluate(env)
        sa6e = sa6.evaluate(env)

        # check the results
        #
        self.assertNotIn('a', sa1e)
        self.assertIn('b', sa1e)
        self.assertEqual(Number(5.2 + 3.4), sa1e['b'])

        self.assertIn('c', sa2e)
        self.assertNotIn('d', sa2e)
        self.assertEqual(Boolean(False), sa2e['c'])

        self.assertIn('a', sa3e)
        self.assertIn('b', sa3e)
        self.assertNotIn('c', sa3e)
        self.assertNotIn('d', sa3e)
        self.assertEqual(Number(1 + 2), sa3e['a'])
        self.assertEqual(Number(5.2 + 3.4), sa3e['b'])

        self.assertNotIn('a', sa4e)
        self.assertNotIn('b', sa4e)
        self.assertIn('c', sa4e)
        self.assertIn('d', sa4e)
        self.assertEqual(Boolean(1 > 2), sa4e['c'])
        self.assertEqual(Boolean(5.2 > 3.4), sa4e['d'])

        self.assertNotIn('a', sa5e)
        self.assertNotIn('b', sa5e)
        self.assertIn('c', sa5e)
        self.assertIn('d', sa5e)
        self.assertEqual(Boolean(1 > 2), sa5e['c'])
        self.assertEqual(Boolean(5.2 > 3.4), sa5e['d'])

        self.assertNotIn('a', sa6e)
        self.assertIn('b', sa6e)
        self.assertNotIn('c', sa6e)
        self.assertNotIn('d', sa6e)
        self.assertEqual(Number(5.2 + 3.4), sa6e['b'])

    def test_if_init(self):
        """Check If.__init__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s3, s4)
        sa3 = If(Boolean(True), s5, s6)
        sa4 = If(Boolean(False), s5, s6)
        sa5 = If(e3, s5, s6)
        sa6 = If(e4, sa1, sa2)

        # Check the initialization
        #
        self.assertEqual(e3, sa1.condition)
        self.assertEqual(s1, sa1.consequence)
        self.assertEqual(s2, sa1.alternative)

        self.assertEqual(e4, sa2.condition)
        self.assertEqual(s3, sa2.consequence)
        self.assertEqual(s4, sa2.alternative)

        self.assertEqual(Boolean(True), sa3.condition)
        self.assertEqual(s5, sa3.consequence)
        self.assertEqual(s6, sa3.alternative)

        self.assertEqual(Boolean(False), sa4.condition)
        self.assertEqual(s5, sa4.consequence)
        self.assertEqual(s6, sa4.alternative)

        self.assertEqual(e3, sa5.condition)
        self.assertEqual(s5, sa5.consequence)
        self.assertEqual(s6, sa5.alternative)

        self.assertEqual(e4, sa6.condition)
        self.assertEqual(sa1, sa6.consequence)
        self.assertEqual(sa2, sa6.alternative)

    def test_if_ne(self):
        """Check If.__ne__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s5, s6)
        sa3 = If(e3, sa1, sa2)
        sa4 = If(e4, sa1, sa2)
        sb1 = If(e3, s1, s2)
        sb2 = If(e4, s5, s6)
        sb3 = If(e3, sb1, sb2)
        sb4 = If(e4, sb1, sb2)

        # Check equality with itself
        #
        self.assertFalse(sa1 != sa1)
        self.assertFalse(sa2 != sa2)
        self.assertFalse(sa3 != sa3)
        self.assertFalse(sa4 != sa4)

        # Check equality with same value but different objects
        #
        self.assertFalse(sa1 != sb1)
        self.assertFalse(sa2 != sb2)
        self.assertFalse(sa3 != sb3)
        self.assertFalse(sa4 != sb4)

        # Check equality with different value
        #
        self.assertTrue(sa1 != sa4)
        self.assertTrue(sa2 != sa1)
        self.assertTrue(sa3 != sa2)
        self.assertTrue(sa4 != sa3)

    def test_if_repr(self):
        """Check If.__repr__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s3, s4)
        sa3 = If(Boolean(True), s5, s6)
        sa4 = If(Boolean(False), s5, s6)
        sa5 = If(e3, s5, s6)
        sa6 = If(e4, sa1, sa2)

        # Check value strings
        #
        self.assertEqual(
            "«if (1 > 2) { a = 1 + 2; } else { b = x + y; }»",
            repr(sa1))
        self.assertEqual(
            "«if (x > y) { c = 1 > 2; } else { d = x > y; }»",
            repr(sa2))
        self.assertEqual(
            "«if (true) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }»",
            repr(sa3))
        self.assertEqual(
            "«if (false) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }»",
            repr(sa4))
        self.assertEqual(
            "«if (1 > 2) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }»",
            repr(sa5))
        self.assertEqual(
            "«if (x > y) { if (1 > 2) { a = 1 + 2; } else { b = x + y; } } "
            + "else { if (x > y) { c = 1 > 2; } else { d = x > y; } }»",
            repr(sa6))

    def test_if_str(self):
        """Check If.__str__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s3, s4)
        sa3 = If(Boolean(True), s5, s6)
        sa4 = If(Boolean(False), s5, s6)
        sa5 = If(e3, s5, s6)
        sa6 = If(e4, sa1, sa2)

        # Check value strings
        #
        self.assertEqual(
            "if (1 > 2) { a = 1 + 2; } else { b = x + y; }",
            str(sa1))
        self.assertEqual(
            "if (x > y) { c = 1 > 2; } else { d = x > y; }",
            str(sa2))
        self.assertEqual(
            "if (true) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }",
            str(sa3))
        self.assertEqual(
            "if (false) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }",
            str(sa4))
        self.assertEqual(
            "if (1 > 2) { a = 1 + 2; b = x + y; } "
            + "else { c = 1 > 2; d = x > y; }",
            str(sa5))
        self.assertEqual(
            "if (x > y) { if (1 > 2) { a = 1 + 2; } else { b = x + y; } } "
            + "else { if (x > y) { c = 1 > 2; } else { d = x > y; } }",
            str(sa6))

    def test_if_to_python(self):
        """Check If.to_python()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)
        s5 = Sequence(s1, s2)
        s6 = Sequence(s3, s4)

        # Initialize some statements
        #
        sa1 = If(e3, s1, s2)
        sa2 = If(e4, s3, s4)
        sa3 = If(Boolean(True), s5, s6)
        sa4 = If(Boolean(False), s5, s6)
        sa5 = If(e3, s5, s6)
        sa6 = If(e4, sa1, sa2)

        # Produce python code strings
        #
        sa1p = sa1.to_python(0)
        sa2p = sa2.to_python(0)
        sa3p = sa3.to_python(0)
        sa4p = sa4.to_python(0)
        sa5p = sa5.to_python(0)
        sa6p = sa6.to_python(0)

        # Check value strings
        #
        self.assertEqual(
            "if (1) > (2):\n    e['a'] = (1) + (2)\n"
            "else:\n    e['b'] = (e['x']) + (e['y'])",
            sa1p)
        self.assertEqual(
            "if (e['x']) > (e['y']):\n    e['c'] = (1) > (2)\n"
            + "else:\n    e['d'] = (e['x']) > (e['y'])",
            sa2p)
        self.assertEqual(
            "if True:\n    e['a'] = (1) + (2)\n"
            + "    e['b'] = (e['x']) + (e['y'])\n"
            + "else:\n    e['c'] = (1) > (2)\n"
            + "    e['d'] = (e['x']) > (e['y'])",
            sa3p)
        self.assertEqual(
            "if False:\n    e['a'] = (1) + (2)\n"
            + "    e['b'] = (e['x']) + (e['y'])\n"
            + "else:\n    e['c'] = (1) > (2)\n"
            + "    e['d'] = (e['x']) > (e['y'])",
            sa4p)
        self.assertEqual(
            "if (1) > (2):\n    e['a'] = (1) + (2)\n"
            + "    e['b'] = (e['x']) + (e['y'])\n"
            + "else:\n    e['c'] = (1) > (2)\n"
            + "    e['d'] = (e['x']) > (e['y'])",
            sa5p)
        self.assertEqual(
            "if (e['x']) > (e['y']):\n"
            + "    if (1) > (2):\n"
            + "        e['a'] = (1) + (2)\n"
            + "    else:\n"
            + "        e['b'] = (e['x']) + (e['y'])\n"
            + "else:\n"
            + "    if (e['x']) > (e['y']):\n"
            + "        e['c'] = (1) > (2)\n"
            + "    else:\n"
            + "        e['d'] = (e['x']) > (e['y'])",
            sa6p)

    # -------------------------------------------------------------------------+
    # Sequence statement tests
    # -------------------------------------------------------------------------+

    def test_sequence_eq(self):
        """Check Sequence.__eq__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)
        sb1 = Sequence(s1, s2)
        sb2 = Sequence(Sequence(s1, s2), s3)
        sb3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Check equality with itself
        #
        self.assertTrue(sa1 == sa1)
        self.assertTrue(sa2 == sa2)
        self.assertTrue(sa3 == sa3)

        # Check equality with same value but different objects
        #
        self.assertTrue(sa1 == sb1)
        self.assertTrue(sa2 == sb2)
        self.assertTrue(sa3 == sb3)

        # Check equality with different value
        #
        self.assertFalse(sa1 == sa3)
        self.assertFalse(sa2 == sa1)
        self.assertFalse(sa3 == sa2)

    def test_sequence_evaluate(self):
        """Check Sequence.evaluate()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Evaluate the add objects
        #
        env = dict([
            ('x', Number(5.2)),
            ('y', Number(3.4))])
        sa1e = sa1.evaluate(env)
        sa2e = sa2.evaluate(env)
        sa3e = sa3.evaluate(env)

        # check the results
        #
        self.assertIn('a', sa1e)
        self.assertIn('b', sa1e)
        self.assertNotIn('c', sa1e)
        self.assertNotIn('d', sa1e)
        self.assertEqual(Number(1 + 2), sa1e['a'])
        self.assertEqual(Number(5.2 + 3.4), sa1e['b'])

        self.assertIn('a', sa2e)
        self.assertIn('b', sa2e)
        self.assertIn('c', sa2e)
        self.assertNotIn('d', sa2e)
        self.assertEqual(Number(1 + 2), sa2e['a'])
        self.assertEqual(Number(5.2 + 3.4), sa2e['b'])
        self.assertEqual(Boolean(1 > 2), sa2e['c'])

        self.assertIn('a', sa3e)
        self.assertIn('b', sa3e)
        self.assertIn('c', sa3e)
        self.assertIn('d', sa3e)
        self.assertEqual(Number(1 + 2), sa3e['a'])
        self.assertEqual(Number(5.2 + 3.4), sa3e['b'])
        self.assertEqual(Boolean(1 > 2), sa3e['c'])
        self.assertEqual(Boolean(5.2 > 3.4), sa3e['d'])

    def test_sequence_init(self):
        """Check Sequence.__init__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Check the initialization
        #
        self.assertEqual(s1, sa1.first)
        self.assertEqual(s2, sa1.second)
        self.assertEqual(s1, sa2.first.first)
        self.assertEqual(s2, sa2.first.second)
        self.assertEqual(s3, sa2.second)
        self.assertEqual(s1, sa3.first.first.first)
        self.assertEqual(s2, sa3.first.first.second)
        self.assertEqual(s3, sa3.first.second)
        self.assertEqual(s4, sa3.second)

    def test_sequence_ne(self):
        """Check Sequence.__ne__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)
        sb1 = Sequence(s1, s2)
        sb2 = Sequence(Sequence(s1, s2), s3)
        sb3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Check inequality with itself
        #
        self.assertFalse(sa1 != sa1)
        self.assertFalse(sa2 != sa2)
        self.assertFalse(sa3 != sa3)

        # Check equality with same value but different objects
        #
        self.assertFalse(sa1 != sb1)
        self.assertFalse(sa2 != sb2)
        self.assertFalse(sa3 != sb3)

        # Check equality with different value
        #
        self.assertTrue(sa1 != sa3)
        self.assertTrue(sa2 != sa1)
        self.assertTrue(sa3 != sa2)

    def test_sequence_repr(self):
        """Check Sequence.__repr__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Check representations
        #
        self.assertEqual("«a = 1 + 2; b = x + y;»", repr(sa1))
        self.assertEqual("«a = 1 + 2; b = x + y; c = 1 > 2;»", repr(sa2))
        self.assertEqual(
            "«a = 1 + 2; b = x + y; c = 1 > 2; d = x > y;»", repr(sa3))

    def test_sequence_str(self):
        """Check Sequence.__str__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Check value strings
        #
        self.assertEqual("a = 1 + 2; b = x + y;", str(sa1))
        self.assertEqual("a = 1 + 2; b = x + y; c = 1 > 2;", str(sa2))
        self.assertEqual(
            "a = 1 + 2; b = x + y; c = 1 > 2; d = x > y;", str(sa3))

    def test_sequence_to_python(self):
        """Check Sequence.to_python()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n2 = Number(2)
        vx = Variable('x')
        vy = Variable('y')
        e1 = Add(n1, n2)
        e2 = Add(vx, vy)
        e3 = GreaterThan(n1, n2)
        e4 = GreaterThan(vx, vy)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('c', e3)
        s4 = Assign('d', e4)

        # Initialize some statements
        #
        sa1 = Sequence(s1, s2)
        sa2 = Sequence(Sequence(s1, s2), s3)
        sa3 = Sequence(Sequence(Sequence(s1, s2), s3), s4)

        # Produce python code strings
        #
        sa1p = sa1.to_python(0)
        sa2p = sa2.to_python(0)
        sa3p = sa3.to_python(0)

        # Check representations
        #
        self.assertEqual(
            "e['a'] = (1) + (2)\ne['b'] = (e['x']) + (e['y'])",
            sa1p)
        self.assertEqual(
            "e['a'] = (1) + (2)\ne['b'] = (e['x']) + (e['y'])\n"
            + "e['c'] = (1) > (2)",
            sa2p)
        self.assertEqual(
            "e['a'] = (1) + (2)\ne['b'] = (e['x']) + (e['y'])\n"
            + "e['c'] = (1) > (2)\ne['d'] = (e['x']) > (e['y'])",
            sa3p)

    # -------------------------------------------------------------------------+
    # While statement tests
    # -------------------------------------------------------------------------+

    def test_while_eq(self):
        """Check While.__eq__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)
        sb1 = While(e4, s4)
        sb2 = While(e5, s5)
        sb3 = While(Boolean(False), s4)

        # Check equality with itself
        #
        self.assertTrue(sa1 == sa1)
        self.assertTrue(sa2 == sa2)
        self.assertTrue(sa3 == sa3)

        # Check equality with same value but different objects
        #
        self.assertTrue(sa1 == sb1)
        self.assertTrue(sa2 == sb2)
        self.assertTrue(sa3 == sb3)

        # Check equality with different value
        #
        self.assertFalse(sa1 == sa3)
        self.assertFalse(sa2 == sa1)
        self.assertFalse(sa3 == sa2)

    def test_while_evaluate(self):
        """Check While.evaluate()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)

        # Evaluate the add objects
        #
        env = dict([
            ('a', Number(0)),
            ('b', Number(0))])
        sa1e = sa1.evaluate(env)
        sa2e = sa2.evaluate(env)
        sa3e = sa3.evaluate(env)

        # check the results
        #
        self.assertIn('a', sa1e)
        self.assertIn('b', sa1e)
        self.assertEqual(Number(3), sa1e['a'])
        self.assertEqual(Number(6), sa1e['b'])

        self.assertIn('a', sa1e)
        self.assertIn('b', sa1e)
        self.assertEqual(Number(-3), sa2e['a'])
        self.assertEqual(Number(-6), sa2e['b'])

        self.assertIn('a', sa1e)
        self.assertIn('b', sa1e)
        self.assertEqual(Number(0), sa3e['a'])
        self.assertEqual(Number(0), sa3e['b'])

    def test_while_init(self):
        """Check While.__init__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)

        # Check the initialization
        #
        self.assertEqual(e4, sa1.condition)
        self.assertEqual(s4, sa1.body)

        self.assertEqual(e5, sa2.condition)
        self.assertEqual(s5, sa2.body)

        self.assertEqual(Boolean(False), sa3.condition)
        self.assertEqual(s4, sa3.body)

    def test_while_ne(self):
        """Check While.__ne__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)
        sb1 = While(e4, s4)
        sb2 = While(e5, s5)
        sb3 = While(Boolean(False), s4)

        # Check equality with itself
        #
        self.assertFalse(sa1 != sa1)
        self.assertFalse(sa2 != sa2)
        self.assertFalse(sa3 != sa3)

        # Check equality with same value but different objects
        #
        self.assertFalse(sa1 != sb1)
        self.assertFalse(sa2 != sb2)
        self.assertFalse(sa3 != sb3)

        # Check equality with different value
        #
        self.assertTrue(sa1 != sa3)
        self.assertTrue(sa2 != sa1)
        self.assertTrue(sa3 != sa2)

    def test_while_repr(self):
        """Check While.__repr__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)

        # Check value strings
        #
        self.assertEqual(
            "«while (a < 3) { a = a + 1; b = b + a; }»",
            repr(sa1))
        self.assertEqual(
            "«while (a > -3) { a = a - 1; b = b + a; }»",
            repr(sa2))
        self.assertEqual(
            "«while (false) { a = a + 1; b = b + a; }»",
            repr(sa3))

    def test_while_str(self):
        """Check While.__str__()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)

        # Check value strings
        #
        self.assertEqual("while (a < 3) { a = a + 1; b = b + a; }", str(sa1))
        self.assertEqual("while (a > -3) { a = a - 1; b = b + a; }", str(sa2))
        self.assertEqual("while (false) { a = a + 1; b = b + a; }", str(sa3))

    def test_while_to_python(self):
        """Check While.to_python()."""
        # Initialize some numbers, bools, variables, expressions,
        # statements
        #
        n1 = Number(1)
        n3 = Number(3)
        n3m = Number(-3)
        va = Variable('a')
        vb = Variable('b')
        e1 = Add(va, n1)
        e2 = Add(vb, va)
        e3 = Subtract(va, n1)
        e4 = LessThan(va, n3)
        e5 = GreaterThan(va, n3m)
        s1 = Assign('a', e1)
        s2 = Assign('b', e2)
        s3 = Assign('a', e3)
        s4 = Sequence(s1, s2)
        s5 = Sequence(s3, s2)

        # Initialize some statements
        #
        sa1 = While(e4, s4)
        sa2 = While(e5, s5)
        sa3 = While(Boolean(False), s4)

        # Produce python code strings
        #
        sa1p = sa1.to_python(0)
        sa2p = sa2.to_python(0)
        sa3p = sa3.to_python(0)

        # Check representations
        #
        self.assertEqual(
            "while (e['a']) < (3):\n"
            + "    e['a'] = (e['a']) + (1)\n"
            + "    e['b'] = (e['b']) + (e['a'])",
            sa1p)
        self.assertEqual(
            "while (e['a']) > (-3):\n"
            + "    e['a'] = (e['a']) - (1)\n"
            + "    e['b'] = (e['b']) + (e['a'])",
            sa2p)
        self.assertEqual(
            "while False:\n"
            + "    e['a'] = (e['a']) + (1)\n"
            + "    e['b'] = (e['b']) + (e['a'])",
            sa3p)
