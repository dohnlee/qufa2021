import json
import argparse

import pandas as pd
from sklearn.preprocessing import StandardScaler

from outlier_detection import Detector


def get_data(input_fname):
    data = pd.read_csv(input_fname)
    num_idxs = data.dtypes[data.dtypes != 'object'].index
    num_vars = [data.columns.get_loc(idx) for idx in num_idxs]

    X_numeric = data.iloc[:, num_vars]
    X_numeric = StandardScaler().fit_transform(X_numeric)
    return X_numeric

def get_outlier_rate(input_fname):
    X_numeric = get_data(input_fname)
    
    detector = Detector()
    outlier_idxs = detector.fit_extract(X_numeric)
    
    N = X_numeric.shape[0]
    outlier_rate = len(outlier_idxs) / N
    return outlier_rate


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fname')
    args = parser.parse_args()

    outlier_rate = get_outlier_rate(args.input_fname)
    print(outlier_rate)
