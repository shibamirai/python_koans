#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cls_name(obj):
    doc = obj.__class__.__doc__ + ": " if obj.__class__.__doc__  else ""
    return doc + obj.__class__.__name__