gene1 = "TATGCTAGTATGCACCT"
gene2 = "TAGTCGTCAATCCGATT"
gene3 = "GAATTTAGTACGTCAAC"
gene4 = "TAGTAGGGATCGATCCA"

padrao = "TAGTATGC"

genes = [gene1, gene2, gene3, gene4]

def conta_diferencas(janela,padrao):
    diferencas = 0 
    for base1, base2 in zip(janela,padrao):
        if (base1 != base2):
            diferencas += 1
    return diferencas

def procura_padrao(genes, padrao, x):
      tamanho_do_padrao = len(padrao)
      gene_id = 0

      for gene in genes:
        gene_id += 1
        tamanho_genes = len(gene)

        for pos in range(tamanho_genes - tamanho_do_padrao + 1):
            janela = gene[pos:pos+tamanho_do_padrao]
            diferencas = conta_diferencas(janela, padrao)
            if diferencas <= x:
                print(f"Gene {gene_id} - > {janela}")
                print(f"Padrçao - > {padrao}")
                print(f"Diferenças - > {diferencas}")
                print(f"Localização no gene: {pos} - {pos+tamanho_do_padrao}/n")

