# Sorting objects any way you like it #

## Learning outcomes ##
* getting to know Java Collection types, in particular ArrayList
* getting to know Java sorting methods


## Assignment details ##
In this package you will find class `Protein`. 
This class models Protein properties: name, accession number, Gene Ontology (GO) annotation, and amino acid sequence.
Note that the properties of instances of this class are _read only_. They are set at construction and cannot be changed
 from the outside. This is quite relevant for some aspects of this assignment.

**Part 1**
Class Protein declares it `implements Comparable<Protein>`. You need to implement the method stub of the corresponding method `compareTo(Protein other)` to support _natural order_ according to Protein name. 

**Part 2**
Besides class `Protein` there is the Java enum `SortingType` which defines the possible ways Protein objects may be sorted. 
Enums are discussed later; for now consider them as a fixed set of possible values for a particular property.  

The static factory method `getSorter()` that is defined in class `Protein` should serve a Comparator instance for each 
SortingType:

```java
/**
 * Serves sorters based on the type that is requested.
 * @param type
 * @return proteinSorter
 */
public static Comparator<Protein> getSorter(SortingType type) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
}
```  

These implementations are expected for each of the possible SortingTypes:

1. `SortingType.PROTEIN_NAME` -- a simple alphabetical sort, ascending (same as 'natural order' in `compareTo()`)
2. `SortingType.ACCESSION_NUMBER` -- a **case insensitive** alphabetical sort on accession number, ascending. 
3. `SortingType.GO_ANNOTATION` -- a multilevel sort on Gene Ontology properties. 
Sorting on GO annotation should be primary on biological process, secondary on cellular component and lastly on molecular 
function; all alphabetically (ascending).
4. `SortingType.PROTEN_WEIGHT` -- sort on the molecular weight of the amino acid sequence, descending.
For amino acid weights you should use the weights listed on [WebQC](http://www.webqc.org/aminoacids.php). 
It is essential you use these exact weights! Note: You will probably want to implement the method `getMolecularWeight()` 
in class Protein if you want to support sorting on molecular weight and should **_cache_** the protein weight within this class!


For this assignment, you may **NOT** assume all amino acid sequence strings provided to the constructor are legal
amino acid DNA sequences containing only regular amino acid characters. 
Also, do **NOT** assume only uppercase characters!
When constructing Protein objects, perform the necessary checks on the given arguments and throw 
an `IllegalArgumentException` if there is anything dodgy going on.  
 
For this purpose, you can apply the rule that amino acid sequence should contain only the twenty regular amino acid characters.

**Part 3: Challenge aspects**  

- Think carefully about the way to couple SortingType to the actual Comparator implementation. Ask yourself this: 
who (which class) should be responsible for creating and serving a Comparator object?
- Can you implement the interface `ProteinDataSource` to read from actual textual data? There is a text representation
of the same data here: `data/proteins.fa`

See these snippets for an example usage and result.

```Java
ProteinDataSource proteinDataSource = new ProteinDataSourceInMemory();
List<Protein> proteins = proteinDataSource.getAllProteins();

//sort in Protein-standard manner
Collections.sort(proteins);

//print the Java 8 way
proteins.stream().forEach(System.out::println);
```
Outputs:

```
Protein{name=60s ribosomal protein l35 pthr13872, accession=Stt3a, aminoAcidSequence=MTDDLVLAW}
Protein{name=fucosyltransferase 8 (alpha (1,6) fucosyltransferase), accession=Fut8, aminoAcidSequence=MGTHIILVLM}
Protein{name=mannosidase alpha, accession=man1b1a, aminoAcidSequence=MRTVALL}
Protein{name=synovial apoptosis inhibitor 1, synoviolin, accession=Syvn1, aminoAcidSequence=MTYIILLVCDERT}
Protein{name=tumor suppressor candidate 3, accession=Tusc3, aminoAcidSequence=MQSVNKLI}
```

and this

```Java
Collections.sort(proteins, Protein.getSorter(SortingType.ACCESSION_NUMBER));

proteins.stream().forEach(System.out::println);
```
Outputs:

```
Protein{name=fucosyltransferase 8 (alpha (1,6) fucosyltransferase), accession=Fut8, aminoAcidSequence=MGTHIILVLM}
Protein{name=mannosidase alpha, accession=man1b1a, aminoAcidSequence=MRTVALL}
Protein{name=60s ribosomal protein l35 pthr13872, accession=Stt3a, aminoAcidSequence=MTDDLVLAW}
Protein{name=synovial apoptosis inhibitor 1, synoviolin, accession=Syvn1, aminoAcidSequence=MTYIILLVCDERT}
Protein{name=tumor suppressor candidate 3, accession=Tusc3, aminoAcidSequence=MQSVNKLI}
```

and this

```Java
Collections.sort(proteins, Protein.getSorter(SortingType.PROTEIN_WEIGHT));

proteins.stream().forEach(System.out::println);
```
Outputs:

```
Protein{name=synovial apoptosis inhibitor 1, synoviolin, accession=Syvn1, aminoAcidSequence=MTYIILLVCDERT} //1569.89 
Protein{name=fucosyltransferase 8 (alpha (1,6) fucosyltransferase), accession=Fut8, aminoAcidSequence=MGTHIILVLM} //1127.47
Protein{name=60s ribosomal protein l35 pthr13872, accession=Stt3a, aminoAcidSequence=MTDDLVLAW} //1063.23 
Protein{name=tumor suppressor candidate 3, accession=Tusc3, aminoAcidSequence=MQSVNKLI} //932.15
Protein{name=mannosidase alpha, accession=man1b1a, aminoAcidSequence=MRTVALL} //803.03
```

and lastly, this

```Java
Collections.sort(proteins, Protein.getSorter(SortingType.GO_ANNOTATION));
//first on biological process (3), then on cellular component (1) and last on molecular function (2)
proteins.stream().forEach(System.out::println);
```
Outputs:

```
Protein{name=synovial apoptosis inhibitor 1, synoviolin, accession=Syvn1, ...} //GOannotation(13259, "cytoplasmatic", "synoviolin-related", "bacterium-cycle regulation")
Protein{name=tumor suppressor candidate 3, accession=Tusc3, ...} //GOannotation(18269, "mitochondrial", "dolichyl-diphosphooligosaccharide--protein glycosyltransferase", "bacterium-cycle regulation")
Protein{name=mannosidase alpha, accession=man1b1a, ...} //GOannotation(15923, "cytoplasmatic", "beta-6-sulfate-N-acetylglucosaminidase activity", "sugar metabolism")
Protein{name=fucosyltransferase 8 (alpha (1,6) fucosyltransferase), accession=Fut8, ...} //GOannotation(342989, "cytoplasmatic", "fucosyltransferase activity", "sugar metabolism")
Protein{name=60s ribosomal protein l35 pthr13872, accession=Stt3a, ...} //GOannotation(18279, "membrane inserted", "protein N-linked glycosylation via asparagine", "sugar metabolism")
```
