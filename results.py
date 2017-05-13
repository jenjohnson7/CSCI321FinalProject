""" Jen Johnson
CSCI 321 Spring 17 Final Project
Comparing contigs of Salmonella genome using single and paired reads """

from PairedReadsGenomeToContigs import genome_to_paired_contigs
from SingleReadsGenomeToContigs import genome_to_single_contigs

def main():

    filename = "SampleGenome.txt"

    k = 3
    d = 1

    print("k " + str(k))
    print("d " + str(d))

    paired_contigs = genome_to_paired_contigs(k, d, filename)

    print("num paired contigs " + str(len(paired_contigs)))
    for result in paired_contigs:
        print(len(result))

    single_contigs = genome_to_single_contigs(k, filename)

    print("num single contigs " + str(len(single_contigs)))
    for result in single_contigs:
        print(len(result))

if __name__ == "__main__":
    main()
