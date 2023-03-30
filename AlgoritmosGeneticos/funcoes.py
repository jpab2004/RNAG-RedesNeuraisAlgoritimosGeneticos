import random



##############################################################################################################
#                                                   GENES                                                    #
##############################################################################################################s



def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor zero ou um.
    '''
    #lista = [0, 1]
    #gene = random.choice(lista)
    #return gene
    
    return random.choice([0, 1])


def gene_cnb(valor_max_caixa):
    '''Gera um gene válido para o problema das caixas não-binárias.
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir.
    
    Returns:
        Um valor de 0 a 'valor_max_caixa' (incluso).
    '''
    gene = random.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    '''Sorteia uma letra para o problema da senha.

    Args:
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Uma letra dentro das possíveis a serem sorteadas.
    '''
    return random.choice(letras)



##############################################################################################################
#                                                 INDIVIDUOS                                                 #
##############################################################################################################



def individuo_cb(n):
    '''Gera um individuo para o problema das caixas binárias.
    
    Args:
        n: número de genes do indivíduo.
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    '''
    #individuo = []
    #for i in range(n):
    #    gene = gene_cb()
    #    individuo.append(gene)
    #return gene

    return [gene_cb() for i in range(n)]


def individuo_cnb(numero_genes, valor_max_caixa):
    '''Gera um individuo válido para o problema das caixas não binárias.
    
    Args:
        numero_genes: número de genes na lista que representa o individuo;
        valor_max_caixa: Valor máximo que a caixa pode assumir.
    
    Returns:
        Uma lista que representa um individuo válido para o problema das CNB.
    '''
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def individuo_senha(tamanho_senha, letras):
    '''Cria um candidato válido para o problema da senha.

    Args:
        tamanho_senha: int com o tamanho da senha a ser acertada;
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Lista com 'tamanho_senha' letras que representa o individuo.
    '''
    individuo = []

    for _ in range(tamanho_senha):
        individuo.append(gene_letra(letras))
    
    return individuo



##############################################################################################################
#                                            POPULAÇÃO INICIAL                                               #
##############################################################################################################



def populacao_cb(tamanho, n):
    '''Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho: tamanho da população;
        n: número de genes de um individuo.
    
    Returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def populacao_cnb(tamanho_populacao,numero_genes,valor_max_caixa):
    '''Cria uma populacao de individuos para o problema das caixas não-binárias.
    
    Args:
        tamanho_populacao: número de individuos da populacao;
        numero_genes: número de genes do individuo;
        valor_max_caixa: valor maximo que a caixa pode assumir.
    
    Returns:
        uma lista onde cada item representa um individuo.
    '''
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    '''Cria uma população inicial para o problema das senhas.

    Args:
        tamanho: tamanho da população;
        tamanho_senha: int com o tamanho da senha a ser acertada;
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Lista, onde cada item é um individuo da população.
    '''
    populacao = []

    for _ in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    
    return populacao



##############################################################################################################
#                                                  SELEÇÃO                                                   #
##############################################################################################################



def selecao_roleta_max(populacao, fitness):
    '''Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        populacao: lista com todos os individuos da população;
        fitness: lista com o valor da função objetivo dos individuos da população.
    
    Returns:
        População dos individuos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    '''Faz a seleção de uma população usando torneio.

        Nota: da forma que está implementada, só funciona em problemas de minimização.
    
    Args:
        populacao: população do problema;
        fitness: lista com os valores de fitness de cada individuo;
        tamanho_torneio: quantidade de invidiuos que batalham entre si.

    Returns:
        Individuos selecionados. Lista com os individuos selecionados com mesmo tamanho do argumento 'populacao'.
    '''
    selecionados = []

    par_populacao_fitness = list(zip(populacao, fitness))

    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        melhor_fit = float('inf')

        for individuo, fit in combatentes:
            if fit < melhor_fit:
                selecionado = individuo
                melhor_fit = fit
        
        selecionados.append(selecionado)
    
    return selecionados



##############################################################################################################
#                                                CRUZAMENTO                                                  #
##############################################################################################################



def cruzamento_ponto_simples(pai, mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
        pai: Uma lista representando um individuo;
        mae: Uma lista representando um individuo.
    
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    '''
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2



##############################################################################################################
#                                                 MUTAÇÃO                                                    #
##############################################################################################################



def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias.
    
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias.

    Returns:
        Um individuo com um gene mutado.
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    '''Realiza a mutação do individuo
    
    Args:
        individuo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
    
    Returns:
        individuo que sofreu a mutação
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def mutacao_senha(individuo, letras):
    '''Realiza a mutação de um gene no problema da senha.

    Args:
        individuo: uma lista representado um individuo no problema da senha;
        letras: letras possíveis de serem sorteadas.

    Return:
        Um individuo (senha) com um gene mutado.
    '''
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo



##############################################################################################################
#                                               FUNÇÃO OBJETIVO                                              #
##############################################################################################################



def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo: lista contendo os genes das caixas binárias.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    '''
    return sum(individuo)


def funcao_objetivo_cnb(individuo):
    '''Calcula o fitness do individuo para o problema das caixas não-binárias
    
    Args:
        individuo: lista que representa um individuo dentro do problema das CNB
        
    Returns:
        Um valor que representa o fitness do individuo
    '''
    fitness = sum(individuo)
    return fitness


def funcao_objetivo_senha(individuo, senha_verdadeira):
    '''Computa a funcao objetivo de um individuo no problema da senha.

    Args:
        individiuo: lista contendo as letras da senha;
        senha_verdadeira: a senha que você está tentando descobrir.

    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    '''
    dif = 0

    for letra_ind, letra_ver in zip(individuo, senha_verdadeira):
        dif += abs(ord(letra_ind) - ord(letra_ver))
    
    return dif



##############################################################################################################
#                                      FUNÇÃO OBJETIVO DA POPULAÇÃO                                          #
##############################################################################################################



def funcao_objetivo_pop_cb(populacao):
    '''Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        populacao: lista com todos os individuos da população.
    
    Returns:
        Lista de valores representando a fitness de cada individuo da população.
    '''
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    '''Calcula o fitness da população completa
    
    Args:
        populacao: lista com todos os individuos da população
    
    Returns:
        Uma lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    '''Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
        populacao: lista com todos os individuos da população;
        senha_verdadeira: a senha que você está tentando descobrir.
    
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    '''
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return fitness



##############################################################################################################
#                                              MINHAS FUNÇÕES                                                #
##############################################################################################################



def melhor_outcome_cb(individuos):
    '''Encotra o melhor indivíduo encontrado a partir da lista de indivíduos passados.
    
    Args:
        individuos: dicionário com os individuos e seus valores de objetivo para calcular o melhor encontrado.
    
    Return:
        O melhor individuo encontrado dentre os presentes no dicionário passado.
    '''
    best = {'melhor': [[0,0,0,0], -1]}
    for key in individuos:
        if individuos[key][1] > best['melhor'][1]:
            best['melhor'] = individuos[key]
    return best