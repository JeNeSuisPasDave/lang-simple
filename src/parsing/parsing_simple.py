# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Module parsing.parsing_simple."""

from re import compile as regex
from pypeg2 import Literal, List, Symbol, compose, some
import simple.simple_expressions as s_e
import simple.simple_statements as s_s


class Number(Literal):

    """Matches a number value token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        s = self.value
        if 0 <= s.find('.'):
            return s_e.Number(float(self.value))
        else:
            return s_e.Number(int(self.value))


class Boolean(Literal):

    """Matches a boolean value token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        if "true" == self.value:
            return s_e.Boolean(True)
        else:
            return s_e.Boolean(False)


class Variable(str):

    """Matches a variable name token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Variable(self)


class Multiply(List):

    """Matches a multiplication expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(compose(self[0]))
        for x in self[1:]:
            s += " * {0}".format(compose(x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Multiply(self[0].to_simple(), self[1].to_simple())


class Divide(List):

    """Matches a division expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(compose(self[0]))
        for x in self[1:]:
            s += " / {0}".format(compose(x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Divide(self[0].to_simple(), self[1].to_simple())


class Add(List):

    """Matches and addition expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(compose(self[0]))
        for x in self[1:]:
            s += " + {0}".format(compose(x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Add(self[0].to_simple(), self[1].to_simple())


class Subtract(List):

    """Matches a subtraction expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(compose(self[0]))
        for x in self[1:]:
            s += " - {0}".format(compose(x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Subtract(self[0].to_simple(), self[1].to_simple())


class Expression(List):

    """Matches any expression, including booleans, variables, numbers."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return compose(self[0])

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return self[0].to_simple()


class Assign(List):

    """Matches an assignment statement."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return "{0} = {1}".format(compose(self[0]), compose(self[1]))

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_s.Assign(self[0], self[1].to_simple())


class Block(List):

    """Matches a block of statements."""

    def _to_simple_subblock(self, remaining):
        """Nest additional statements within Sequence objects.

        This is a helper method for to_simple(). Required because
        the simple Sequence object only holds two statements. We
        take advantage of the fact that one or both of those
        statements can also be a Sequence object. By nesting
        Sequence objects, we can represent a block of arbitrary
        length.

        """
        if 2 < len(remaining):
            return s_s.Sequence(
                remaining[0].to_simple(),
                self._to_simple_subblock(remaining[1:]))
        else:
            return s_s.Sequence(
                remaining[0].to_simple(),
                remaining[1].to_simple())

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        ss = []
        for s in self:
            ss.append("{0}".format((compose(s))))
        return "\n".join(ss)

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        if 1 == len(self):
            return s_s.Sequence(s_s.DoNothing(), self[0].to_simple())
        else:
            return self._to_simple_subblock(self[:])


class Program(List):

    """Matches a full program."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return compose(self[0])

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return self[0].to_simple()


Number.grammar = regex(r"(\+|\-)?[0-9]+(\.[0-9]+)?")
Boolean.grammar = regex(r"(true|false)")
Variable.grammar = Symbol

term_expression = [Number, Boolean, Variable]
multiplicative_expression = [Multiply, Divide, term_expression]

Multiply.grammar = term_expression, "*", multiplicative_expression
Divide.grammar = term_expression, "/", multiplicative_expression

additive_expression = [Add, Subtract, multiplicative_expression]

Add.grammar = multiplicative_expression, "+", additive_expression
Subtract.grammar = multiplicative_expression, "-", additive_expression
Expression.grammar = additive_expression

Assign.grammar = Variable, "=", Expression

statement = [Assign]
Block.grammar = some(statement)
Program.grammar = Block
