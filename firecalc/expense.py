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


class Expense:

    """
    Expense object.

    More to come
    """

    def __init__(self, amount: Amount, income: float):
        """
        Initialize the Expense for a certain category.

        Args:
            amount (Amount): An amount object that will be used in the expenses
            income (float): An income for the person whose expense this will be
        """
        self.amount = amount
        self.income = income
