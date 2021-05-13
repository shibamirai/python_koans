#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# グリードは、最大で5つまでのサイコロを振って得点を競うゲームです。
# 下記の score 関数は、サイコロ一振りの得点を計算します。
# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used to calculate the
# score of a single roll of the dice.
#
# グリードは以下のように得点が決まります。
# A greed roll is scored as follows:
#
# * 1の目が3つ揃うと1000点です。
# * A set of three ones is 1000 points
#
# * 1以外の目が3つ揃うと、出た目の100倍の得点です。(例：5の目が3つで500点)
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * 3つの組以外の1の目は1個につき100点です。
# * A one (that is not part of a set of three) is worth 100 points.
#
# * 3つの組以外の5の目は1個につき50点です。
# * A five (that is not part of a set of three) is worth 50 points.
#
# * 上記以外は0点です。
# * Everything else is worth 0 points.
#
#
# 例：
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# 他の例は下記のテストコードにあります。
# More scoring examples are given in the tests below:
#
# この score 関数を完成させてください。
# Your goal is to write the score method.

def score(dice):
    # この関数の処理を書いてください
    # You need to write this method
    pass

class AboutScoringProject(Koan):
    "得点プロジェクト"

    def test_score_of_an_empty_list_is_zero(self):
        "空のリストは0点です"
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        "5の目が1つで50点です"
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        "1の目が1つで100点です"
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        "1のゾロ目と5のゾロ目はそれぞれの得点の合計です"
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        "2, 3, 4, 6の目は1つだけでは0点です"
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        "1の目が3つで1000点です"
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        "1以外の目が3つで、その目の100倍の得点です"
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        "得点はそれらの合計です"
        self.assertEqual(250, score([2,5,2,2,3]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        "1つだけの得点も忘れずに"
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))
