package snippets.apis;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class FileStorageSequenceWriter implements SequenceWriter {
    @Override
    public void store(Sequence sequence) {
        Path file = Paths.get("/Users/michiel/Desktop/finished_sequences.fa");
        try {
            if (! Files.exists(file)) {
                Files.createFile(file);
            }
            String fasta = ">" + sequence.name + System.lineSeparator() + sequence.sequence + System.lineSeparator();
            Files.write(
                    file,
                    fasta.getBytes(),
                    StandardOpenOption.APPEND);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
