#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Amount:
    """
    Amount object. Used to describe different types of amounts on a yearly basis.

    For example, a weekly expense of fixed amount will have 52 payments per year,
        so the total cost will be 52 * amount
    """
    periods_per_year = {
        'year': 1,
        'month': 12,
        'day': 365,
    }

    styles = ('%', '$')

    def __init__(self, style, period, amount):
        """
        Initialize the Amount

        Args:
            style (str): An acceptable style of payment. Currently specified by self.styles
            period (str): An acceptable payment period. Currently specified in the keys of self.periods_per_year
            amount (numeric): The amount of payment per period.
        """
        if style not in self.styles:
            raise ValueError('Style must be of type: {0}'.format(self.styles))
        else:
            self.style = style

        if period not in self.periods_per_year.keys():
            raise ValueError('Period must be a valid period. {0}'.format(list(self.periods_per_year.keys())))
        else:
            self.period = period
            self.multiplier = self.periods_per_year[period]

        # TODO(tjdevries): Check that amount is "good"
        #   For example, when it's % based, should not allow numbers over 100
        self.amount = amount

    def payment(self, income):
        if self.style == '%':
            return (self.amount / 100) * (income / self.multiplier)
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
