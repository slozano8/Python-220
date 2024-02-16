# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 22:13:27 2024

@author: Santo
"""

from sqlalchemy import *

import pandas as pd

data = sqlalchemy.create_engine('sqlite:////path/books.db')

#select and print the title column from the book table in alphabetical order.
df=pd.read_sql('Book about python',data)

print(df)