# Importing Pandas library
import pandas as pd

# Creating two lists
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
article = [210, 211, 114, 178]
# Creating two Series by passing lists
auth_series = pd.Series(author)
article_series = pd.Series(article)
# Creating a dictionary by passing Series objects as values
frame = {'Author': auth_series, 'Article': article_series}
# Creating DataFrame by passing Dictionary
result = pd.DataFrame(frame)
# Printing elements of Dataframe
print(result)