# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Tests for module parsing.parsing_simple."""

import unittest
import os

import parsing.parsing_simple as p
from simple.simple_expressions import Boolean, Number, Variable, Add, \
    Divide, Multiply, Subtract, GreaterThan, LessThan, Not, And, Or
from simple.simple_statements import Assign, If, Sequence, While
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

    # -------------------------------------------------------------------------+
    # parse numeric literals
    # -------------------------------------------------------------------------+

    def test_number_fp_1(self):
        """Test parsing floating point literal value 1.23."""
        ast = parse("1.23", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        n = ast.to_simple()

        self.assertEqual("1.23", c)
        self.assertEqual(Number(1.23), n)

    def test_number_fp_2(self):
        """Test parsing floating point literal value -1.23."""
        ast = parse("-1.23", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        n = ast.to_simple()

        self.assertEqual("-1.23", c)
        self.assertEqual(Number(-1.23), n)

    def test_number_int_1(self):
        """Test parsing integer literal value 123."""
        ast = parse("123", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        n = ast.to_simple()

        self.assertEqual("123", c)
        self.assertEqual(Number(123), n)

    def test_number_int_2(self):
        """Test parsing integer literal value -123."""
        ast = parse("-123", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        n = ast.to_simple()

        self.assertEqual("-123", c)
        self.assertEqual(Number(-123), n)

    # -------------------------------------------------------------------------+
    # parse boolean literals
    # -------------------------------------------------------------------------+

    def test_boolean_t(self):
        """Test parsing boolean literal value true."""
        ast = parse("true", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        b = ast.to_simple()

        self.assertEqual("true", c)
        self.assertEqual(Boolean(True), b)

    def test_boolean_f(self):
        """Test parsing boolean literal value false."""
        ast = parse("false", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        b = ast.to_simple()

        self.assertEqual("false", c)
        self.assertEqual(Boolean(False), b)

    # -------------------------------------------------------------------------+
    # parse variable names
    # -------------------------------------------------------------------------+

    def test_variable_x(self):
        """Test parsing variable x."""
        ast = parse("x", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        v = ast.to_simple()

        self.assertEqual("x", c)
        self.assertEqual(Variable('x'), v)

    def test_variable_xu(self):
        """Test parsing variable x_."""
        ast = parse("x_", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        v = ast.to_simple()

        self.assertEqual("x_", c)
        self.assertEqual(Variable('x_'), v)

    def test_variable_ux(self):
        """Test parsing variable _x."""
        ast = parse("_x", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        v = ast.to_simple()

        self.assertEqual("_x", c)
        self.assertEqual(Variable('_x'), v)

    def test_variable_x_x(self):
        """Test parsing variable x_x."""
        ast = parse("x_x", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        v = ast.to_simple()

        self.assertEqual("x_x", c)
        self.assertEqual(Variable('x_x'), v)

    def test_variable_mixedcase(self):
        """Test parsing variable MixedCase."""
        ast = parse("MixedCase", p.term_expression)
        c = compose(ast, indent="  ", autoblank=False)
        v = ast.to_simple()

        self.assertEqual("MixedCase", c)
        self.assertEqual(Variable('MixedCase'), v)

    def test_variable_keywords(self):
        """Test parsing keywords as variables."""
        with self.assertRaises(SyntaxError):
            parse("if", p.term_expression)
        with self.assertRaises(SyntaxError):
            parse("while", p.term_expression)

    # -------------------------------------------------------------------------+
    # parse addition expression
    # -------------------------------------------------------------------------+

    def test_addition_1525(self):
        """Test parsing addition expression 1.5 + 2.5."""
        ast = parse("1.5 + 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 + 2.5", c)
        self.assertEqual(Add(Number(1.5), Number(2.5)), e)

    def test_addition_m2m1(self):
        """Test parsing addition expression -2 + -1."""
        ast = parse("-2 + -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 + -1", c)
        self.assertEqual(Add(Number(-2), Number(-1)), e)

    def test_addition_x25(self):
        """Test parsing addition expression x + 2.5."""
        ast = parse("x + 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x + 2.5", c)
        self.assertEqual(Add(Variable('x'), Number(2.5)), e)

    def test_addition_15x(self):
        """Test parsing addition expression 1.5 + x."""
        ast = parse("1.5 + x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 + x", c)
        self.assertEqual(Add(Number(1.5), Variable('x')), e)

    def test_addition_xy(self):
        """Test parsing addition expression x + y."""
        ast = parse("x + y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x + y", c)
        self.assertEqual(Add(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse division expression
    # -------------------------------------------------------------------------+

    def test_division_1525(self):
        """Test parsing division expression 1.5 / 2.5."""
        ast = parse("1.5 / 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 / 2.5", c)
        self.assertEqual(Divide(Number(1.5), Number(2.5)), e)

    def test_division_m2m1(self):
        """Test parsing division expression -2 / -1."""
        ast = parse("-2 / -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 / -1", c)
        self.assertEqual(Divide(Number(-2), Number(-1)), e)

    def test_division_x25(self):
        """Test parsing division expression x / 2.5."""
        ast = parse("x / 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x / 2.5", c)
        self.assertEqual(Divide(Variable('x'), Number(2.5)), e)

    def test_division_15x(self):
        """Test parsing division expression 1.5 / x."""
        ast = parse("1.5 / x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 / x", c)
        self.assertEqual(Divide(Number(1.5), Variable('x')), e)

    def test_division_xy(self):
        """Test parsing division expression x / y."""
        ast = parse("x / y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x / y", c)
        self.assertEqual(Divide(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse multiplication expression
    # -------------------------------------------------------------------------+

    def test_multiplication_1525(self):
        """Test parsing multiplication expression 1.5 * 2.5."""
        ast = parse("1.5 * 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 * 2.5", c)
        self.assertEqual(Multiply(Number(1.5), Number(2.5)), e)

    def test_multiplication_m2m1(self):
        """Test parsing multiplication expression -2 * -1."""
        ast = parse("-2 * -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 * -1", c)
        self.assertEqual(Multiply(Number(-2), Number(-1)), e)

    def test_multiplication_x25(self):
        """Test parsing multiplication expression x * 2.5."""
        ast = parse("x * 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x * 2.5", c)
        self.assertEqual(Multiply(Variable('x'), Number(2.5)), e)

    def test_multiplication_15x(self):
        """Test parsing multiplication expression 1.5 * x."""
        ast = parse("1.5 * x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 * x", c)
        self.assertEqual(Multiply(Number(1.5), Variable('x')), e)

    def test_multiplication_xy(self):
        """Test parsing multiplication expression x * y."""
        ast = parse("x * y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x * y", c)
        self.assertEqual(Multiply(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse subtraction expression
    # -------------------------------------------------------------------------+

    def test_subtraction_1525(self):
        """Test parsing subtraction expression 1.5 - 2.5."""
        ast = parse("1.5 - 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 - 2.5", c)
        self.assertEqual(Subtract(Number(1.5), Number(2.5)), e)

    def test_subtraction_2m1m(self):
        """Test parsing subtraction expression -2 - -1."""
        ast = parse("-2 - -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 - -1", c)
        self.assertEqual(Subtract(Number(-2), Number(-1)), e)

    def test_subtraction_x25(self):
        """Test parsing subtraction expression x - 2.5."""
        ast = parse("x - 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x - 2.5", c)
        self.assertEqual(Subtract(Variable('x'), Number(2.5)), e)

    def test_subtraction_15x(self):
        """Test parsing subtraction expression 1.5 - x."""
        ast = parse("1.5 - x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 - x", c)
        self.assertEqual(Subtract(Number(1.5), Variable('x')), e)

    def test_subtraction_xy(self):
        """Test parsing subtraction expression x - y."""
        ast = parse("x - y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x - y", c)
        self.assertEqual(Subtract(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse greater than expression
    # -------------------------------------------------------------------------+

    def test_greaterthan_1525(self):
        """Test parsing greater than expression 1.5 > 2.5."""
        ast = parse("1.5 > 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 > 2.5", c)
        self.assertEqual(GreaterThan(Number(1.5), Number(2.5)), e)

    def test_greaterthan_2m1m(self):
        """Test parsing greater than expression -2 - -1."""
        ast = parse("-2 > -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 > -1", c)
        self.assertEqual(GreaterThan(Number(-2), Number(-1)), e)

    def test_greaterthan_x25(self):
        """Test parsing greater than expression x > 2.5."""
        ast = parse("x > 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x > 2.5", c)
        self.assertEqual(GreaterThan(Variable('x'), Number(2.5)), e)

    def test_greaterthan_15x(self):
        """Test parsing greater than expression 1.5 > x."""
        ast = parse("1.5 > x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 > x", c)
        self.assertEqual(GreaterThan(Number(1.5), Variable('x')), e)

    def test_greaterthan_xy(self):
        """Test parsing greater than expression x > y."""
        ast = parse("x > y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x > y", c)
        self.assertEqual(GreaterThan(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse less than expression
    # -------------------------------------------------------------------------+

    def test_lessthan_1525(self):
        """Test parsing less than expression 1.5 < 2.5."""
        ast = parse("1.5 < 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 < 2.5", c)
        self.assertEqual(LessThan(Number(1.5), Number(2.5)), e)

    def test_lessthan_2m1m(self):
        """Test parsing less than expression -2 - -1."""
        ast = parse("-2 < -1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-2 < -1", c)
        self.assertEqual(LessThan(Number(-2), Number(-1)), e)

    def test_lessthan_x25(self):
        """Test parsing less than expression x < 2.5."""
        ast = parse("x < 2.5", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x < 2.5", c)
        self.assertEqual(LessThan(Variable('x'), Number(2.5)), e)

    def test_lessthan_15x(self):
        """Test parsing less than expression 1.5 < x."""
        ast = parse("1.5 < x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("1.5 < x", c)
        self.assertEqual(LessThan(Number(1.5), Variable('x')), e)

    def test_lessthan_xy(self):
        """Test parsing less than expression x < y."""
        ast = parse("x < y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x < y", c)
        self.assertEqual(LessThan(Variable('x'), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse logical and expression
    # -------------------------------------------------------------------------+

    def test_and_tt(self):
        """Test parsing logical and expression true && true."""
        ast = parse("true && true", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("true && true", c)
        self.assertEqual(And(Boolean(True), Boolean(True)), e)

    def test_and_ft(self):
        """Test parsing logical and expression false && true."""
        ast = parse("false && true", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("false && true", c)
        self.assertEqual(And(Boolean(False), Boolean(True)), e)

    def test_and_xf(self):
        """Test parsing logical and expression x && false."""
        ast = parse("x && false", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x && false", c)
        self.assertEqual(And(Variable('x'), Boolean(False)), e)

    def test_and_1my(self):
        """Test parsing logical and expression -1 && y."""
        ast = parse("-1 && y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-1 && y", c)
        self.assertEqual(And(Number(-1), Variable('y')), e)

    def test_and_xny(self):
        """Test parsing logical and expression x && !y."""
        ast = parse("x && !y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x && !y", c)
        self.assertEqual(And(Variable('x'), Not(Variable('y'))), e)

    def test_and_nxy(self):
        """Test parsing logical and expression !x && y."""
        ast = parse("!x && y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!x && y", c)
        self.assertEqual(And(Not(Variable('x')), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse not expression
    # -------------------------------------------------------------------------+

    def test_not_true(self):
        """Test parsing logical negation expression !true."""
        ast = parse("!true", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!true", c)
        self.assertEqual(Not(Boolean(True)), e)

    def test_not_false(self):
        """Test parsing logical negation expression !false."""
        ast = parse("!false", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!false", c)
        self.assertEqual(Not(Boolean(False)), e)

    def test_not_x(self):
        """Test parsing logical negation expression !x."""
        ast = parse("!x", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!x", c)
        self.assertEqual(Not(Variable('x')), e)

    def test_not_zero(self):
        """Test parsing logical negation expression !0."""
        ast = parse("!0", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!0", c)
        self.assertEqual(Not(Number(0)), e)

    def test_not_one(self):
        """Test parsing logical negation expression !1."""
        ast = parse("!1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!1", c)
        self.assertEqual(Not(Number(1)), e)

    def test_not_1m(self):
        """Test parsing logical negation expression !-1."""
        ast = parse("!-1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!-1", c)
        self.assertEqual(Not(Number(-1)), e)

    def test_not_0p0(self):
        """Test parsing logical negation expression !0.0."""
        ast = parse("!0.0", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!0.0", c)
        self.assertEqual(Not(Number(0.0)), e)

    def test_not_1p1(self):
        """Test parsing logical negation expression !1.1."""
        ast = parse("!1.1", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!1.1", c)
        self.assertEqual(Not(Number(1.1)), e)

    # -------------------------------------------------------------------------+
    # parse logical or expression
    # -------------------------------------------------------------------------+

    def test_or_tt(self):
        """Test parsing logical or expression true || true."""
        ast = parse("true || true", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("true || true", c)
        self.assertEqual(Or(Boolean(True), Boolean(True)), e)

    def test_or_ft(self):
        """Test parsing logical or expression false || true."""
        ast = parse("false || true", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("false || true", c)
        self.assertEqual(Or(Boolean(False), Boolean(True)), e)

    def test_or_xf(self):
        """Test parsing logical or expression x || false."""
        ast = parse("x || false", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x || false", c)
        self.assertEqual(Or(Variable('x'), Boolean(False)), e)

    def test_or_1my(self):
        """Test parsing logical or expression -1 || y."""
        ast = parse("-1 || y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("-1 || y", c)
        self.assertEqual(Or(Number(-1), Variable('y')), e)

    def test_or_xny(self):
        """Test parsing logical or expression x || !y."""
        ast = parse("x || !y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("x || !y", c)
        self.assertEqual(Or(Variable('x'), Not(Variable('y'))), e)

    def test_or_nxy(self):
        """Test parsing logical or expression !x || y."""
        ast = parse("!x || y", p.Expression)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual("!x || y", c)
        self.assertEqual(Or(Not(Variable('x')), Variable('y')), e)

    # -------------------------------------------------------------------------+
    # parse assignment statement
    # -------------------------------------------------------------------------+

    def test_assign_x12(self):
        """Test parsing assignment statement."""
        ast = parse("x = 1 + 2;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = 1 + 2;", c)
        self.assertEqual(Assign('x', Add(Number(1), Number(2))), s)

    def test_assign_xf(self):
        """Test parsing assignment statement."""
        ast = parse("x = false;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = false;", c)
        self.assertEqual(Assign('x', Boolean(False)), s)

    def test_assign_xt(self):
        """Test parsing assignment statement."""
        ast = parse("x = true;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = true;", c)
        self.assertEqual(Assign('x', Boolean(True)), s)

    def test_assign_nx1(self):
        """Test parsing assignment statement."""
        ast = parse("x = !1;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = !1;", c)
        self.assertEqual(Assign('x', Not(Number(1))), s)

    def test_assign_nxt(self):
        """Test parsing assignment statement."""
        ast = parse("x = !true;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = !true;", c)
        self.assertEqual(Assign('x', Not(Boolean(True))), s)

    def test_assign_xyz(self):
        """Test parsing assignment statement."""
        ast = parse("x = y + z;", p.Assign)
        c = compose(ast, indent="  ", autoblank=False)
        s = ast.to_simple()

        self.assertEqual("x = y + z;", c)
        self.assertEqual(Assign('x', Add(Variable('y'), Variable('z'))), s)

    def test_assign_err_123(self):
        """Test parsing assignment statement."""
        with self.assertRaises(SyntaxError):
            parse("1 = 2 + 3;", p.Assign)

    # -------------------------------------------------------------------------+
    # parse if statement
    # -------------------------------------------------------------------------+

    def test_if_tx1x2(self):
        """Test parsing if statement if (true) {x = 1;} else {x = 2;}."""
        expected = "if (true)\n{\n  x = 1;\n}\n"
        expected += "else\n{\n  x = 2;\n}"
        ast = parse(expected, p.If)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual(expected, c)
        self.assertEqual(
            If(
                Boolean(True),
                Assign('x', Number(1)),
                Assign('x', Number(2))),
            e)

    def test_if_tx1yx2y(self):
        """Test parsing if statement if (x > y) {...} else {...}."""
        expected = "if (x > y)\n"
        expected += "{\n"
        expected += "  x = 1;\n"
        expected += "  y = x * 3;\n"
        expected += "}\n"
        expected += "else\n"
        expected += "{\n"
        expected += "  x = 2;\n"
        expected += "  y = 3 * x;\n"
        expected += "}"
        ast = parse(expected, p.If)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual(expected, c)
        self.assertEqual(
            If(
                GreaterThan(Variable('x'), Variable('y')),
                Sequence(
                    Assign('x', Number(1)),
                    Assign('y', Multiply(Variable('x'), Number(3)))),
                Sequence(
                    Assign('x', Number(2)),
                    Assign('y', Multiply(Number(3), Variable('x'))))),
            e)

    # -------------------------------------------------------------------------+
    # parse while statement
    # -------------------------------------------------------------------------+

    def test_while_tx1x2(self):
        """Test parsing while statement while (false) {x = 1;}."""
        expected = "while (false)\n{\n  x = 1;\n}"
        ast = parse(expected, p.While)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual(expected, c)
        self.assertEqual(
            While(
                Boolean(False),
                Assign('x', Number(1))),
            e)

    def test_while_tx1yx2y(self):
        """Test parsing while statement whil (x > y) {...}."""
        expected = "while (x > y)\n"
        expected += "{\n"
        expected += "  x = 1;\n"
        expected += "  y = x * 3;\n"
        expected += "}"
        ast = parse(expected, p.While)
        c = compose(ast, indent="  ", autoblank=False)
        e = ast.to_simple()

        self.assertEqual(expected, c)
        self.assertEqual(
            While(
                GreaterThan(Variable('x'), Variable('y')),
                Sequence(
                    Assign('x', Number(1)),
                    Assign('y', Multiply(Variable('x'), Number(3))))),
            e)

    # -------------------------------------------------------------------------+
    # parse program
    # -------------------------------------------------------------------------+

    def test_program(self):
        """Test simple 3 line program."""
        simple_lines = \
            """
            x = 1 + 1;
            y = x + 3;
            z = y + 5;
            """
        ast = parse(simple_lines, p.Program)
        prog = ast.to_simple()

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
            y = x + 3;
            z = y + 5;
            """
        ast = parse(simple_lines, p.Program)
        prog = ast.to_simple()

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
