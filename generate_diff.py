import sys
import getopt

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

FILE_BEFORE_OPTI = "examples/before.txt"
FILE_AFTER_OPTI = "examples/after.txt"
# Specify the file where your labels are. If None, take range(1, len(line in before file))
LABEL_FILE = None

LABEL_BEFORE = "Before optimization"
LABEL_AFTER = "After optimization"
X_LABEL = "Number of iteration"
Y_LABEL = "Seconds"
TITLE = "Evoltion of time before and after the optimization"

# Size of the matplotlib figure
HEIGHT = 10
WIDTH = 15

# You can specify here your label
def get_labels(before_data, after_data):
    if LABEL_FILE:
        return read_file(LABEL_FILE)
    return [f"{x}" for x in range(1, len(before_data) + 1)]

def read_file(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(float(line.strip()))
    return result

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate("",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def show_figure(output: str = None):
    before = read_file(FILE_BEFORE_OPTI)
    after = read_file(FILE_AFTER_OPTI)

    labels = get_labels(before, after)

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, before, width, label=LABEL_BEFORE)
    rects2 = ax.bar(x + width/2, after, width, label=LABEL_AFTER)

    ax.set_ylabel(Y_LABEL)
    ax.set_title(TITLE)
    ax.set_xticks(x)
    ax.set_xlabel(X_LABEL)
    ax.set_xticklabels(labels)
    ax.legend()

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    fig.set_figheight(HEIGHT)
    fig.set_figwidth(WIDTH)
    fig.tight_layout()
    
    if not output:
        plt.show()
    else:
        plt.savefig(output)

def usage():
    print(f"Usage: {sys.argv[0]} [-o <output-file>]")
    exit(-1)

def parse_arguments() -> (str, str):
    try:
        help_mode = False
        output = None
        opts, args = getopt.getopt(sys.argv[1:], "o:h", ["output=", "help"])
        for (opt, value) in opts:
            if opt in ("-h", "--help"):
                help_mode = True
            elif opt in ("-o", "--output"):
                output = str(value)
        if help_mode:
            usage()
        return output
    except Exception :
        usage()

def main():
    output = parse_arguments()
    show_figure(output)

if __name__ == "__main__":
    main()
