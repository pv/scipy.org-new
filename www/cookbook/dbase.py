# <markdowncell>

# Update - 1/18/2007
# ==================
# 
# `* Added a function to convert a data-dictionary to a rec-array (Pierre GM).`
# 
# Update - 1/14/2007
# ==================
# 
# `* Replaces missing values with 'nan'`\
# `* Loads non-numeric data from csv`
# 
# Dbase
# =====
# 
# The [dbase.py](![](files/dbase_attachments/dbase.0.7.py) class, can be used to
)# read/write/summarize/plot time-series data.
# 
# To summarize the functionality:
# 
# `1. data and variable names stored in a dictionary - accessible using variable names`\
# `1. load/save from/to csv/pickle format, including date information (shelve format to be added)`\
# `1. plotting and descriptive statistics, with dates if provided`\
# `1. adding/deleting variables, including trends/(seasonal)dummies`\
# `1. selecting observations based on dates or other variable values (e.g., > 1/1/2003)`\
# `1. copying instance data`
# `Attached also the `[`dbase_pydoc.txt`](![](files/dbase_attachments/dbase_pydoc.0.2.txt)` information for the class.`
)# 
# Example Usage
# -------------
# 
# To see the class in action download the file and run it (python
# dbase.py). This will create an example data file
# (./dbase\_test\_files/data.csv) that will be processed by the class.
# 
# To import the module:
# 
# <codecell>


#!python
import dbase

# <markdowncell>

# After running the class you can load the example data using
# 
# <codecell>


#!python
data = dbase.dbase("./dbase_test_files/data.csv", date = 0)

# <markdowncell>

# In the above command '0' is the index of the column containing dates.
# 
# You can plot series 'b' and 'c' in the file using
# 
# <codecell>


#!python
data.dataplot('b','c')

# <markdowncell>

# <![](files/dbase_attachments/ex_plot.0.1.png>
)# 
# You get descriptive statistics for series 'a','b', and 'c' by using
# 
# <codecell>


#!python
data.info('a','b','c')

# <markdowncell>

# Since there is date information in [data.csv](![](files/dbase_attachments/data.0.3.csv)
)# this information will be added automatically when calling dataplot() or
# info().
# 
# There is an extensive set of examples at the bottom of the code file
# that demonstrates the functionality of the class.
# 
# * * * * *
# 
# CategoryCookbook
# 