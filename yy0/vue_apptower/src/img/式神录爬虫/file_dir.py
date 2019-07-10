# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os


def file_name(file_dir):
    fname_list = []
    for root, dirs, fname in os.walk(file_dir):
        for i in fname:
            k = i.replace('.png', '')
            fname_list.append(k)
        return fname_list

a = file_name("./式神")
print(a)
