# sklern toy datasets
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston

dataBoston = load_boston()
# print(dataBoston)
# print(dir(dataBoston))
# ['DESCR', 'data', 'feature_names', 'filename', 'target']
# print(dataBoston['DESCR'])
# print(dataBoston['data'].shape)
# print(dataBoston['data'][0])

df = pd.DataFrame(
    dataBoston['data'],
    columns= dataBoston['feature_names']
)
print(df)