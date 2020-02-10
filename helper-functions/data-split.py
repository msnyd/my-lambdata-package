from sklearn.model_selection import train_test_split
import pandas as pd

data = ''
target = ''


def data_split(data, target):
    
    train, val, = train_test_split(data, random_state = 42)

    train_features = train.drop(columns=[target])

    numeric_features = train_features.select_dtypes(include='number').columns.tolist()

    cardinality = train_features.select_dtypes(exclude='number').nunique()

    categorical_features = cardinality[cardinality <= 50].index.tolist()

    features = numeric_features + categorical_features

    X_train = train[features]
    y_train = train[target]
    X_val = val[features]
    y_val = val[target]

    print('X_train shape', X_train.shape)
    print('X_test shape', X_val.shape)
    print('y_train shape', y_train.shape)
    print('y_test shape', y_val.shape)