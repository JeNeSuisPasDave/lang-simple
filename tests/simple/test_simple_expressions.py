# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

"""Tests for module simple.simple_expressions."""

import unittest
import os

from simple.simple_expressions import Boolean


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
    # Boolean tests
    # -------------------------------------------------------------------------+

    def test_boolean_eq(self):
        """Check Boolean.__eq__()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        b2t = Boolean(True)
        b2f = Boolean(False)

        self.assertTrue(b1t == b2t)
        self.assertTrue(b1f == b2f)
        self.assertFalse(b1t == b2f)
        self.assertFalse(b1f == b2t)

    def test_boolean_evaluate(self):
        """Check Boolean.evaluate()."""
        env = {}
        b1t = Boolean(True)
        b1f = Boolean(False)
        b1te = b1t.evaluate(env)
        b1fe = b1f.evaluate(env)

        self.assertEqual(b1t, b1te)
        self.assertEqual(b1f, b1fe)

    def test_boolean_init(self):
        """Check Boolean.__init__()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        self.assertTrue(b1t.value)
        self.assertFalse(b1f.value)

    def test_boolean_ne(self):
        """Check Boolean.__ne__()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        b2t = Boolean(True)
        b2f = Boolean(False)

        self.assertFalse(b1t != b2t)
        self.assertFalse(b1f != b2f)
        self.assertTrue(b1t != b2f)
        self.assertTrue(b1f != b2t)

    def test_boolean_repr(self):
        """Check Boolean.__repr__()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        self.assertEqual("«True»", repr(b1t))
        self.assertEqual("«False»", repr(b1f))

    def test_boolean_str(self):
        """Check Boolean.__str__()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        self.assertEqual("True", str(b1t))
        self.assertEqual("False", str(b1f))

    def test_boolean_to_python(self):
        """Check Boolean.to_python()."""
        b1t = Boolean(True)
        b1f = Boolean(False)
        b1tp = b1t.to_python(0)
        b1fp = b1f.to_python(0)

        self.assertEqual("True", b1tp)
        self.assertEqual("False", b1fp)
