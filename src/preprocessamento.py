import pandas as pd
from sklearn.preprocessing import StandardScaler

def carregar_dados(train_path, test_path):
    """
    Carrega os dados de treinamento e teste a partir dos caminhos fornecidos.
    """
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def limpar_dados(df):
    """
    Realiza a limpeza básica dos dados, como remoção de valores nulos e duplicatas.
    """
    df = df.dropna().drop_duplicates()
    return df

def converter_rotulos(df):
    """
    Converte rótulos em números. Sendo uma conexão normal = 0 e anômala = 1.
    """
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
    return df

def codificar_categorias(train_df, test_df, categorical_cols):
    """
    Codifica variáveis categóricas usando One-Hot Encoding e normaliza os dados se especificado.
    """
    all_df = pd.concat([train_df, test_df], sort=False)
    all_df = pd.get_dummies(all_df, columns=categorical_cols)

    # Repartir os dados novamente
    train_df = all_df.iloc[:len(train_df), :]
    test_df = all_df.iloc[len(train_df):, :]

    return train_df, test_df

def normalizar_dados(train_df, test_df, normalize=True):
    """
    Normaliza os dados numéricos usando StandardScaler se normalize for True.
    """
    scaler = None
    num_cols = train_df.select_dtypes(include=['float64', 'int64']).columns.difference(['label'])
    if normalize:
        scaler = StandardScaler()
        # Ajustar e transformar os dados de treinamento
        train_df[num_cols] = scaler.fit_transform(train_df[num_cols])
        
        # Transformar os dados de teste
        test_df[num_cols] = scaler.transform(test_df[num_cols])

    return train_df, test_df

def separar_features_labels(train_df, test_df):
    """
    Separa as features e os labels dos dataframes de treinamento e teste.
    """
    X_train = train_df.drop('label', axis=1)
    y_train = train_df['label']
    X_test = test_df.drop('label', axis=1)
    y_test = test_df['label']
    return X_train, y_train, X_test, y_test


def preprocess(train_path, test_path, normalize=True):
    """
    Função principal de pré-processamento que integra todas as etapas.
    1. Carrega os dados.
    2. Limpa os dados.
    3. Converte rótulos.
    4. Codifica variáveis categóricas.
    5. Normaliza os dados (opcional).
    6. Separa features e labels.
    Retorna os conjuntos de dados prontos para modelagem.
    """
    print("Iniciando pré-processamento...")

    train_df, test_df = carregar_dados(train_path, test_path)

    train_df = limpar_dados(train_df)
    test_df = limpar_dados(test_df)

    train_df = converter_rotulos(train_df)
    test_df = converter_rotulos(test_df)

    categorical_cols = ['protocol_type', 'service', 'flag']
    train_df, test_df = codificar_categorias(train_df, test_df, categorical_cols)

    train_df, test_df, scaler = normalizar_dados(train_df, test_df, normalize)

    X_train, y_train, X_test, y_test = separar_features_labels(train_df, test_df)

    print("Pré-processamento concluído!\n")
    return X_train, y_train, X_test, y_test, scaler