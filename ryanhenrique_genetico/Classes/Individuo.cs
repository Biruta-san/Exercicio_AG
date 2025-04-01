using System.Collections.Generic;
using System;

/*
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
*/

public class Individuo
{
    /// <summary>
    /// Fitness, o quanto o individuo é bom
    /// </summary>
    public int Fitness { get; set; }

    /// <summary>
    /// Número da geração
    /// </summary>
    public int Geracao { get; set; }

    /// <summary>
    /// Lista de itens da solução canditata
    /// </summary>
    public List<Item> Itens { get; set; }

    /// <summary>
    /// Cromossomo, lista de 0s e 1s, onde cada posição corresponde a um item, e 1 significa que o item foi selecionado para a mochila
    /// </summary>
    public List<bool> Cromossomos { get; set; }

    /// <summary>
    /// Capacidade da mochila
    /// </summary>
    public int Capacidade { get; set; }

    private var Rand = new Random();

    public Individuo(List<Item> itens, int capacidade, int geracao = 0)
    {
        Fitness = 0;
        Geracao = geracao;
        Cromossomos = new List<int>();
        Itens = itens;
        Capacidade = capacidade;

        foreach (var _ in Itens)
        {
            Cromossomos.Add(new Rand.Next(2) == 1); // Inicializa o cromossomo com 0s e 1s aleatórios
        }
    }

    /// <summary>
    /// Realiza avaliação do individuo
    /// </summary>
    public void Avaliacao()
    {
        int pesoTotal = 0;
        int valorTotal = 0;

        // Calcula o valor total dos itens selecionados
        for (int i = 0; i < Cromossomos.Count; i++)
        {
            if (Cromossomos[i])
            {
                valorTotal += Itens[i].Valor;
                pesoTotal += Itens[i].Peso;
            }
        }

        if (pesoTotal > Capacidade)
            Fitness = 0; // Penaliza se ultrapassar a capacidade
        else
            Fitness = valorTotal;
    }

    /*
    def crossover(self, outro_individuo):
        ponto_corte = random.randint(0, len(self.cromossomo) - 1)
        
        filho1 = self.cromossomo[:ponto_corte] + outro_individuo.cromossomo[ponto_corte:]
        filho2 = outro_individuo.cromossomo[:ponto_corte] + self.cromossomo[ponto_corte:]

        filhos = [Individuo(self.itens, self.capacidade, self.geracao + 1),
                  Individuo(self.itens, self.capacidade, self.geracao + 1)]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        return filhos*/

    public List<Individuo> Crossover(Individuo outroIndivido)
    {
        int pontoCorte = Rand.Next(0, Cromossomos.Count - 1); // Ponto de corte aleatório
        #region Filhos
        var filho1 = new List<bool>(Cromossomos.GetRange(0, pontoCorte));
        filho1.AddRange(
            outroIndivido.Cromossomos.GetRange(
                pontoCorte, outroIndivido.Cromossomos.Count - pontoCorte
            )
        );

        var filho2 = new List<bool>(
            Cromossomos.GetRange(
                pontoCorte, outroIndivido.Cromossomos.Count - pontoCorte
            ));
        filho2.AddRange(Cromossomos.GetRange(0, pontoCorte));
        #endregion

        // Inicializar novos individuos
        var filhos = new List<Individuo> {
            new Individuo(Itens, Capacidade, Geracao + 1),
            new Individuo(Itens, Capacidade, Geracao + 1)
        }

        // Atribuir os cromossomos dos filhos
        filhos[0].Cromossomos = filho1;
        filhos[1].Cromossomos = filho2;

        return filhos;
    }

}