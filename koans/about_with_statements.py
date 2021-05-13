#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutSandwichCode in the Ruby Koans
#

from runner.koan import *

import re # 正規表現での文字列比較で使用 For regular expression string comparisons

class AboutWithStatements(Koan):
    "with 構文"

    def count_lines(self, file_name):
        try:
            file = open(file_name)
            try:
                return len(file.readlines())
            finally:
                file.close()
        except IOError:
            # 発生しないはず
            # should never happen
            self.fail()

    def test_counting_lines(self):
        "行数のカウント"
        self.assertEqual(__, self.count_lines("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line(self, file_name):
        try:
            file = open(file_name)
            try:
                for line in file.readlines():
                    match = re.search('e', line)
                    if match:
                        return line
            finally:
                file.close()
        except IOError:
            # 発生しないはず
            # should never happen
            self.fail()

    def test_finding_lines(self):
        "行の検索"
        self.assertEqual(__, self.find_line("example_file.txt"))

    ## ------------------------------------------------------------------
    ## 考えてみましょう：
    ## THINK ABOUT IT:
    ##
    ## count_lines と find_line メソッドは似ていますが違いがあります
    ## どちらも "サンドイッチコード" パターンに従っています
    ## The count_lines and find_line are similar, and yet different.
    ## They both follow the pattern of "sandwich code".
    ##
    ## サンドイッチコードは3つのパートに分けられます:
    ## (1) 上のパン (2) 肉 (3) 下のパン
    ## パンの部分は大抵いつも同じですが、肉の部分は常に異なります
    ## Sandwich code is code that comes in three parts: (1) the top slice
    ## of bread, (2) the meat, and (3) the bottom slice of bread.
    ## The bread part of the sandwich almost always goes together, but
    ## the meat part changes all the time.
    ##
    ## サンドイッチコードの異なる部分は間の肉の部分なので、多くの言語では、
    ## 上下のパンの部分だけを抽象化してライブラリにするのは困難です。
    ## Because the changing part of the sandwich code is in the middle,
    ## abstracting the top and bottom bread slices to a library can be
    ## difficult in many languages.
    ##
    ## (C++ は別です：スマートポインタにおけるメモリの所有権の考え方は
    ## リソース確保時のサンドイッチコードの問題を扱うものです)
    ## (Aside for C++ programmers: The idiom of capturing allocated
    ## pointers in a smart pointer constructor is an attempt to deal with
    ## the problem of sandwich code for resource allocation.)
    ##
    ## Python ではコンテキストマネージャを使ってこの問題を解決します。
    ## 次のコードを見てみましょう。
    ## Python solves the problem using Context Managers. Consider the
    ## following code:
    ##

    class FileContextManager():
        def __init__(self, file_name):
            self._file_name = file_name
            self._file = None

        def __enter__(self):
            self._file = open(self._file_name)
            return self._file

        def __exit__(self, cls, value, tb):
            self._file.close()

    # 今度はこのように書くことができます
    # Now we write:

    def count_lines2(self, file_name):
        with self.FileContextManager(file_name) as file:
            return len(file.readlines())

    def test_counting_lines2(self):
        "行数のカウント２"
        self.assertEqual(__, self.count_lines2("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line2(self, file_name):
        # コンテキストマネージャ self.FileContextManager を使って、文字'e'を
        # 含む最初の行を返すようにこのメソッドを書き換えてください
        # Using the context manager self.FileContextManager, rewrite this
        # function to return the first line containing the letter 'e'.
        return None

    def test_finding_lines2(self):
        self.assertNotEqual(None, self.find_line2("example_file.txt"))
        self.assertEqual('test\n', self.find_line2("example_file.txt"))

    # ------------------------------------------------------------------

    def count_lines3(self, file_name):
        with open(file_name) as file:
            return len(file.readlines())

    def test_open_already_has_its_own_built_in_context_manager(self):
        "open 関数には、それ自身のコンテキストマネージャがあります"
        self.assertEqual(__, self.count_lines3("example_file.txt"))
