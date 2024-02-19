# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import pandas as pd
from renumics import spotlight
from IPython.display import display





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("test.csv")
    display(df)
    df = df.drop('Unnamed: 0.1', axis=1).drop('Unnamed: 0', axis=1)
    spotlight.show(df)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
