# -*- coding: utf-8 -*-

from app import freezer
from prepare import prepare

if __name__ == '__main__':
    prepare()
    freezer.freeze()