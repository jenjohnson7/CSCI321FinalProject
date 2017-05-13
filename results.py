""" Jen Johnson
CSCI 321 Spring 17 Final Project
Comparing contigs of Salmonella genome using single and paired reads """

from PairedReadsGenomeToContigs import genome_to_paired_contigs
from SingleReadsGenomeToContigs import genome_to_single_contigs
from numpy import mean

def main():

    filename = "data/Salmonella1-20.txt"

    k = 100
    d = 50

    print("k " + str(k))
    print("d " + str(d))

    paired_paths = genome_to_paired_contigs(k, d, filename)

    paired_contigs = []

    for path in paired_paths:
        paired_contigs.append(len(path))

    print("num paired contigs " + str(len(paired_contigs)))
    avg = mean(paired_contigs)
    print("avg len paired contig " + str(avg))

    single_paths = genome_to_single_contigs(k, filename)

    single_contigs = []

    for path in single_paths:
        single_contigs.append(len(path))
    print("num single contigs " + str(len(single_contigs)))
    avg = sum(single_contigs)/len(single_contigs)
    print("avg len single contig " + str(avg))

if __name__ == "__main__":
    main()
