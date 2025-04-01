/// <summary>
/// Representa um item que será colocado na mochila
/// </summary>
public class Item
{
    /// <summary>
    /// Valor do item
    /// </summary>
    public int Valor { get; set; }

    /// <summary>
    /// Peso do item
    /// </summary>
    public int Peso { get; set; }

    /// <summary>
    /// Inicializar o item
    /// </summary>
    /// <param name="valor">Valor do item</param>
    /// <param name="peso">Peso do Item</param>
    public Item(int valor, int peso)
    {
        Valor = valor;
        Peso = peso;
    }
}