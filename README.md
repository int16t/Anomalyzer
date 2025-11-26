# Anomalyzer (PT) 
Projeto de Machine Learning (ML) voltado a identificação de anomalias em Tráfego de Redes. 

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![seaborn](https://img.shields.io/badge/seaborn-%2342a7f5.svg?style=for-the-badge&logo=seaborn&logoColor=white)

## Equipe
- Leonardo Gabriel Ramos dos Santos Souza (RA 2225201787)
- Gabriel Landim Zillig (RA 2224104595)
- Turma: 41 - SA | Curso: Ciência da Computação | Período: Noturno | Ano: 2025

## Problema
No contexto de redes de computadores, muitas empresas lidam com um grande volume de tráfego, o que torna desafiadora a identificação rápida de atividades maliciosas. É inviável que administradores de rede ou analistas de cibersegurança analisem pacote por pacote para proteger a organização contra vazamentos de dados, indisponibilidade de serviços ou quebra de integridade dos sistemas. Diante disso, desenvolvemos o Anomalyzer, um modelo de Inteligência Artificial capaz de analisar pacotes de rede legítimos e não legítimos, aprendendo a diferenciar conexões seguras de não seguras. O objetivo é auxiliar o time Blue Team no monitoramento e detecção proativa de anomalias em tráfego de rede.

## Abordagem de IA
O projeto utiliza aprendizado supervisionado, com o modelo de classificação Random Forest. Esse algoritmo constrói diversas árvores de decisão independentes e combina seus resultados para chegar a uma conclusão final mais robusta. Como o tráfego de rede apresenta dados variados — como src_bytes, dst_bytes, count e flag — o Random Forest se destaca por lidar bem com esse tipo misto de informações. Além disso, ele não depende de uma única regra, mas sim do consenso entre várias árvores, o que torna as previsões mais estáveis e generalizáveis.
Outro ponto relevante é a capacidade do modelo de exibir a importância das variáveis, permitindo visualizar quais atributos mais contribuem para a detecção de ataques. Por exemplo, o número de acessos de um mesmo IP pode indicar um ataque DoS, enquanto a variável flag pode ajudar a identificar tentativas de varredura de rede. Outras técnicas, como regressão logística, KNN ou redes neurais, foram consideradas, mas se mostraram menos adequadas: as primeiras por assumirem relações lineares ou apresentarem sensibilidade a ruídos, e as últimas por exigirem maior complexidade e poder computacional, fugindo do escopo do projeto. Assim, o Random Forest equilibra desempenho, interpretabilidade e simplicidade, sendo a escolha mais apropriada para o problema proposto.
A avaliação do modelo foi realizada utilizando a métrica principal F1-score, por ser a mais adequada em problemas com classes desbalanceadas, como neste caso, em que há muito mais conexões legítimas do que ataques. Essa métrica combina precisão (precision) e revocação (recall), permitindo mensurar o equilíbrio entre a capacidade do modelo de identificar ataques e de evitar falsos alarmes. Dessa forma, um valor elevado de F1-score indica que o modelo é eficiente na detecção de atividades maliciosas, sem comprometer a confiabilidade das previsões.

## Dados
- O link para os arquivos utilizados como dataset para esse modelo de IA/ML pode ser encontrado diretamente via Kaggle: [Link](https://www.kaggle.com/datasets/mostafaashraf1/nsl-kdd/data).
- OBS: é um dataset público, publicado pela Universidade de New Brunswick (UNB) através do projeto ISCX / CIC. [Link](https://www.unb.ca/cic/datasets/nsl.html)

## Instalação do Python

1. Verifique se o Python já está instalado:
```bash
python --version
ou
python3 --version
```
2. Caso não esteja instalado, baixe em:
```bash
https://www.python.org/downloads/
```
3. Durante a instalação no Windows, marque a opção:
```bash
"Add Python to PATH"
```
4. macOS: o Python pode ser instalado via Homebrew:
```bash
brew install python
```
5. Linux (Ubuntu/Debian):
```bash
sudo apt install python3
```
6. Após instalar, feche e reabra todos os terminais e confirme a instalação:
``` bash
python --version
(deve exibir algo como "Python 3.11.6")
```

## Execução

1. Clonar o repositório:
```bash
  git clone https://github.com/int16t/Anomalyzer.git
```
2. Acessar pasta do repositório
```bash
  cd Anomalyzer/
```
3. Ativar ambiente...
```bash
  python3 -m venv .venv
```

4. Instalar dependencias  
```bash
  .venv/bin/pip install -r requirements.txt
```

5. Executar o programa
```bash
  python3 src/principal.py
```

## Organização das pastas
```
  📂 Anomalyzer/
  .
  ├─ README.md
  ├─ requirements.txt
  ├── data/
  │   ├── NSL_KDD_Test.csv
  │   └── NSL_KDD_Train.csv
  ├── src/
  │   ├── utils.py
  │   ├── preprocessamento.py
  │   ├── treinamento.py
  │   ├── avaliacao.py
  │   └── principal.py
  ├── notebooks/
  │   └── arquivo.ipynb
  ├── models/
  │   └── arquivo.pkl
  ├─ reports/
  │  └── figures/
  └─ .gitignore
```
## Resultados do Projeto
Gráfico 1, intitulado como "Distribuição de Classes no Dataset de Teste", demonstra que há aproximadamente 13 mil registros de ataque e cerca de 9,7 mil registros normais. Este desbalanceamento leve ressalta a importância do uso de métricas como o F1-score, precision e recall, uma vez que a simples acurácia poderia mascarar erros relevantes de classificação. Além disso, a análise confirma que o dataset representa um cenário atípico do mundo real, porque na amostra utilizada para plotagem, os ataques aparecem em proporção maior que tráfegos legítimos

![Distribuição de Classes](https://github.com/int16t/Anomalyzer/blob/main/reports/figures/distribuicao-classes-teste.png)

---

O Gráfico 2 apresenta a Curva Precision-Recall do modelo. Observa-se que, à medida que a revocação aumenta, a precisão tende a diminuir, indicando que, embora o modelo seja capaz de detectar a maior parte dos ataques, isso ocorre ao custo de um número maior de falsos positivos. Esse comportamento é comum em classificadores aplicados à detecção de tráfego de rede, onde os padrões são altamente variáveis e ruidosos.
Nota-se também que a curva apresenta boa precisão até cerca de 0.6–0.7 de recall, sofrendo queda mais acentuada após esse ponto, o que sugere dificuldade do modelo em capturar os ataques mais sutis. No geral, o desempenho permanece consistente com o esperado para o tipo de problema e pode ser ajustado conforme o limiar de decisão desejado.

![Curva Precision Recall](https://github.com/int16t/Anomalyzer/blob/main/reports/figures/curva-precision-recall.png)

---
Gráfico 3 exibe a distribuição entre TP, TN, FP e FN de forma visual. O modelo atingiu uma alta quantidade de verdadeiros positivos e verdadeiros negativos, demonstrando boa capacidade de distinguir comportamento normal e malicioso. No entanto, nota-se um volume considerável de falsos negativos, casos em que um ataque foi classificado como normal. Esse aspecto explica o F1-score final de aproximadamente 0,81, considerado satisfatório, mas indicando necessidade de melhorias, especialmente para reduzir a taxa de falsos negativos, algo crítico em cenários reais de segurança.

![Barras Matriz Confusao](https://github.com/int16t/Anomalyzer/blob/main/reports/figures/barras-matriz-confusao.png)


# Anomalyzer (EN)
Machine Leaning Projeto focused on identifying anomalies in Network Traffic.

