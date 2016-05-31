#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script of how to use this library.

This will show the basic functionality and then graph it at the end!
"""

import os.path
from bokeh.plotting import figure, output_file, save

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file(os.path.expanduser('~/Downloads/example_graph.html'))

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

save(p)
