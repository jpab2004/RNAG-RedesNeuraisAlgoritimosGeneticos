import random
from collections import deque



##############################################################################################################
#                                                CAIXA BINÁRIA                                               #
##############################################################################################################



def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor zero ou um.
    '''
    #lista = [0, 1]
    #gene = random.choice(lista)
    #return gene
    
    return random.choice([0, 1])


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


def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo: lista contendo os genes das caixas binárias.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    '''
    return sum(individuo)


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



##############################################################################################################
#                                              CAIXA NÃO BINÁRIA                                             #
##############################################################################################################



def gene_cnb(valor_max_caixa):
    '''Gera um gene válido para o problema das caixas não-binárias.
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir.
    
    Returns:
        Um valor de 0 a 'valor_max_caixa' (incluso).
    '''
    gene = random.randint(0, valor_max_caixa)
    return gene


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


def funcao_objetivo_cnb(individuo):
    '''Calcula o fitness do individuo para o problema das caixas não-binárias
    
    Args:
        individuo: lista que representa um individuo dentro do problema das CNB
        
    Returns:
        Um valor que representa o fitness do individuo
    '''
    fitness = sum(individuo)
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



##############################################################################################################
#                                                    SENHA                                                   #
##############################################################################################################



def gene_letra(letras):
    '''Sorteia uma letra para o problema da senha.

    Args:
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Uma letra dentro das possíveis a serem sorteadas.
    '''
    return random.choice(letras)


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
#                                              CAIXEIRO VIAJANTE                                             #
##############################################################################################################



def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    indice1, indice2 = random.sample(indices, k=2)

    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]

    return individuo


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    individuo_copy = deque(individuo)
    individuo_copy.rotate(-1)

    for ini, che in zip(individuo, individuo_copy):
        inicio = cidades[ini]
        chegada = cidades[che]

        distancia += distancia_entre_dois_pontos(inicio, chegada)
    
    return distancia


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado



##############################################################################################################
#                                             PROBLEMA DA MOCHILA                                            #
##############################################################################################################



def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """
    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila


def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado



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


def selecao_torneio_max(populacao, fitness, tamanho_torneio):
    '''Faz a seleção de uma população usando torneio.

        Nota: da forma que está implementada, só funciona em problemas de maximização.
    
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

        melhor_fit = -float('inf')

        for individuo, fit in combatentes:
            if fit > melhor_fit:
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


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)

    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)

    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)

    return filho1, filho2



##############################################################################################################
#                                                   SUPORTE                                                  #
##############################################################################################################



def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist



def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """
    valor_total = 0
    peso_total = 0

    for pegou_o_itenm_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_itenm_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]['valor']
            peso_do_item = objetos[nome_do_item]['peso']

            valor_total += valor_do_item
            peso_total += peso_do_item

    return valor_total, peso_total



##############################################################################################################
#                                       SENHA DE TAMANHO VARIÁVEL                                            #
##############################################################################################################


def gene_sv(letras):
    '''Sorteia uma letra para o problema da senha de tamanho variável.

    Args:
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Uma letra dentro das possíveis a serem sorteadas.
    '''
    return random.choice(letras)


def individuo_sv(tamanho_max, letras):
    '''Cria um individuo para o problema da senha variável.

    Args:
        tamanho_max: tamanho máximo que a senha pode assumir;
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Uma lista que representa o individuo.
    '''
    tamanho_individuo = random.randint(3,tamanho_max)
    individuo = []
    for _ in range(tamanho_individuo):
        individuo.append(gene_sv(letras))
    return individuo


def pop_inicial_sv(num_individuos, tamanho_max, letras):
    '''Cria uma população para o problema da senha variável.

    Args:
        num_individuos: número de individuos da população;
        tamanho_max: tamanho máximo que a senha pode assumir;
        letras: possíveis letras a serem sorteadas.
    
    Returns:
        Uma lista que contem todos os individuos.
    '''
    pop = []
    for _ in range(num_individuos):
        pop.append(individuo_sv(tamanho_max, letras))
    return pop


def obj_sv(individuo, senha_verdadeira, peso_da_penalidade):
    '''Computa a funcao objetivo de um individuo no problema da senha.

    Args:
        individiuo: lista contendo as letras da senha;
        senha_verdadeira: a senha que você está tentando descobrir;
        peso_da_penalidade: peso para a diferenca de tamanho entre o individuo e a senha real.

    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    '''
    dif = 0

    for letra_ind, letra_ver in zip(individuo, senha_verdadeira):
        dif += abs(ord(letra_ind) - ord(letra_ver))
    
    diferenca_tamanho = abs(len(individuo) - len(senha_verdadeira))
    dif += peso_da_penalidade * diferenca_tamanho

    return dif


def obj_pop_sv(populacao, senha_verdadeira, peso_da_penalidade):
    '''Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
        populacao: lista com todos os individuos da população;
        senha_verdadeira: a senha que você está tentando descobrir;
        peso_da_penalidade: peso para a diferenca de tamanho entre o individuo e a senha real.
    
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    '''
    fitness = []

    for individuo in populacao:
        fitness.append(obj_sv(individuo, senha_verdadeira, peso_da_penalidade))

    return fitness


def selecao_torneio_senha_sv(populacao, fitness, tamanho_torneio):
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


def cruzamento_ponto_simples_sv(pai, mae):
    '''Operador de cruzamento de ponto simples para o problema da senha variável.
    
    Args:
        pai: Uma lista representando um individuo;
        mae: Uma lista representando um individuo.
    
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    '''
    if len(pai) < len(mae):
        ponto_de_corte = random.randint(1, len(pai) - 1)
    else:
        ponto_de_corte = random.randint(1, len(mae) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def mutacao_senha_sv(individuo, letras, tamanho_max):
    '''Realiza a mutação de um gene no problema da senha variável.

    Args:
        individuo: uma lista representado um individuo no problema da senha;
        letras: letras possíveis de serem sorteadas;
        tamanho_max: tamanho máximo que a senha pode assumir.

    Return:
        Um individuo (senha variável) com um gene mutado.
    '''
    if random.random() < .5:
        gene = random.randint(0, len(individuo) - 1)
        individuo[gene] = gene_sv(letras)
        return individuo
    else:
        novo_tamanho = random.randint(3, tamanho_max)
        if novo_tamanho < len(individuo):
            return individuo[:novo_tamanho]
        else:
            for _ in range(novo_tamanho - len(individuo)):
                individuo.append(gene_sv(letras))
            return individuo




##############################################################################################################
#                     CAIXEIRO VIAJANTE COM GASOLINA INFINITA (E SEM CONSCIÊNCIA AMBIENTAL)                  #
##############################################################################################################



def individuo_cv_gasolina_inf(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante com gasolina infinita.
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes


def populacao_inicial_cv_gasolina_inf(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante com gasolina infinita.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def mutacao_de_troca_gasolina_inf(individuo):
    """Troca o valor de dois genes para o problema do caixeiro viajante com gasolina infinita.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    indice1, indice2 = random.sample(indices, k=2)

    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]

    return individuo


def funcao_objetivo_cv_gasolina_inf(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante com gasolina infinita.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    individuo_copy = deque(individuo)
    individuo_copy.rotate(-1)

    for ini, che in zip(individuo, individuo_copy):
        inicio = cidades[ini]
        chegada = cidades[che]

        distancia += distancia_entre_dois_pontos(inicio, chegada)
    
    return distancia


def funcao_objetivo_pop_cv_gasolina_inf(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante com gasolina infinita.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado



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