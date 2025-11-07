from time import sleep
from tqdm import tqdm
import pandas as pd
from sklearn.preprocessing import StandardScaler
from utils import linha, centralizar

def carregar_dados(train_path, test_path):
    """
    Carrega os dados de treinamento e teste a partir dos caminhos fornecidos.
    """
    # Nomes das colunas do dataset NSL-KDD
    col_names = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
                 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
                 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
                 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
                 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
                 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
                 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
                 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
                 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label']
    
    train_df = pd.read_csv(train_path, names=col_names)
    test_df = pd.read_csv(test_path, names=col_names)
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
    Retorna os dataframes normalizados e o scaler utilizado.
    """
    scaler = None
    num_cols = train_df.select_dtypes(include=['float64', 'int64']).columns.difference(['label'])
    if normalize:
        scaler = StandardScaler()
        # Ajustar e transformar os dados de treinamento
        train_df[num_cols] = scaler.fit_transform(train_df[num_cols])
        
        # Transformar os dados de teste
        test_df[num_cols] = scaler.transform(test_df[num_cols])

    return train_df, test_df, scaler

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
    linha('=', 160)
    for x in tqdm(range(100), desc="Iniciando pré-processamento", ncols=100):
        sleep(0.15)
    sleep(2)
    train_df, test_df = carregar_dados(train_path, test_path)

    train_df = limpar_dados(train_df)
    test_df = limpar_dados(test_df)

    train_df = converter_rotulos(train_df)
    test_df = converter_rotulos(test_df)

    categorical_cols = ['protocol_type', 'service', 'flag']
    train_df, test_df = codificar_categorias(train_df, test_df, categorical_cols)

    train_df, test_df, scaler = normalizar_dados(train_df, test_df, normalize)

    X_train, y_train, X_test, y_test = separar_features_labels(train_df, test_df)
    print()
    print(centralizar("Pré-processamento concluído!", 160))
    sleep(1)
    linha('=', 160)
    return X_train, y_train, X_test, y_test, scaler, test_df