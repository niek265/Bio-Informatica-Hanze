package snippets.apis;

public class Sequence {
    String sequence;
    String name;

    /**
     * returns the molecular weight, in Daltons
     * @return weightInDaltons
     */
    double getMolecularWeight() {
        double weight = 0;
        //implementation to calculate weight
        return weight;
    }

    /**
     * Mutates a single position and returns a modified copy.
     * This object itself is NOT mutated!
     * @param position
     * @param newCharacter
     * @return mutatedSequence
     */
    Sequence mutate(int position, char newCharacter) {
        StringBuilder stringBuilder = new StringBuilder(this.sequence);
        stringBuilder.setCharAt(position, newCharacter);
        Sequence mutatedSequence = new Sequence();
        mutatedSequence.sequence = stringBuilder.toString();
        return mutatedSequence;
    }


}
