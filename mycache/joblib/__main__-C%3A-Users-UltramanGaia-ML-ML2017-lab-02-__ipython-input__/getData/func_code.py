# first line: 1
@mem.cache
def getData():
    train_X, train_y = load_svmlight_file('data/a9a', n_features=123)
    test_X, test_y = load_svmlight_file('data/a9a.t', n_features=123)

    train_y =  train_y.reshape(train_y.shape[0],1)
    test_y =  test_y.reshape(test_y.shape[0],1)

    train_y[train_y == -1] = 0
    test_y[test_y == -1] = 0
    return train_X, test_X, train_y, test_y
