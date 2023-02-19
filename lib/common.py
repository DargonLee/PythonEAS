#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :common.py
# @Time      :2023/2/18 11:03
# @Author    :Harlan
import hashlib

def pwd_to_sha256(pwd):
    h = hashlib.sha256()
    h.update('天青色等烟雨'.encode('utf-8'))
    h.update(pwd.encode('utf-8'))
    h.update('而我在等你'.encode('utf-8'))
    return h.hexdigest()


if __name__ == "__main__":
    run_code = 0
