#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Amount:
    periods_per_year = {
        'year': 1,
        'month': 12,
        'day': 365,
    }

    styles = ('%', '$')

    def __init__(self, style, period, amount):
        if style not in self.styles:
            raise ValueError('Style must be of type: {0}'.format(self.styles))
        else:
            self.style = style

        if period not in self.periods_per_year.keys():
            raise ValueError('Period must be a valid period. {0}'.format(self.periods_per_year.keys()))
        else:
            self.period = period
            self.multiplier = self.periods_per_year[period]

    def payment(self, income):
        if self.style == '%':
            return self.amount / 100 * income
        elif self.style == '$':
            return self.amount


    def cost(self, income):
        """
        Returns the yearly monetary cost/value of this item
        """
        return self.multiplier * self.payment(income)

class Expense:
    def __init__(self, amount: Amount):
        self.amount = amount
