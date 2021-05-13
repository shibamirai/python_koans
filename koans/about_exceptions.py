#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutExceptions(Koan):
    "例外"

    class MySpecialError(RuntimeError):
        pass

    def test_exceptions_inherit_from_exception(self):
        "例外クラスを継承した独自例外"
        mro = self.MySpecialError.mro()
        self.assertEqual(__, mro[1].__name__)
        self.assertEqual(__, mro[2].__name__)
        self.assertEqual(__, mro[3].__name__)
        self.assertEqual(__, mro[4].__name__)

    def test_try_clause(self):
        "try 句"
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'

            ex2 = ex

        self.assertEqual(__, result)

        self.assertEqual(__, isinstance(ex2, Exception))
        self.assertEqual(__, isinstance(ex2, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual(__, ex2.args[0])

    def test_raising_a_specific_error(self):
        "例外を投げる"
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]

        self.assertEqual(__, result)
        self.assertEqual(__, msg)

    def test_else_clause(self):
        "try の else 句"
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual(__, result)


    def test_finally_clause(self):
        "finally 句"
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual(__, result)
