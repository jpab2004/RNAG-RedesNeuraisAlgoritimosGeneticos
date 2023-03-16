import random


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


def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo: lista contendo os genes das caixas binárias.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    '''
    return sum(individuo)


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