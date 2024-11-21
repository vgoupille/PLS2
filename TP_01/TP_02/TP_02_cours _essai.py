# script pour le TP 2


for chrom, sub_gene in genes.items()
    if chrom in tfact: # si la clef est dans le dictionnaire tfact
        sub_fact = tfact[chrom] # alors on recupere la valeur de la clef
        for gene in sub_gene:
            for fact in sub_fact:
                print (chrom, gene, fact)
                
                


for chrom in genes: # parcours les clefs du dictionnaire genes
    print(chrom) #return la clef
    
for chrom in genes.keys(): 
    print(chrom) #return la clef

for chrom in genes.values():
    print(chrom) #return la valeur 

for chrom, sub_gene in genes.items():
    print(chrom) #return la valeur 
    print(sub_gene) #return la valeur

for chrom, sub_gene in genes.items():
    if chrom in tfact: # si la clef est dans le dictionnaire tfact
        sub_fact = tfact[chrom] # alors on recupere la valeur de la clef
        for gene in sub_gene:
            for fact in sub_fact:
                print(chrom, gene, fact)
                
                
with open("output.txt", "w", encoding= "utf-8") as file:             
    for chrom, sub_gene in genes.items():
        if chrom in tfact: # si la clef est dans le dictionnaire tfact
            sub_fact = tfact[chrom] # alors on recupere la valeur de la clef
            for gene, (start_gene, stop_gene) in sub_gene.items():
                for fact, (start_fact, stop_fact) in sub_fact.items():
                    d = distance(start_gene, stop_gene, start_fact, stop_fact)
                    if d < 500000:
                        print(gene, fact, d, sep="\t")
                        file.write(f"{chrom}\t{gene}\t{fact}\t{d}\n")    
