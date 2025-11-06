import os
from pathlib import Path
from preprocessamento import preprocess
from treinamento import treinar_modelo, salvar_modelo
from avaliacao import avaliar_modelo, plotar_barras_confusao, plotar_heatmap_confusao, salvar_grafico_distribuicao_classes, plot_precision_recall_f1



# Obtém o diretório do arquivo atual e navega até a pasta data
BASE_DIR = Path(__file__).resolve().parent.parent
train_path = BASE_DIR / 'data' / 'NSL_KDD_Train.csv'
test_path = BASE_DIR / 'data' / 'NSL_KDD_Test.csv'

X_train, y_train, X_test, y_test, scaler, train_df = preprocess(train_path, test_path)

modelo = treinar_modelo(X_train, y_train)

salvar_modelo(modelo)
salvar_grafico_distribuicao_classes(train_df)

cm, y_pred, f1 = avaliar_modelo(modelo, X_test, y_test)
plotar_barras_confusao(cm)
plotar_heatmap_confusao(cm)
plot_precision_recall_f1(y_test, y_pred)