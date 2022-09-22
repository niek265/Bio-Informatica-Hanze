# Challenging Exercise

## Learning outcomes
* implementing algorithmic logic

## Assignment: Creating a consensus sequence  

Implement a method that will determine the consensus of a given set of sequences (of the same length).
The input sequences are provided as an Array of Strings.
For this assignment, you may assume all DNA strings provided are legal DNA sequences containing ONLY G, A, T or C characters,  in uppercase.

The consensus sequence can be created in two ways, specified by the second argument to the method.
If the iupac flag is set to true, IUPAC-type encoding will be used, else a bracket-type notation should be used.
With bracket notation, the nucleotides should be ordered alphabetically! So this is wrong: "GA[A/T/C]" and this is right: "GA[A/C/T]"

IUPAC encoding is explained [here](http://en.wikipedia.org/wiki/Nucleic_acid_notation)

See this snippet for an example usage and result:

```Java
String[] sequences = new String[4];
sequences[0] = "GAAT";
sequences[1] = "GAAA";
sequences[2] = "GATT";
sequences[3] = "GAAC";
ConsensusSequenceCreator csc = new ConsensusSequenceCreator();
String consensus = csc.createConsensus(sequences, true);
//consensus should equal "GAWH"
consensus = csc.createConsensus(sequences, false);
//consensus should equal "GA[A/T][A/C/T]"
``` 

**NOTE: this problem can be solved in many ways, some hard and some easy -- so think before you start!**

- *Tip 1*: use String.join("+", sequences) to join array elements into a single string (if you think you need this feature)
- *Tip 2*: use String.split("delimiter") to split a String into separate elements. Leaving the delimiter empty will split on all characters!
- *Tip 3*: use Arrays.sort() to sort a String[] alphabetically
- *Tip 4*: you will need to use some kind of nested for-loop to get this done

