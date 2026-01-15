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
# %%
# Recipe
# 1. Create a GitHub repo whether by forking, cloning, or just making a new one.
# 2. Open VS codes from GitHub codespaces.
# 3. Create a virtual environment in your local machine or codespace.
# 4. Install necesasary extensions in your codespace and freeze it into a requirements.txt file.
# 5. Create a .py file or another type of file to write your code.
# 6. Commit and push your changes to your GitHub repo.
