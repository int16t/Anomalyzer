from preprocessamento import preprocess

train_path = '../data/NSL_KDD_Train.csv'
test_path = '../data/NSL_KDD_Test.csv'

X_train, y_train, X_test, y_test, scaler = preprocess(train_path, test_path)
