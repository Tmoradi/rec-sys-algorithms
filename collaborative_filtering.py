import pandas as pd 
import numpy as np
import tensorflow_datasets as tfds 


if __name__ == '__main__':
   movies = pd.read_csv('../datasets/movielens-100k/')