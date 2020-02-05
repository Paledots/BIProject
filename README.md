
Project goals and tasks
---
Search for epistatic gene interactions using coalescence methods and using the hidden Markov model. You can get such trees using ASMC methods, but first, you need to prepare the data for this method.
Tasks:
*  Modify the ASMC methodology for constructing “phylogenetic” trees at each locus of the genome.
*  To develop theoretical model for inferring coevolution from two coalescent trees.
*  Apply a model to search for coevolution in real data


Description of the used methods
---
The Ascertained Sequentially Markovian Coalescent is a method to efficiently estimate pairwise coalescence time along the genome. It can be run using SNP array or whole-genome sequencing (WGS) data.
The home repository for a project can be found here.

Running scripts
---
To run the ASMC method, the instruction can be found [here](https://github.com/pierpal/ASMC).

To get three files (.map, .haps / .hap, .sample) you need a vcf file with the original genotypes. To convert .vcf files to three files you need to do:

* python3 ./vcftoHap.py
  filename.vcf
      
  where filename.vcf is the source file with all genotypes, when the program runs, the asmc.haps file will be created in the current folder
      
*  python3 ./hapToMap.py
   filename.vcf
      
   where filename.haps / filename.hap is the .hap / haps file with all genotypes, when the program runs, the asmc.map file will be created in the current folder
      
*  python3 ./getSample.py
   N
      
   where N is the number of all genotypes, when the program runs, the asmc.sample file will be created in the current folder
 

Scripting requires python version at least 3.6

Source data of genotypes: [1000genomes project](https://www.internationalgenome.org/data#download),  [.map files](https://github.com/joepickrell/1000-genomes-genetic-maps)

An article describing the application of Hidden Markov Model and the ASMC approach can be found [here](https://www.nature.com/articles/s41588-018-0177-x)

