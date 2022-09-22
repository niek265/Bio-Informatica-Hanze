package snippets.apis;

import java.util.ArrayList;
import java.util.List;

public class SequenceCollection{
    private List<Sequence> sequences = new ArrayList<>();

    public void addSequence(Sequence sequence) {
        this.sequences.add(sequence);
    }

    public void removeSequence(Sequence sequence) {
        this.sequences.remove(sequence);
    }

    /**
     * Looks for pathogenic sequences in the current batch
     * @return pathogenicSequences
     */
    public List<Sequence> findPathogenicSequences() {
        ArrayList<Sequence> pathogenics = new ArrayList<>();
        //complex logic
        return pathogenics;
    }

    /**
     * This will write the current SequenceCollection to en external destination
     * and empty the collection.
     * @param writer the writer that processes each individual sequence object
     */
    public void flush(SequenceWriter writer) {
        for (Sequence seq : this.sequences) {
            //NO CLUE OF THE ACTUAL WRITING IMPLEMENTATION
            //ONLY KNOW THERE IS AN OBJECT LIVING UP TO TO THE CONTRACT
            writer.store(seq);
        }
        this.sequences.clear();
    }


    //LOGIC INVOLVING THIS SEQUENCE COLLECTION
}
