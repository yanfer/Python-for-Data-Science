import pandas as pd

""" Let’s say we would like to load a csv file using the pandas built-in function “read csv.” """

csv_path="file1.csv"
df=pd.read_csv(csv_path, sep='\\s+')

""" 
One way pandas allows you to work with data is with a data frame. 
Let's go over the process to go from a csv file to a data frame.
"""
df.head() #We can use the method head to examine the first 5 rows of a dataframe.


""" The process for loading an excel file is similar. We use the path of the excel file.
The function reads excel. The result is a dataframe. """

xlsx_path = "file1.xlsx"

df2 = pd.read_excel(xlsx_path)
df2.head()

""" We can create a data frame out of a dictionary. The keys correspond to the column labels. 
The values are lists corresponding to the rows."""

songs = {"Album":["Thriller","Back in Black","Ocean Avenue","Page Avenue"],
         "Released":[1982,1980,2003,2004],
         "Length":["00:42:19","00:42:11","00:57:44","00:52:33"]}

""" We then cast the dictionary to a dataframe using the function DataFrame. """
songs_frame = pd.DataFrame(songs)

""" We can create a new dataframe consisting of one column.We just put the dataframe name, 
in this case "df" and the name of the column header enclosed in double brackets."""

x=songs['Length']
y=df2[['Piezas']]

""" You can do the same thing for multiple columns. """
w=df2[['Piezas','Clientes']]

""" ne way to access unique elements is the ix method.  """
clms = df.columns # get the columns names

z = df.iloc[:,0:2] # take all rows in columns 1 and 2

z1 = df.iloc[0,1] # get the first row in the second column
