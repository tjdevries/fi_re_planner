#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from firecalc.expense import Amount

class TestAmount:
    def test_init_style(self):
        a = Amount('$', 'year', 10)

        assert(a.style == '$')
