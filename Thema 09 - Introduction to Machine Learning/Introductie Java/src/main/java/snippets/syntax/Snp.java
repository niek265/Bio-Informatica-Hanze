package snippets.syntax;

/**
 * Class Snp models a Single Nucleotide Polymorphism in its simplest form.
 * The class is public, so any class within the project may instantiate it.
 */
public class Snp {
    /**
     * These are the INSTANCE VARIABLES that model the SNPs data. They form the DATA BLUEPRINT
     * of this class. They are PRIVATE, so they can not be accessed from outside this class.
     * The types are long (integer) and character (single letter)
     */
    private long position;
    private char referenceNucleotide;
    private char alternativeNucleotide;

    /**
     * This is the CONSTRUCTOR method that forces client code to provide the three essential
     * properties of a Snp that every INSTANCE should have defined before being INSTANTIATED.
     * It is public so accessible to all. Properties are passed as constructor arguments and
     * stored as INSTANCE VARIABLES.
     * @param position a long integer
     * @param reference a single character: A, C, G or T
     * @param alternative a single character: A, C, G or T
     * @throws IllegalArgumentException if the given position is negative
     */
    public Snp(long position, char reference, char alternative) {
        if (position < 1) {
            throw new IllegalArgumentException("postition must be positive");
        }
        this.position = position;
        this.referenceNucleotide = reference;
        this.alternativeNucleotide = alternative;
    }

    /**
     * a GETTER for the position. Since the "position" field is private, this makes it a READ_ONLY
     * property.
     * @return the position as long integer
     */
    public long getPosition() {
        return position;
    }

    /**
     * same here
     * @return reference
     */
    public char getReferenceNucleotide() {
        return referenceNucleotide;
    }

    /**
     *
     * @return alternative nuc
     */
    public char getAlternativeNucleotide() {
        return alternativeNucleotide;
    }

    /**
     * this method tells a client whether ths SNP is a transition or a transversion.
     * The return type is boolean (true or false).s
     * @return transition boolean
     */
    public boolean isTransition() {
        return ((referenceNucleotide == 'A' && alternativeNucleotide == 'G')
                || (referenceNucleotide == 'C' && alternativeNucleotide == 'T'));
    }
}
