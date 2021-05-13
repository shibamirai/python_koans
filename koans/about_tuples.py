#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    "タプル（変更不可リスト）"

    def test_creating_a_tuple(self):
        "タプルの作成"
        count_of_three =  (1, 2, 5)
        self.assertEqual(__, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
        "タプルはイミュータブル（編集不可）"

        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # 補足：assertRegex() は正規表現でパターンマッチングしているので、
        # エラーメッセージ全体をコピーしてくる必要はありません。
        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        self.assertRegex(msg, __)

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        "タプルはイミュータブル（要素の追加も不可）"
        count_of_three =  (1, 2, 5)
        with self.assertRaises(___): count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        "タプルを変更するには、全体を置き換えるしかありません"
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual(__, count_of_three)

    def test_tuples_of_one_look_peculiar(self):
        "要素が１つだけのタプルを作るには？"
        self.assertEqual(__, (1).__class__)
        self.assertEqual(__, (1,).__class__)
        self.assertEqual(__, ("I'm a tuple",).__class__)
        self.assertEqual(__, ("Not a tuple").__class__)

    def test_tuple_constructor_can_be_surprising(self):
        "タプルのコンストラクタは予想外の動きをします"
        self.assertEqual(__, tuple("Surprise!"))

    def test_creating_empty_tuples(self):
        "空のタプルを作る方法"
        self.assertEqual(__ , ())
        self.assertEqual(__ , tuple()) #Sometimes less confusing

    def test_tuples_can_be_embedded(self):
        "タプルは別のタプルに埋め込むことができます"
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(__, place)

    def test_tuples_are_good_for_representing_records(self):
        "タプルを使うとレコードをうまく表現できます"
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual(__, locations[2][0])
        self.assertEqual(__, locations[0][1][2])
