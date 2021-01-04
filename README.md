## Description
This little script allows you to create a grouped bar chart with matplotlib.

You can change mutiple fields inside the script:
- `FILE_BEFORE`: This is the values before your changes. One line by value
- `FILE_AFTER`: This is the values after your changes. One line by value

You can find examples inside the `examples` directory

`LABEL_FILE` allows you the specify your own labels on the horizontal axis. If `None`, take the range of number of values inside `FILE_BEFORE`

`LEGEND_BEFORE` and `LEGEND_AFTER` are the name of bars

`X_LABEL` and `Y_LABEL` are the name of axis

## Usage

By default, the program only shows the chart.

`python3 generate_diff.py [-o <output-file>]`

With `-o`, you can specify an output and save the graph into a png
