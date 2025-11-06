import os
from pathlib import Path
from preprocessamento import preprocess
from treinamento import treinar_modelo, salvar_modelo

# Obtém o diretório do arquivo atual e navega até a pasta data
BASE_DIR = Path(__file__).resolve().parent.parent
train_path = BASE_DIR / 'data' / 'NSL_KDD_Train.csv'
test_path = BASE_DIR / 'data' / 'NSL_KDD_Test.csv'

X_train, y_train, X_test, y_test, scaler = preprocess(train_path, test_path)

modelo = treinar_modelo(X_train, y_train)

salvar_modelo(modelo)