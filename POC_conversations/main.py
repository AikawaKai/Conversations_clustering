# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from renumics import spotlight
from IPython.display import display


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_pickle("embedding_L12_clustered_LLM_banking_classes.pkl")
    display(df)
    print(df["Zephyr"])
    spotlight.show(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
