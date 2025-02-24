import pandas as pd

""" When we have a dataframe we can work with the data and save the results in other formats.
pandas has the method unique to determine the unique elements in a column of a dataframe."""

""" Let’s say we would like to determine the unique year of the albums in the data set. """

csv_path="file2.csv"
df=pd.read_csv(csv_path, sep='\\s+')

songs_frame = pd.DataFrame(df)

a = df["Released"].unique() #We enter the name of the dataframe, then enter the name of the column ‘Released’ within brackets.


""" Let's say we would like to create a new database consisting of songs from the 2000's and after. 
We can look at the column ‘Released’ for songs made after 1999, then select the corresponding columns.
We can accomplish this within one line of code in Pandas"""

b = df["Released"]>=2000   #The result is a series of Boolean values.

df1 = df[df["Released"]>=2000]  #We now have a new dataframe, where each album was released after 1999

""" We can save the new dataframe using the method to_csv """

df1.to_csv('new_songs.csv')

df3=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})

test = df3['a']==1 