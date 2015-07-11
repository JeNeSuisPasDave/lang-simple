# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Module parsing.parsing_simple."""

from re import compile as regex
from pypeg2 import Enum, Keyword, K, Literal, List, Symbol, some
import simple.simple_expressions as s_e
import simple.simple_statements as s_s


class Add(List):

    """Matches and addition expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " + {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Add(self[0].to_simple(), self[1].to_simple())


class And(List):

    """Matches a logical and expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " && {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.And(self[0].to_simple(), self[1].to_simple())


class Assign(List):

    """Matches an assignment statement."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return "{0}{1} = {2};".format(
            p.indent * p.indention_level,
            p.compose(self[0], **x), p.compose(self[1], **x))

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_s.Assign(self[0].to_simple().name, self[1].to_simple())


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
            ss.append("{0}".format((p.compose(s, **x))))
        return "\n".join(ss)

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        if 1 == len(self):
            return self[0].to_simple()
        else:
            return self._to_simple_subblock(self[:])


class Boolean(Literal):

    """Matches a boolean value token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        if "true" == self.value:
            return s_e.Boolean(True)
        else:
            return s_e.Boolean(False)


class Divide(List):

    """Matches a division expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " / {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Divide(self[0].to_simple(), self[1].to_simple())


class Expression(List):

    """Matches any expression, including booleans, variables, numbers."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return p.compose(self[0], **x)

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return self[0].to_simple()


class GreaterThan(List):

    """Matches a greater than expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " > {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.GreaterThan(self[0].to_simple(), self[1].to_simple())


class If(List):

    """Matches an if statement."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}if ({1})\n{0}{{\n".format(
            p.indent * p.indention_level,
            p.compose(self[0], **x))
        p.indention_level += 1
        s += "{0}\n".format(
            p.compose(self[1], **x))
        p.indention_level -= 1
        s += "{0}}}\n{0}else\n{0}{{\n".format(p.indent * p.indention_level)
        p.indention_level += 1
        s += "{0}\n".format(
            p.compose(self[2], **x))
        p.indention_level -= 1
        s += "{0}}}".format(p.indent * p.indention_level)
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_s.If(
            self[0].to_simple(), self[1].to_simple(), self[2].to_simple())


class LessThan(List):

    """Matches a less than expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " < {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.LessThan(self[0].to_simple(), self[1].to_simple())


class Multiply(List):

    """Matches a multiplication expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " * {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Multiply(self[0].to_simple(), self[1].to_simple())


class Not(List):

    """Matches a logical not expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "!{0}".format(p.compose(self[0], **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Not(self[0].to_simple())


class Number(Literal):

    """Matches a number value token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        s = self.value
        if 0 <= s.find('.'):
            return s_e.Number(float(self.value))
        else:
            return s_e.Number(int(self.value))


class Or(List):

    """Matches a logical or expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " || {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Or(self[0].to_simple(), self[1].to_simple())


class Program(List):

    """Matches a full program."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        return p.compose(self[0], **x)

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return self[0].to_simple()


class Subtract(List):

    """Matches a subtraction expression."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}".format(p.compose(self[0], **x))
        for part in self[1:]:
            s += " - {0}".format(p.compose(part, **x))
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Subtract(self[0].to_simple(), self[1].to_simple())


class Variable(str):

    """Matches a variable name token."""

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_e.Variable(self)


class While(List):

    """Matches a while statement."""

    def compose(self, p, **x):
        """Produce the equivalent simple language as matched.

        Might have different whitespace and be otherwise formatted
        in a normalized fashion.

        """
        s = "{0}while ({1})\n{0}{{\n".format(
            p.indent * p.indention_level,
            p.compose(self[0], **x))
        p.indention_level += 1
        s += "{0}\n".format(
            p.compose(self[1], **x))
        p.indention_level -= 1
        s += "{0}}}".format(p.indent * p.indention_level)
        return s

    def to_simple(self):
        """Generate corresponding simple object that can be evaluated."""
        return s_s.While(
            self[0].to_simple(), self[1].to_simple())


identifier = regex(r"[a-zA-Z_][0-9a-zA-Z_]*")
Symbol.regex = identifier

Keyword.grammar = Enum(
    K("else"),
    K("if"),
    K("while")
    )
Symbol.check_keywords = True

Number.grammar = regex(r"(\+|\-)?[0-9]+(\.[0-9]+)?")
Boolean.grammar = regex(r"(true|false)")
Variable.grammar = Symbol

term_expression = [Number, Boolean, Variable]

Not.grammar = "!", term_expression

unary_term_expression = [Not, term_expression]

multiplicative_expression = [Multiply, Divide, unary_term_expression]

Multiply.grammar = term_expression, "*", multiplicative_expression
Divide.grammar = term_expression, "/", multiplicative_expression

additive_expression = [Add, Subtract, multiplicative_expression]

Add.grammar = multiplicative_expression, "+", additive_expression
Subtract.grammar = multiplicative_expression, "-", additive_expression

conditional_expression = [GreaterThan, LessThan, additive_expression]

GreaterThan.grammar = additive_expression, ">", conditional_expression
LessThan.grammar = additive_expression, "<", conditional_expression

logical_expression = [And, Or, conditional_expression]

And.grammar = conditional_expression, "&&", logical_expression
Or.grammar = conditional_expression, "||", logical_expression

Expression.grammar = logical_expression

Assign.grammar = Variable, "=", Expression, ";"

statement = [Assign, If, While]

If.grammar = K("if"), "(", logical_expression, ")", "{", Block, "}", \
    K("else"), "{", Block, "}"

While.grammar = K("while"), "(", logical_expression, ")", "{", Block, "}"

Block.grammar = some(statement)

Program.grammar = Block
