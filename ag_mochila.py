import random

# Representa um item a ser colocado na mochila, contendo seu valor e peso
class Item:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

# Solução candidata
class Individuo:
    def __init__(self, itens, capacidade, geracao=0):
        self.fitness = 0
        self.geracao = geracao
        # Cada cromossomo é uma lista de 0s e 1s, onde cada posição corresponde a um item, e 1 significa que o item foi selecionado para a mochila
        self.cromossomo = [random.choice([0, 1]) for _ in range(len(itens))]
        self.itens = itens
        self.capacidade = capacidade

    # Calcula o valor total dos itens selecionados
    def avaliacao(self):
        peso_total = 0
        valor_total = 0
        
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == 1:
                valor_total += self.itens[i].valor
                peso_total += self.itens[i].peso
        
        if peso_total > self.capacidade:
            self.fitness = 0  # Penaliza se ultrapassar a capacidade
        else:
            self.fitness = valor_total

    # Troca partes dos cromossomos
    def crossover(self, outro_individuo):
        ponto_corte = random.randint(0, len(self.cromossomo) - 1)
        
        filho1 = self.cromossomo[:ponto_corte] + outro_individuo.cromossomo[ponto_corte:]
        filho2 = outro_individuo.cromossomo[:ponto_corte] + self.cromossomo[ponto_corte:]

        filhos = [Individuo(self.itens, self.capacidade, self.geracao + 1),
                  Individuo(self.itens, self.capacidade, self.geracao + 1)]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        return filhos

    # Inverte um gene para mutação
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random.random() < taxa_mutacao:
                self.cromossomo[i] = 1 - self.cromossomo[i]  # Inverte o gene (0 para 1 ou 1 para 0)
        return self

class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao, itens, capacidade):
        self.tamanho_populacao = tamanho_populacao
        self.itens = itens
        self.capacidade = capacidade
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = None

    # Inicializa a população com os itens e a capacidade da mochila
    def inicializaPopulacao(self):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(self.itens, self.capacidade))

    #ordena a população com base no fitness
    def ordenaPop(self):
        self.populacao = sorted(self.populacao, key=lambda x: x.fitness, reverse=True)

    # soma o fitness de todos os indivíduos da população
    def somaFitness(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.fitness
        return soma

    # selecionar dois pais com maior probabilidade de serem bons indivíduos
    def selecionaPai(self, somaFitness):
        pai = -1
        valor_sorteado = random.random() * somaFitness
        soma = 0
        i = 0

        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].fitness
            pai += 1
            i += 1

        return pai

    # Imprimir informações da geração atual
    def visualizaGeracao(self):
        melhor = self.populacao[0]
        print(f"Geração: {melhor.geracao} - Fitness: {melhor.fitness} - Valor: {melhor.fitness} - Peso: {self.calcularPeso(melhor)}")

    # verifica o peso total dos itens selecionados
    def calcularPeso(self, individuo):
        peso_total = 0
        for i in range(len(individuo.cromossomo)):
            if individuo.cromossomo[i] == 1:
                peso_total += self.itens[i].peso
        return peso_total

    # Executa o algoritmo genético
    def resolver(self, taxa_mutacao, numero_geracoes):
        self.inicializaPopulacao() # inicializar

        for individuo in self.populacao:
            individuo.avaliacao() # avaliar cada indivíduo

        self.ordenaPop() # ordenar a população
        self.melhor_solucao = self.populacao[0] # armazenar a melhor solução

        self.visualizaGeracao() # imprimir os dados da geração atual

        for geracao in range(numero_geracoes):
            soma_avaliacao = self.somaFitness()
            nova_pop = []

            for individuo_gerado in range(0, self.tamanho_populacao, 2):
                pai1 = self.selecionaPai(soma_avaliacao)
                pai2 = self.selecionaPai(soma_avaliacao)

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                nova_pop.append(filhos[0].mutacao(taxa_mutacao))
                nova_pop.append(filhos[1].mutacao(taxa_mutacao))

            self.populacao = nova_pop

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordenaPop()
            self.visualizaGeracao()

            melhor_encontrada = self.populacao[0]
            self.melhor_solucao = melhor_encontrada

        print(f"Melhor solução encontrada -> Geração: {self.melhor_solucao.geracao} - Fitness: {self.melhor_solucao.fitness}")
        print(f"Valor total: {self.melhor_solucao.fitness}")
        print(f"Peso total: {self.calcularPeso(self.melhor_solucao)}")
        print(f"Itens selecionados: {[i for i in range(len(self.melhor_solucao.cromossomo)) if self.melhor_solucao.cromossomo[i] == 1]}")

if __name__ == "__main__":
    # Definir os itens (valor, peso)
    itens = [
        Item(60, 10),  # Item 1: Valor = 60, Peso = 10
        Item(100, 20), # Item 2: Valor = 100, Peso = 20
        Item(120, 30), # Item 3: Valor = 120, Peso = 30
    ]
    
    capacidade_mochila = 50
    taxa_mutacao = 0.01
    geracoes = 1000
    tam_pop = 100
    
    ag = AlgoritmoGenetico(tam_pop, itens, capacidade_mochila)
    ag.resolver(taxa_mutacao, geracoes)
