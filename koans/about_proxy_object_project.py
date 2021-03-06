#!/usr/bin/env python
# -*- coding: utf-8 -*-

# プロジェクト：プロキシクラスの作成
# Project: Create a Proxy Class
#
# この課題は、プロキシクラスを作成します（以下から開始します）
# 任意のオブジェクトでプロキシオプジェクトを初期化できるようにしてください。
# プロキシオプジェクトに対する属性の呼び出しは、すべて元のオブジェクトに送ってください。
# プロキシは、属性が呼び出される度に、その属性名を記録してください。
# In this assignment, create a proxy class (one is started for you
# below).  You should be able to initialize the proxy object with any
# object.  Any attributes called on the proxy object should be forwarded
# to the target object.  As each attribute call is sent, the proxy should
# record the name of the attribute sent.
#
# プロキシクラスのひな形が用意してあります。ここに、メソッドや足りないハンドラ、
# その他必要なメソッドを追加してください。プロキシクラスの仕様は
# AboutProxyObjectProject に示されています。
# The proxy class is started for you.  You will need to add a method
# missing handler and any other supporting methods.  The specification
# of the Proxy class is given in the AboutProxyObjectProject koan.

# 注釈：この課題は少しトリッキーですが、あなたならきっと出来ます！
# Note: This is a bit trickier than its Ruby Koans counterpart, but you
# can do it!

from runner.koan import *

class Proxy:
    def __init__(self, target_object):
        # ここにコードを書いてください WRITE CODE HERE

        # '_obj' の初期化は最後です。信じてください！
        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object

    # ここにコードを書いてください WRITE CODE HERE

# プロキシオブジェクトは下記の koan にパスしなければなりません。
# The proxy object should pass the following Koan:
#
class AboutProxyObjectProject(Koan):
    "プロキシオブジェクトプロジェクト"
    def test_proxy_method_returns_wrapped_object(self):
        "Proxy メソッドはラップしたオブジェクトを返します"
        # 注意：Television クラスは下で定義してあります
        # NOTE: The Television class is defined below
        tv = Proxy(Television())

        self.assertTrue(isinstance(tv, Proxy))

    def test_tv_methods_still_perform_their_function(self):
        "tv のメソッドは元のオブジェクトと同じように使えます"
        tv = Proxy(Television())

        tv.channel = 10
        tv.power()

        self.assertEqual(10, tv.channel)
        self.assertTrue(tv.is_on())

    def test_proxy_records_messages_sent_to_tv(self):
        "プロキシは tv へのメッセージを記録します"
        tv = Proxy(Television())

        tv.power()
        tv.channel = 10

        self.assertEqual(['power', 'channel'], tv.messages())

    def test_proxy_handles_invalid_messages(self):
        "プロキシは不正なメッセージに対して例外を出します"
        tv = Proxy(Television())

        with self.assertRaises(AttributeError):
            tv.no_such_method()


    def test_proxy_reports_methods_have_been_called(self):
        "プロキシは呼ばれたことがあるメソッドを報告します"
        tv = Proxy(Television())

        tv.power()
        tv.power()

        self.assertTrue(tv.was_called('power'))
        self.assertFalse(tv.was_called('channel'))

    def test_proxy_counts_method_calls(self):
        "プロキシはメソッドが呼ばれた回数を数えます"
        tv = Proxy(Television())

        tv.power()
        tv.channel = 48
        tv.power()

        self.assertEqual(2, tv.number_of_times_called('power'))
        self.assertEqual(1, tv.number_of_times_called('channel'))
        self.assertEqual(0, tv.number_of_times_called('is_on'))

    def test_proxy_can_record_more_than_just_tv_objects(self):
        "プロキシは tv オブジェクト以外にも使えます"
        proxy = Proxy("Py Ohio 2010")

        result = proxy.upper()

        self.assertEqual("PY OHIO 2010", result)

        result = proxy.split()

        self.assertEqual(["Py", "Ohio", "2010"], result)
        self.assertEqual(['upper', 'split'], proxy.messages())

# ====================================================================
# 下記のコードはプロキシクラスのテストに使用されます。
# このコメント以降は書き換えないでください。
# The following code is to support the testing of the Proxy class.  No
# changes should be necessary to anything below this comment.

# 上記のプロキシのテストで使用するクラスです
# Example class using in the proxy testing above.
class Television:
    def __init__(self):
        self._channel = None
        self._power = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        if self._power == 'on':
            self._power = 'off'
        else:
            self._power = 'on'

    def is_on(self):
        return self._power == 'on'

# Television クラスのテストコードです。すべてにパスしないといけません。
# Tests for the Television class.  All of theses tests should pass.
class TelevisionTest(Koan):
    "テレビのテスト"
    def test_it_turns_on(self):
        "電源が入ること"
        tv = Television()

        tv.power()
        self.assertTrue(tv.is_on())

    def test_it_also_turns_off(self):
        "電源を消せること"
        tv = Television()

        tv.power()
        tv.power()

        self.assertFalse(tv.is_on())

    def test_edge_case_on_off(self):
        "電源 ON/OFF の境界値分析"
        tv = Television()

        tv.power()
        tv.power()
        tv.power()

        self.assertTrue(tv.is_on())

        tv.power()

        self.assertFalse(tv.is_on())

    def test_can_set_the_channel(self):
        "チャンネルを選べること"
        tv = Television()

        tv.channel = 11
        self.assertEqual(11, tv.channel)
