#Spam Detection algorithm using tensoflow

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv(r"C:\Users\devan\Desktop\Coding Folders\Python\Positiveway Internship\spam.csv", encoding='latin-1')

print(df.head())

