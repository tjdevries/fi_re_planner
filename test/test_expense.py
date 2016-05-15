#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from firecalc.expense import Amount


class TestAmount:
    def test_init_style(self):
        a = Amount('$', 'year', 10)
        assert(a.style == '$')

        b = Amount('%', 'year', 10)
        assert(b.style == '%')

        with pytest.raises(ValueError):
            c = Amount('x', 'year', 10)
            c

    def test_init_period(self):
        periods_per_year = {
            'year': 1,
            'month': 12,
            'day': 365,
        }

        for period in periods_per_year:
            temp = Amount('$', period, 10)
            assert(temp.period == period)
            assert(temp.multiplier == periods_per_year[period])

        with pytest.raises(ValueError):
            a = Amount('$', 'not a date', 10)
            a

    def test_cost(self):
        amount = 10
        income = 1000

        # Test regular dollar amount
        a = Amount('$', 'year', amount)
        assert(a.cost(income) == amount * 1)

        b = Amount('$', 'month', amount)
        assert(b.cost(income) == amount * 12)

        c = Amount('$', 'day', amount)
        assert(c.cost(income) == amount * 365)

        # Test percentage dollar amount
        d = Amount('%', 'year', amount)
        assert(d.cost(income) == amount / 100 * income)

        e = Amount('%', 'day', amount)
        assert(e.cost(income) == amount / 100 * income)

    def test_str(self):
        amount = 10
        income = 1000

        # Test printing Amount
        a = Amount('$', 'year', amount)
        print(a)
