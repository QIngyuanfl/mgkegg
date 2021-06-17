## Kegg color pathway object for metagenome

Command line version for [KEGG Pathway obejct](https://www.genome.jp/kegg/tool/map_pathway2.html) and [KEGG rest api](https://www.kegg.jp/kegg/rest/keggapi.html)



### installation

```sh
pip install mgkegg
```

#### Usage

1. Display database release information and linked db information

   ```sh
   mgkegg info <dbentries>
   # displays the current statistics of the KEGG database
   mgkegg info kegg
   # displays the number of pathway entries including both the reference and organism-specific pathways
   mgkegg info pathway
   # displays the number of gene entries for the KEGG organism Homo sapiens
   mgkegg info hsa
   ```

2.  Obtain a list of entry identifiers and associated definition

   ```sh
   mgkegg ls <dbentries>
   # returns the list of reference pathways
   mgkegg ls pathway
   # returns the list of human pathways
   mgkegg ls pathway hsa
   # returns the list of KEGG organisms with taxonomic classification
   mgkegg ls organism
   # returns the entire list of human genes
   mgkegg ls hsa
   # returns the list of a human gene and an E.coli O157 gene
   mgkegg ls hsa:10458+ece:Z5100
   # returns the list of a compound entry and a glycan entry
   mgkegg ls cpd:C01290+gl:G00092
   ```

3. Find entries with matching query keyword or other query data

   ```sh
   mgkegg find <databases> <query>
   # for keywords "shiga" and "toxin" (use nop option to disable this processing)
   mgkegg find genes shiga+toxin
   # for keywords "shiga toxin"
   mgkegg find genes shiga toxin
   # for chemical formula "C7H10O5"
   mgkegg find compound C7H10O5 formula
   # for chemical formula containing "O5" and "C7"
   mgkegg find compound O5C7 formula
   # for 174.045 =< exact mass < 174.055
   mgkegg find 174.05 exact_mass
   # for 300 =< molecular weight =< 310
   mgkegg find 300-310 mol_weight
   ```
   
4. Retrieve given database entries

   ```sh
   mgkegg get <dbentries>
   # retrieves a compound entry and a glycan entry
   mgkegg get cpd:C01290+gl:G00092
   # retrieves a human gene entry and an E.coli O157 gene entry
   mgkegg get hsa:10458+ece:Z5100
   # retrieves amino acid sequences of a human gene and an E.coli O157 gene
   mgkegg get hsa:10458+ece:Z5100 aaseq
   # retrieves the gif image file of a compound
   mgkegg get C00002 image
   # retrieves the png image file of a pathway map
   mgkegg get hsa05130 image
   # retrieves the conf file of a pathway map
   mgkegg get hsa05130 conf
   # retrieves the kgml file of a pathway map
   mgkegg get hsa05130 kgml
   # retrieves the htext file of a brite hierarchy
   mgkegg get br:br08301
   # retrieves the json file of a brite hierarchy
   mgkegg get br:br08301 json
   ```

5. Download the latest kegg reference map.

   ```sh
   mgkegg download
   ```

6. Update to the latest kegg reference map if not already the lastet.

   ```sh
   mgkegg update
   ```

7. Highlight the given kegg object with the given color offline.

   ``` sh
   mgkegg highlight --glist <gene.list> --color <color> -o <outdir>
   ```



