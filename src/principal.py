from preprocessamento import preprocess
from treinamento import treinar_modelo, salvar_modelo


train_path = '../data/NSL_KDD_Train.csv'
test_path = '../data/NSL_KDD_Test.csv'

X_train, y_train, X_test, y_test, scaler = preprocess(train_path, test_path)

modelo = treinar_modelo(X_train, y_train)

salvar_modelo(modelo)