#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Written in place of AboutBlocks in the Ruby Koans
#
# Note: Both blocks and generators use a yield keyword, but they behave
# a lot differently
#

from runner.koan import *

class AboutGenerators(Koan):
    "ジェネレータ"

    def test_generating_values_on_the_fly(self):
        "その場で値を都度生成します"
        result = list()
        bacon_generator = (n + ' bacon' for n in ['crunchy','veggie','danish'])

        for bacon in bacon_generator:
            result.append(bacon)

        self.assertEqual(['crunchy bacon','veggie bacon','danish bacon'], result)

    def test_generators_are_different_to_list_comprehensions(self):
        "ジェネレータはリスト内包表記とは異なります"
        num_list = [x*2 for x in range(1,3)]
        num_generator = (x*2 for x in range(1,3))

        self.assertEqual(2, num_list[0])

        # ジェネレータは繰り返されないと使えません
        # A generator has to be iterated through.
        with self.assertRaises(TypeError): num = num_generator[0]

        self.assertEqual(2, list(num_generator)[0])

        # リスト内包表記とジェネレータはどちらも繰り返しで使うことができます。
        # しかし、ジェネレータが実際に呼ばれるのは繰り返しが始まってからです。
        # 値は保管されるのではなく、その場で作られます
        # Both list comprehensions and generators can be iterated though. However, a generator
        # function is only called on the first iteration. The values are generated on the fly
        # instead of stored.
        # 
        # ジェネレータの方がメモリ使用量が少なくてすみますが、使える場面は限られます
        # Generators are more memory friendly, but less versatile

    def test_generator_expressions_are_a_one_shot_deal(self):
        "ジェネレータ表記は1度しか使えません"
        dynamite = ('Boom!' for n in range(3))

        attempt1 = list(dynamite)
        attempt2 = list(dynamite)

        self.assertEqual(['Boom!', 'Boom!', 'Boom!'], attempt1)
        self.assertEqual([], attempt2)

    # ------------------------------------------------------------------

    def simple_generator_method(self):
        yield 'peanut'
        yield 'butter'
        yield 'and'
        yield 'jelly'

    def test_generator_method_will_yield_values_during_iteration(self):
        "ジェネレータ関数は繰り返しの最中に値を生成します"
        result = list()
        for item in self.simple_generator_method():
            result.append(item)
        self.assertEqual(['peanut', 'butter', 'and', 'jelly'], result)

    def test_generators_can_be_manually_iterated_and_closed(self):
        "ジェネレータ関数は繰り返しと終了を操作できます"
        result = self.simple_generator_method()
        self.assertEqual('peanut', next(result))
        self.assertEqual('butter', next(result))
        result.close()

    # ------------------------------------------------------------------

    def square_me(self, seq):
        for x in seq:
            yield x * x

    def test_generator_method_with_parameter(self):
        "引数を持つジェネレータ関数"
        result = self.square_me(range(2,5))
        self.assertEqual([4, 9, 16], list(result))

    # ------------------------------------------------------------------

    def sum_it(self, seq):
        value = 0
        for num in seq:
            # ローカル変数 'value' は繰り返し中も状態を保持します
            # The local state of 'value' will be retained between iterations
            value += num
            yield value

    def test_generator_keeps_track_of_local_variables(self):
        "ジェネレータはローカル変数の値を保持します"
        result = self.sum_it(range(2,5))
        self.assertEqual([2, 5, 9], list(result))

    # ------------------------------------------------------------------

    def coroutine(self):
        result = yield
        yield result

    def test_generators_can_act_as_coroutines(self):
        "ジェネレータはコルーチンとして使うことが可能です"
        generator = self.coroutine()

        # 考えてみましょう：
        # なぜこの行が必要なのでしょうか
        # THINK ABOUT IT:
        # Why is this line necessary?
        #
        # ヒント：http://www.python.org/dev/peps/pep-0342/ の
        #        "Specification: Sending Values into Generators" を参照してください
        # Hint: Read the "Specification: Sending Values into Generators"
        #       section of http://www.python.org/dev/peps/pep-0342/
        next(generator)

        self.assertEqual(3, generator.send(1 + 2))

    def test_before_sending_a_value_to_a_generator_next_must_be_called(self):
        "send() で値を送る前には、必ず next() を呼ばなければなりません"
        generator = self.coroutine()

        try:
            generator.send(1 + 2)
        except TypeError as ex:
            self.assertRegex(ex.args[0], "can't send non-None value to a just-started generator")

    # ------------------------------------------------------------------

    def yield_tester(self):
        value = yield
        if value:
            yield value
        else:
            yield 'no value'

    def test_generators_can_see_if_they_have_been_called_with_a_value(self):
        "ジェネレータは、値が送信されたかどうかを判別できます"
        generator = self.yield_tester()
        next(generator)
        self.assertEqual('with value', generator.send('with value'))

        generator2 = self.yield_tester()
        next(generator2)
        self.assertEqual('no value', next(generator2))

    def test_send_none_is_equivalent_to_next(self):
        "None を送るのは next を呼ぶのと同じです"
        generator = self.yield_tester()

        next(generator)
        # 'next(generator)' は 'generator.send(None)' と同じです。
        # 'next(generator)' is exactly equivalent to 'generator.send(None)'
        self.assertEqual('no value', generator.send(None))
