# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Module simple.simple_expressions."""

from .simple_expressions import Boolean


class Assign:

    """Represents an assignment statement."""

    def __init__(self, name, expression):
        """Constructor.

        Args:
            name: variable name of the variable on the left hand side of
                the assignment.
            expression: right hand side of the assignment.

        """
        self.name = name
        self.expression = expression

    def __eq__(self, other_statement):
        """Equality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is also an Assign object and has the
            same variable name and expression as this object.

        """
        if not isinstance(other_statement, Assign):
            return False
        if self.name != other_statement.name:
            return False
        if self.expression != other_statement.expression:
            return False
        return True

    def __ne__(self, other_statement):
        """Inequality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is not the same as this object.

        """
        return not self.__eq__(other_statement)

    def __repr__(self):
        """A guillemet-delimited string representation of the statement."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the statement."""
        return "{0} = {1}".format(self.name, self.expression)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Always returns an environment, updated to reflect the evaluation
            of the statement.

        """
        new_environment = environment.copy()
        new_environment.update(
            dict([(self.name, self.expression.evaluate(environment))]))
        return new_environment

    def to_python(self, indentation):
        """Produce the statement translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            statement.

        """
        return "{0}e['{1}'] = {2}".format(
            "    " * indentation,
            self.name, self.expression.to_python(indentation))


class DoNothing:

    """Represents an null statement."""

    def __eq__(self, other_statement):
        """Equality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is also an DoNothing object.

        """
        return isinstance(other_statement, DoNothing)

    def __ne__(self, other_statement):
        """Inequality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is not the same as this object.

        """
        return not self.__eq__(other_statement)

    def __repr__(self):
        """A guillemet-delimited string representation of the statement."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the statement."""
        return "do-nothing"

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Returns the environment, unmodified.

        """
        return environment

    def to_python(self, indentation):
        """Produce the statement translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            statement.

        """
        return "{0}pass".format("    " * indentation)


class If:

    """Represents an if statement."""

    def __init__(self, condition, consequence, alternative):
        """Constructor.

        Args:
            condition: the expression to be evaluated for truth.
            consequence: the statement to be evaluated if the condition
                is true.
            alternative: the statement to be evaluated if the condition
                is false.

        """
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __eq__(self, other_statement):
        """Equality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is also an If object and has the
            same condition, consequence, and alternativeas as this object.

        """
        if not isinstance(other_statement, If):
            return False
        if self.condition != other_statement.condition:
            return False
        if self.consequence != other_statement.consequence:
            return False
        if self.alternative != other_statement.alternative:
            return False
        return True

    def __ne__(self, other_statement):
        """Inequality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is not the same as this object.

        """
        return not self.__eq__(other_statement)

    def __repr__(self):
        """A guillemet-delimited string representation of the statement."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the statement."""
        return "if ({0}) {{ {1} }} else {{ {2} }}".format(
            self.condition, self.consequence, self.alternative)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            If the condition is true, returns the environment from
            the evaluated consequence; otherwise, returns the environment
            from the evaluated alternative.

        """
        c = self.condition.evaluate(environment)
        if c == Boolean(True):
            return self.consequence.evaluate(environment)
        else:
            return self.alternative.evaluate(environment)

    def to_python(self, indentation):
        """Produce the statement translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            statement.

        """
        return "{0}if {1}:\n{2}\nelse:\n{3}".format(
            "    " * indentation,
            self.condition.to_python(indentation),
            self.consequence.to_python(indentation + 1),
            self.alternative.to_python(indentation + 1))


class Sequence:

    """Represents a sequence of two statements."""

    def __init__(self, first, second):
        """Constructor.

        Args:
            first: the first statement to be evaluated.
            second: the second statement to be evaluated.

        """
        self.first = first
        self.second = second

    def __eq__(self, other_statement):
        """Equality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is also an If object and has the
            same first and second statements as this object.

        """
        if not isinstance(other_statement, Assign):
            return False
        if self.first != other_statement.first:
            return False
        if self.second != other_statement.second:
            return False
        return True

    def __ne__(self, other_statement):
        """Inequality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is not the same as this object.

        """
        return not self.__eq__(other_statement)

    def __repr__(self):
        """A guillemet-delimited string representation of the statement."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the statement."""
        return "{0}; {1}".format(self.first, self.second)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Returns the environment produced by evaluated the first statement
            and then the second statement.

        """
        return self.second.evaluate(self.first.evaluate(environment))

    def to_python(self, indentation):
        """Produce the statement translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            statement.

        """
        return "{0}\n{1}".format(
            self.first.to_python(indentation),
            self.second.to_python(indentation))


class While:

    """Represents a while statement."""

    def __init__(self, condition, body):
        """Constructor.

        Args:
            condition: the expression to be evaluated for truth before
                each potential execution of the body.
            body: the statement to be evaluated if the condition
                is true.

        """
        self.condition = condition
        self.body = body

    def __eq__(self, other_statement):
        """Equality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is also an If object and has the
            same condition and body as this object.

        """
        if not isinstance(other_statement, Assign):
            return False
        if self.condition != other_statement.condition:
            return False
        if self.body != other_statement.body:
            return False
        return True

    def __ne__(self, other_statement):
        """Inequality relation.

        Args:
            other_statement: A statement to be compared against.

        Returns:
            True if other_statement is not the same as this object.

        """
        return not self.__eq__(other_statement)

    def __repr__(self):
        """A guillemet-delimited string representation of the statement."""
        return "«{0}»".format(self)

    def __str__(self):
        """A string representation of the statement."""
        return "while ({0}) {{ {1} }}".format(self.condition, self.body)

    def evaluate(self, environment):
        """Execute the expression in the context of the environment.

        Args:
            environment: a dictionary of variable names (keys) and their
                values.

        Returns:
            Returns the environment produced by repeated evaluations
            of the body statement.

        """
        c = self.condition.evaluate(environment)
        if c == Boolean(True):
            return self.evaluate(self.body.evaluate(environment))
        else:
            return environment

    def to_python(self, indentation):
        """Produce the statement translated to Python.

        Args:
            indentation: The current indentation level (in count of
                4-character chunks).

        Returns:
            A string containing Python code representing the
            statement.

        """
        return "{0}while {1}:\n{2}".format(
            "    " * indentation,
            self.condition.to_python(indentation),
            self.body.to_python(indentation + 1))
