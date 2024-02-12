from genetic.genetic.gene import Gene


class Chromosome:

    def __init__(self, genes: list[Gene] = None) -> None:

        self.genes = genes

    def get_genes(self) -> list[Gene]:

        return self.genes

    def set_genes(self, genes: list[Gene]) -> None:

        self.genes = genes

    def get_gene(self, index: int) -> Gene:

        return self.genes[index]

    def set_gene(self, index: int, gene: Gene) -> None:

        self.genes[index] = gene

    def add_gene(self, gene: Gene) -> None:

        self.genes.append(gene)

    def remove_gene(self, index: int) -> None:

        self.genes.pop(index)

    def get_cromossom_size(self) -> int:

        return len(self.genes)

    # str and repr for this cromossom
    def __str__(self):
        return f"Genes: {self.genes}"

    def __repr__(self):
        return f"Genes: {self.genes}"

    def __eq__(self, other):
        if not isinstance(other, Chromosome):
            return NotImplemented
        return self.genes == other.genes
