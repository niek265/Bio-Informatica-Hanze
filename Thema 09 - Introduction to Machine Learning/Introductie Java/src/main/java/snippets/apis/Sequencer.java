package snippets.apis;

public class Sequencer {
    public static void main(String[] args) {
        Sequencer sequencer = new Sequencer();
        sequencer.start();
    }

    private void start() {
        SequenceCollection sequenceCollection = new SequenceCollection();
        Sequence seq;

        seq = new Sequence();
        seq.name = "harmless";
        seq.sequence = "GATAACAGCATAGCAAG";
        sequenceCollection.addSequence(seq);

        seq = new Sequence();
        seq.name = "probably harmless";
        seq.sequence = "GATCAGCAACTCAGCACTACGGCT";
        sequenceCollection.addSequence(seq);

        seq = new Sequence();
        seq.name = "really deadly";
        seq.sequence = "GACACGCGCGCTACAGCACT";
        sequenceCollection.addSequence(seq);

        sequenceCollection.findPathogenicSequences();

//        sequenceCollection.flush(new NoStorageSequenceWriter());
        sequenceCollection.flush(new FileStorageSequenceWriter());
    }
}
