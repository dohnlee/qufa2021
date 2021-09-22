import json
import argparse

import pandas as pd


def get_data(input_fname):
    data = pd.read_csv(input_fname)
    num_idxs = data.dtypes[data.dtypes != 'object'].index
    num_vars = [data.columns.get_loc(idx) for idx in num_idxs]
    cat_vars = sorted(set(range(data.shape[1])) - set(num_vars))
    
    X_numeric = data.iloc[:, num_vars]
    return X_numeric

def get_numerical_missing_rate(input_fname):
    X_numeric = get_data(input_fname)
    
    missing_count = pd.isnull(X_numeric).sum().sum()
    total_count = X_numeric.shape[0] * X_numeric.shape[1]
    numerical_missing_rate = missing_count / total_count
    return numerical_missing_rate


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fname')
    args = parser.parse_args()

    numerical_missing_rate = get_numerical_missing_rate(args.input_fname)
    print(numerical_missing_rate)
