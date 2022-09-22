package snippets.apis;


public interface SequenceWriter {
    /**
     * This is the sole method defined in this interface. It accepts an
     * object and will write a representation of it to an external destination.
     * @param sequence the object to write
     */
    void store(Sequence sequence);
}
