#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from firecalc.core.line_item import Amount, LineItem, LineGroup


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

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_str(self):
        amount = 10

        # Test printing Amount
        a = Amount('$', 'year', amount)
        print(a)


class TestLineItem:
    def test_cost(self):
        amount = 100
        income = 1000
        a = Amount('$', 'year', amount)
        l = LineItem('Food', a, 2)

        assert(l.cost(income) == amount * 1)


class TestLineGroup:
    def test_init(self):
        # Test with no items
        a = LineGroup('a')
        assert(a.items == [])

        # Test with some items
        i_a = Amount('$', 'year', 10)
        i_b = Amount('$', 'week', 20)
        line_items = [i_a, i_b]
        b = LineGroup('b', line_items)
        assert(b.items == [i_a, i_b])

        line_items.append('hello world')
        assert(b.items == [i_a, i_b])

        # TODO(tjdevries): Add a check for only acceptable items in items

    def test_add_item(self):
        g = LineGroup('Food')

    def test_cost(self):
        g = LineGroup('Food')
