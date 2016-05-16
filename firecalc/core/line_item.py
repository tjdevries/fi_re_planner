#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Handles all the different expense accounts.

Maybe need a different name for all the fire calculations.
"""


class Amount:

    """
    Amount object. Used to describe different types of amounts on a yearly basis.

    For example, a weekly expense of fixed amount will have 52 payments per year,
        so the total cost will be 52 * amount
    """

    # Simple setup. May want to adjust this to be exact in the future.
    periods_per_year = {
        'year': 1,
        'month': 12,
        'week': 52,
        'day': 365,
    }

    styles = ('%', '$')

    def __init__(self, style, period, amount):
        """
        Initialize the Amount.

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
        """
        Calculate the value for each installment.

        Args:
            income (float): The income of the person to be considered in percentage based amounts

        Returns:
            pay (float): The value of the installment.
        """
        if self.style == '%':
            pay = (self.amount / 100) * (income / self.multiplier)
        elif self.style == '$':
            pay = self.amount

        return pay

    def cost(self, income):
        """
        Calculate the yearly monetary cost/value of this item.

        Args:
            income (float): An income for the person whose expense this will be
        """
        return self.multiplier * self.payment(income)

    def __str__(self):
        return 'Amount: Style={0}, Period={1}, Amount={2}'.format(self.style, self.period, self.amount)

    def __repr__(self):
        return '<Amount Obj: {0}, {1}, {2}>'.format(self.style, self.period, self.amount)


class Expense:

    """
    Expense object.

    More to come
    """

    def __init__(self, name: str, amount: Amount, duration: float=None):
        """
        Initialize the Expense for a certain category.

        Args:
            name (str): The name of the expense
            amount (Amount): An amount object that will be used in the expenses
            duration
        """
        self.name = name
        self.amount = amount

        if duration:
            self.duration = duration
        else:
            # Set to a big number.
            self.durationg = 999

    def cost(self, income):
        """
        Calculate the yearly monetary cost/value of this expense.

        Args:
            income (float): An income for the person whose expense this will be
        """
        return self.amount.cost(income)

    def total_cost(self, income):
        """
        Calculate the total cost without any other factors.

        This might be useless

        Args:
            income (float): An income for the person whose expense this will be
        """
        return self.cost(income) * self.duration

    def __str__(self):
        return 'Expense {0}: Amount {1}'.format(self.name, self.amount)

    def __repr__(self):
        return '<Expense Obj: {0}>'.format(self.name)
