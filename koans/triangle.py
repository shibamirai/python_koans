#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle プロジェクトのコード
# Triangle Project Code.

# triangle 関数は三角形の3辺の長さ(引数 a, b, cで与えられる)を調べ、三角形の種類を返す
# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# 次の文字列を返す：
#   'equilateral'  3辺がすべて等しい（正三角形）
#   'isosceles'    いずれか2辺が等しい（二等辺三角形）
#   'scalene'      すべての辺の長さが異なる（不等辺三角形）
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# この関数のテストコードは
#   about_triangle_project.py
# と
#   about_triangle_project2.py
# にあります
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # 'pass' を消して、ここにコードを書いてください
    # DELETE 'PASS' AND WRITE THIS CODE
    if (a <= 0 or b <= 0 or c <= 0):
        raise TriangleError
    elif (a + b <= c or b + c <= a or c + a <= b):
        raise TriangleError

    if (a == b and a == c):
        return 'equilateral'
    elif (a == b or b == c or c == a):
        return 'isosceles'
    else:
        return 'scalene'

# パート2で使われるエラークラス。これを修正する必要はありません
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
