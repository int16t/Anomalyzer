from sklearn.metrics import classification_report, confusion_matrix, f1_score, precision_recall_curve
from datetime import datetime
from pathlib import Path
from utils import linha, centralizar
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Diretório para salvar os gráficos
BASE_DIR = Path(__file__).resolve().parent.parent
out_dir = BASE_DIR / 'reports' / 'figures'

nome = f"matriz_confusao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

def avaliar_modelo(modelo, X_test, y_test):
    """
    Avalia o modelo treinado utilizando os dados de teste.
    Gera F1-score, relatório de classificação e matriz de confusão.
    """

    # 1) Previsões do modelo
    y_probs = modelo.predict_proba(X_test)[:, 1]
    y_pred = (y_probs >= 0.35).astype(int)

    # 2) Métrica principal
    f1 = f1_score(y_test, y_pred)
    linha('=', 160)
    print(centralizar("MÉTRICAS", 160))
    print(f"F1-Score do modelo: {f1:.4f}\n")

    # 3) Relatório completo (Precision, Recall, F1 para cada classe)
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred))

    # 4) Matriz de Confusão
    cm = confusion_matrix(y_test, y_pred)

    print("Matriz de Confusão:")
    print(cm)
    linha('=', 160)

    return cm, y_pred, f1

def salvar_grafico_distribuicao_classes(df, nome_arquivo = "distribuicao-classes-teste.png"):
    """
    Gera e salva um gráfico de barras mostrando quantas amostras existem
    de cada classe (normal x ataque) para o arquivo de teste.
    """

    # Garante que o diretório exista
    os.makedirs(out_dir, exist_ok=True)

    # Conta quantas ocorrências de cada classe existem / Converter 0/1 para nomes
    df_plot = df.copy()
    df_plot["label"] = df_plot["label"].replace({0: "Normal", 1: "Ataque"})

    contagem = df_plot["label"].value_counts()

    # Cria o gráfico
    plt.figure(figsize=(8,5))
    contagem.plot(kind='bar')
    plt.title("Distribuição de Classes no Dataset de Teste")
    plt.xlabel("Classe")
    plt.ylabel("Quantidade de Registros")
    
    # Caminho completo do arquivo
    caminho = out_dir / nome_arquivo
    
    # Salva a imagem
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    print(centralizar("GRÁFICO DE DISTRIBUIÇÃO", 160))
    print()
    print(f"Gráfico de distribuição salvo em: {caminho}")

def plotar_barras_confusao(cm, nome_arquivo="barras-matriz-confusao.png"):
    """
    Gera um gráfico de barras a partir da matriz de confusão.
    cm = [[TN, FP],
          [FN, TP]]
    """

    tn, fp, fn, tp = cm.ravel()

    valores = [tp, tn, fp, fn]
    categorias = ["TP (Verdadeiro Positivo)",
                  "TN (Verdadeiro Negativo)",
                  "FP (Falso Positivo)",
                  "FN (Falso Negativo)"]
    cores = ['tab:green', 'tab:blue', 'tab:orange', 'tab:red']

    plt.figure(figsize=(8,5))
    plt.bar(categorias, valores, color=cores)
    plt.title("Distribuição: TP / TN / FP / FN")
    plt.ylabel("Quantidade")
    plt.tight_layout()

    # caminho = os.path.join(out_dir, nome)

    caminho = out_dir / nome_arquivo

    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

    print(centralizar("GRÁFICOS DE MATRIZ DE CONFUSÃO", 160))
    print()
    print(f"Gráfico de distribuição salvo em: {caminho}")

def plotar_heatmap_confusao(cm, nome_arquivo="mapa-calor-matriz-confusao.png"):
    """
    Gera um heatmap a partir da matriz de confusão.
    cm = [[TN, FP],
          [FN, TP]]
    """

    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Normal', 'Ataque'],
                yticklabels=['Normal', 'Ataque'])
    plt.title("Matriz de Confusão")
    plt.ylabel("Classe Verdadeira")
    plt.xlabel("Classe Predita")
    plt.tight_layout()

    figures_dir = BASE_DIR / 'reports' / 'figures'
    caminho = figures_dir / nome_arquivo
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

    print(f"Gráfico de distribuição salvo em: {caminho}")

def plot_precision_recall_f1(y_test, y_scores, nome_arquivo="curva-precision-recall.png"):
    """
    Plota a Curva Precision-Recall e salva em /reports/figures.
    y_test: rótulos reais (0 = Normal, 1 = Ataque)
    y_scores: probabilidade prevista do modelo para classe 'Ataque'
    """
    
    
    precision, recall, thresholds = precision_recall_curve(y_test, y_scores)

    plt.figure(figsize=(6,5))
    plt.plot(recall, precision, linewidth=2)
    plt.xlabel("Recall (Revocação)")
    plt.ylabel("Precision (Precisão)")
    plt.title("Curva Precision-Recall")
    plt.grid(True)

    caminho = out_dir / nome_arquivo
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    
    plt.show()
    plt.close()

    linha("=", 160)
    print(centralizar("GRÁFICO DE PRECISION-RECALL", 160))
    print()
    print(f"Curva Precision-Recall salva em: {caminho}")