# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Module simple.simple_expressions."""


class Add:

    """Represents an addition operation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an Add object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, Add):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} + {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Number value.

        """
        return Number(
            self.left.evaluate(environment).value
            + self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) + ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class And:

    """Represents a logical and expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an And object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, And):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} && {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Boolean value.

        """
        return Boolean(
            bool(self.left.evaluate(environment).value)
            and bool(self.right.evaluate(environment).value))

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) and ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class Boolean:

    """Represents a boolean value expression."""

    def __init__(self, value):
        """Constructor.

        Args:
            value: operand to be interpreted as a boolean value.

        """
        self.value = bool(value)

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be evaluated and the result
                compared with this Boolean object's value.

        Returns:
            True if other_expression equals this boolean value;
            otherwise, False

        """
        if not isinstance(other_expression, Boolean):
            return False
        if self.value != other_expression.value:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be evaluated and the result
                compared with this Boolean object's value.

        Returns:
            True if other_expression does not equal this boolean value;
            otherwise, False

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0}".format(bool(self.value))

    def evaluate(self, environment):
        """Return itself.

        Args:
            environment: a dictionary of variable names (keys) and their
                values. Not used in this class's evaluate() implementation.

        Returns:
            Always returns a Boolean value.

        """
        return self

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "{0}".format(self.value)


class Divide:

    """Represents an divide operation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an Divide object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, Divide):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} / {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Number value.

        """
        return Number(
            self.left.evaluate(environment).value
            / self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) / ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class GreaterThan:

    """Represents a greater than relation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an GreaterThan object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, GreaterThan):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} > {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Boolean value.

        """
        return Boolean(
            self.left.evaluate(environment).value
            > self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) > ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class LessThan:

    """Represents a less than relation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an LessThan object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, LessThan):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} < {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Boolean value.

        """
        return Boolean(
            self.left.evaluate(environment).value
            < self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) < ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class Multiply:

    """Represents a multiplication operation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an Multiply object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, Multiply):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} * {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Number value.

        """
        return Number(
            self.left.evaluate(environment).value
            * self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) * ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class Not:

    """Represents a logical negation expression."""

    def __init__(self, value):
        """Constructor.

        Args:
            value: operand to be interpret as a boolean value and negated.

        """
        self.value = value

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression  to be compared against.

        Returns:
            True if other_expression is also a Not object and has the
            same value as this object.

        """
        if not isinstance(other_expression, Not):
            return False
        if self.left != other_expression.value:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "!{0}".format(self.value)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Boolean value.

        """
        return Boolean(
            not bool(self.value.evaluate(environment).value))

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "!({0})".format(
            self.value.to_python(indentation))


class Number:

    """Represents a numeric value expression."""

    def __init__(self, value):
        """Constructor.

        Args:
            value: operand to be interpreted as a numeric value.

        """
        self.value = value

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be evaluated and the result
                compared with this Number object's value.

        Returns:
            True if other_expression equals this numeric value;
            otherwise, False

        """
        if not isinstance(other_expression, Number):
            return False
        if self.value != other_expression.value:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be evaluated and the result
                compared with this Number object's value.

        Returns:
            True if other_expression does not equal this numeric value;
            otherwise, False

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0}".format(self.value)

    def evaluate(self, environment):
        """Return itself.

        Args:
            environment: a dictionary of variable names (keys) and their
                values. Not used in this class's evaluate() implementation.

        Returns:
            Always returns a Number value.

        """
        return self

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "{0}".format(self.value)


class Or:

    """Represents a logical or expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an Or object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, Or):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} || {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Boolean value.

        """
        return Boolean(
            bool(self.left.evaluate(environment).value)
            or bool(self.right.evaluate(environment).value))

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) or ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class Subtract:

    """Represents a subtraction operation expression."""

    def __init__(self, left, right):
        """Constructor.

        Args:
            left: left hand operand (can be any expression)
            right: right hand operand (can be any expression)

        """
        self.left = left
        self.right = right

    def __eq__(self, other_expression):
        """Equality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is also an Subtract object and has the
            same left and right as this object.

        """
        if not isinstance(other_expression, Subtract):
            return False
        if self.left != other_expression.left:
            return False
        if self.right != other_expression.right:
            return False
        return True

    def __ne__(self, other_expression):
        """Inequality relation.

        Args:
            other_expression: An expression to be compared against.

        Returns:
            True if other_expression is not the same as this object.

        """
        return not self.__eq__(other_expression)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0} - {1}".format(self.left, self.right)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns a Number value.

        """
        return Number(
            self.left.evaluate(environment).value
            - self.right.evaluate(environment).value)

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "({0}) - ({1})".format(
            self.left.to_python(indentation),
            self.right.to_python(indentation))


class Variable:

    """Represents a variable expression."""

    def __init__(self, name):
        """Constructor.

        Args:
            name: the variable name.

        Note that the variable has no value. The value is determined by
        looking up the variable name in an environment (a dictionary).

        """
        self.name = name

    def __eq__(self, other_variable):
        """Equality relation.

        Args:
            other_variable: A variable to be compared against.

        Returns:
            True if other_variable is also a Variable object and has the
            same variable name.

        """
        if not isinstance(other_variable, Variable):
            return False
        if self.name != other_variable.name:
            return False
        return True

    def __ne__(self, other_variable):
        """Inequality relation.

        Args:
        other_variable: A variable to be compared against.

        Returns:
            True if other_variable is not the same as this object.

        """
        return not self.__eq__(other_variable)

    def __repr__(self):
        """A guillemet-delimited string representation of the expression."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the expression."""
        return "{0}".format(self.name)

    def evaluate(self, environment):
        """Produce the value of the variable.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            The Number or Boolean value of the variable.

        """
        return environment[self.name]

    def to_python(self, indentation):
        """Produce the expression translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            expression.

        """
        return "e['{0}']".format(self.name)
