from sklearn.ensemble import RandomForestClassifier
import joblib

def treinar_modelo(X_train, y_train, n_estimators=200, max_depth=None, random_state=42):
    """
    Treina um modelo de RandomForestClassifier.
    Parâmetros:
    - X_train: Features de treinamento(valores de entrada).
    - y_train: Labels de treinamento(valores de "saída"/o resultado de cada linha).
    - n_estimators: Número de árvores na floresta(valores de cada arvore sao comparados no final).
    - max_depth: Profundidade máxima das árvores(nesse caso máxima).
    - random_state: Semente para reprodutibilidade(Garante uma aleatoridade controlada).
    """

    print('+' * 20)
    print("Treinando o modelo RandomForestClassifier...")
    print('+' * 20)

    modelo = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1  # Usa todos os núcleos do processador para acelerar o treinamento
    )

    print('+' * 20)
    print("Modelo treinado com sucesso!")
    print('+' * 20)

    modelo.fit(X_train, y_train)
    return modelo

def salvar_modelo(modelo, caminho='modelo_randomforest.pkl'):
    """
    Salva o modelo treinado em um arquivo para uso posterior.
    """
    joblib.dump(modelo, caminho)
    print(f"Modelo salvo em: {caminho}")