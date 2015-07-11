# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Tests for module parsing.parsing_simple."""

import unittest
import os

import parsing.parsing_simple as p
from simple.simple_expressions import Boolean, Number, Variable, Add, \
    Multiply
from simple.simple_statements import Assign
from pypeg2 import parse, compose


class ParsingSimpleTests(unittest.TestCase):

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

    def test_fp_number(self):
        """Test parsing floating point literal value."""
        f = parse("1.23", p.term_expression)
        c = compose(f)
        n = f.to_simple()

        self.assertEqual("1.23", c)
        self.assertEqual(Number(1.23), n)

    def test_boolean(self):
        """Test parsing boolean literal value."""
        f = parse("true", p.term_expression)
        c = compose(f)
        b = f.to_simple()

        self.assertEqual("true", c)
        self.assertEqual(Boolean(True), b)

    def test_variable(self):
        """Test parsing variable."""
        f = parse("x", p.term_expression)
        c = compose(f)
        v = f.to_simple()

        self.assertEqual("x", c)
        self.assertEqual(Variable('x'), v)

    def test_addition(self):
        """Test parsing addition expression."""
        f = parse("x + 2", p.Expression)
        c = compose(f)
        e = f.to_simple()

        self.assertEqual("x + 2", c)
        self.assertEqual(Add(Variable('x'), Number(2)), e)

    def test_multiplication(self):
        """Test parsing multiplication expression."""
        f = parse("x * 2", p.Expression)
        c = compose(f)
        e = f.to_simple()

        self.assertEqual("x * 2", c)
        self.assertEqual(Multiply(Variable('x'), Number(2)), e)

    def test_assign(self):
        """Test parsing assignment statement."""
        f = parse("x = 1 + 2", p.Assign)
        c = compose(f)
        a = f.to_simple()

        self.assertEqual("x = 1 + 2", c)
        self.assertEqual(Assign('x', Add(Number(1), Number(2))), a)

    def test_program(self):
        """Test simple 3 line program."""
        simple_lines = \
            """
            x = 1 + 1
            y = x + 3
            z = y + 5
            """
        f = parse(simple_lines, p.Program)
        prog = f.to_simple()

        env_expected = dict(x=Number(2), y=Number(5), z=Number(10))
        env = {}
        env2 = prog.evaluate(env)
        self.assertEqual(len(env_expected), len(env2))
        for x in env_expected.keys():
            self.assertEqual(env_expected[x], env2[x])

        # show that we can reuse the program

        env3 = prog.evaluate(env2)
        self.assertEqual(len(env_expected), len(env3))
        for x in env_expected.keys():
            self.assertEqual(env_expected[x], env3[x])

    def test_program_diff_env(self):
        """Test simple 2 line program with different initial conditions."""
        simple_lines = \
            """
            y = x + 3
            z = y + 5
            """
        f = parse(simple_lines, p.Program)
        prog = f.to_simple()

        env_expected = dict(x=Number(2), y=Number(5), z=Number(10))
        env = dict(x=Number(2))
        env2 = prog.evaluate(env)
        self.assertEqual(len(env_expected), len(env2))
        for x in env_expected.keys():
            self.assertEqual(env_expected[x], env2[x])

        # show that we can reuse the program

        env_expected = dict(x=Number(9), y=Number(12), z=Number(17))
        env2['x'] = Number(9)
        env3 = prog.evaluate(env2)
        self.assertEqual(len(env_expected), len(env3))
        for x in env_expected.keys():
            self.assertEqual(env_expected[x], env3[x])
