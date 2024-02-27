import pandas as pd
from tkinter import filedialog, Tk
from renumics import spotlight
from IPython.display import display

def browse_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
    return file_path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = browse_file()
    
    if file_path:
        df = pd.read_pickle(file_path)
        spotlight.show(df)
