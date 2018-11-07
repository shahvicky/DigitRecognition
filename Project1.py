# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:15:34 2018

@author: doshi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'train.csv'

df = pd.read_csv(url)

train_label = pd.DataFrame(df['label'])
train_columns = df.drop('label', axis = 1)

image = {}

for i in range(9):
    image[i] = df[df['label'] == i]

print(np.array(train_columns.loc[0]))

#print(image[0].drop('label', axis = 1).iloc[0])


fig = plt.figure()
plt.subplot(3,3,i+1)
plt.tight_layout()
plt.imshow(np.array(train_columns.loc[0]), cmap='gray', interpolation='none')
plt.title("Digit: 0")
plt.xticks([])
plt.yticks([])
plt.show()  