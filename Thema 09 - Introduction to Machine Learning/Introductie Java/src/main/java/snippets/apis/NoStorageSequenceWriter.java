package snippets.apis;

public class NoStorageSequenceWriter implements SequenceWriter {
    @Override
    public void store(Sequence sequence) {
        System.out.println("not interested in sequence " + sequence.name + " anymore");
    }
}
