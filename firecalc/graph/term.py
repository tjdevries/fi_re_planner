#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Basic graphing capabilities meant for terminal use.

This may end upbeing used by other graphing items, if the work does end
    up being fairly modular. Otherwise it will be primarily used for
    development purposes.
"""

from bokeh.plotting import figure, output_file

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("~/Downloads/example_graph.html", title="line plot example")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)
