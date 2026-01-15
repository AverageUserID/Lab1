# %%
# Terminal display path
"/workspaces/Lab1"
# You should not include your virtual environment in your repo
# The path does not change after creating a virtual environment
# %%
import pandas as pd
df = pd.read_csv("SpanishDecade.csv")
# %%
df.head()
# %%
# Extention Management
# There is a local and a codespaces section in the extention menu.
# Three useful elements of Data Wrangler are: 
# One, you can directly access a file and do data cleaning without loading it with pandas.
# Two, you can export the cleaning steps as a python script.
# Three, you can easily visualize and filter large tabular datasets.
# %%
# We use requirements.txt to manage dependencies in our project and record the packages need to run the program, so whoever clones our repo can easily install the required packages in a virtual environment.
