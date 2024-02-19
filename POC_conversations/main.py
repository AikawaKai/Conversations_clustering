# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import pandas as pd
from renumics import spotlight
from IPython.display import display





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("https://renumics.com/data/mnist/mnist-tiny.csv")
    display(df)
    spotlight.show(df, dtype={"image": spotlight.Image})


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
