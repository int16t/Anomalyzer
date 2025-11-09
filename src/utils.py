def centralizar(conteudo, largura=60, preenchimento=' '):
    """
    Centraliza qualquer texto na largura especificada.
    
    Parâmetros:
    - conteudo: O texto a ser centralizado
    - largura: Largura total da linha (padrão: 60)
    - preenchimento: Caractere de preenchimento (padrão: espaço)
    """
    return conteudo.center(largura, preenchimento)

def linha(caractere='-', largura=60):
    """
    Gera uma linha composta por um caractere repetido.
    
    Parâmetros:
    - caractere: O caractere a ser repetido (padrão: '-')
    - largura: Largura total da linha (padrão: 60)
    """
    print(caractere * largura)

def titulo():
    """
    Exibe o título do Anomalyzer.
    """

    print("""
________  ________   ________  _____ ______   ________  ___           ___    ___ ________  _______   ________     
│╲   __  ╲│╲   ___  ╲│╲   __  ╲│╲   _ ╲  _   ╲│╲   __  ╲│╲  ╲         │╲ ╲  ╱  ╱│╲_____  ╲│╲  ___ ╲ │╲   __  ╲    
╲ ╲  ╲│╲  ╲ ╲  ╲╲ ╲  ╲ ╲  ╲│╲  ╲ ╲  ╲╲╲__╲ ╲  ╲ ╲  ╲│╲  ╲ ╲  ╲        ╲ ╲ ╲╱  ╱ ╱╲│___╱  ╱╲ ╲   __╱│╲ ╲  ╲│╲  ╲   
 ╲ ╲   __  ╲ ╲  ╲╲ ╲  ╲ ╲  ╲╲╲  ╲ ╲  ╲╲│__│ ╲  ╲ ╲   __  ╲ ╲  ╲        ╲ ╲   ╱ ╱     ╱  ╱ ╱╲ ╲  ╲_│╱_╲ ╲   _  _╲  
  ╲ ╲  ╲ ╲  ╲ ╲  ╲╲ ╲  ╲ ╲  ╲╲╲  ╲ ╲  ╲    ╲ ╲  ╲ ╲  ╲ ╲  ╲ ╲  ╲____    ╲╱  ╱ ╱     ╱  ╱_╱__╲ ╲  ╲_│╲ ╲ ╲  ╲╲  ╲│ 
   ╲ ╲__╲ ╲__╲ ╲__╲╲ ╲__╲ ╲_______╲ ╲__╲    ╲ ╲__╲ ╲__╲ ╲__╲ ╲_______╲__╱  ╱ ╱     │╲________╲ ╲_______╲ ╲__╲╲ _╲ 
    ╲│__│╲│__│╲│__│ ╲│__│╲│_______│╲│__│     ╲│__│╲│__│╲│__│╲│_______│╲___╱ ╱       ╲│_______│╲│_______│╲│__│╲│__│
                                                                     ╲│___│╱                                       
                                                                                                                   
                                                                                                                   ANOMALYZER - DETECTOR DE ANOMALIAS NA REDE""")
    
def plataforma():
    """
    Verifica a plataforma do Anomalyzer.
    """
    import platform
    sistema = platform.system()
    if sistema == 'Windows':
        return 'Windows'
    elif sistema == 'Linux':
        return 'Linux'
    else:
        return 'Desconhecido'