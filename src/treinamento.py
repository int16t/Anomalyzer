from time import sleep
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path
from utils import linha, centralizar

def treinar_modelo(X_train, y_train, n_estimators=300, max_depth=None, random_state=42):
    """
    Treina um modelo de RandomForestClassifier.
    Parâmetros:
    - X_train: Features de treinamento(valores de entrada).
    - y_train: Labels de treinamento(valores de "saída"/o resultado de cada linha).
    - n_estimators: Número de árvores na floresta(valores de cada arvore sao comparados no final).
    - max_depth: Profundidade máxima das árvores(nesse caso máxima).
    - random_state: Semente para reprodutibilidade(Garante uma aleatoridade controlada).
    """

    for x in tqdm(range(100),
        desc="Treinando o modelo Random Forest",
        ncols=100):
        sleep(0.15)

    modelo = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        class_weight='balanced', # Aumenta o Recall mas diminui a precisão
        n_jobs=-1  # Usa todos os núcleos do processador para acelerar o treinamento
    )

    print()
    print(centralizar("Modelo treinado com sucesso!", 160))
    sleep(1)
    linha('=', 160)


    modelo.fit(X_train, y_train)
    return modelo

def salvar_modelo(modelo, caminho=None):
    """
    Salva o modelo treinado em um arquivo para uso posterior.
    Cria automaticamente o diretório se não existir.
    """
    if caminho is None:
        # Obtém o diretório do projeto e cria o caminho para a pasta models
        BASE_DIR = Path(__file__).resolve().parent.parent
        models_dir = BASE_DIR / 'models'
        caminho = models_dir / 'modelo_randomforest.pkl'
    else:
        # Converte para Path se for string que o usuario digitar
        caminho = Path(caminho)
    
    # Cria o diretório pai se não existir (funciona para qualquer caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    
    joblib.dump(modelo, caminho)
    print(centralizar("SALVANDO O MODELO", 160))
    print()
    print(f"Modelo salvo em: {caminho}")
    linha('=', 160)