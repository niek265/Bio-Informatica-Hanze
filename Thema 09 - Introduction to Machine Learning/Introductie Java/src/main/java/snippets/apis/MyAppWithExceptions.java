package snippets.apis;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MyAppWithExceptions {

    public static void main(String[] args) {
        MyAppWithExceptions app = new MyAppWithExceptions();
        app.start();
    }

    private void start() {
        try {
            loadDatabase();
            readFile("some_file");
            processData();
            writeResults("results_file");
        } catch (IOException | SQLException e) {
            Logger.getLogger("MyApp").log(Level.SEVERE, "IO error!", e);
            System.err.println("An error occurred. See the log for details.");
            //don't use stacktrace in production!
            //e.printStackTrace();
        }
    }

    private void processData() {
        try {
            //processing file data
        } catch (NumberFormatException e) {
            //note this is an unchecked exception;
            //the try/catch is optional
            Logger.getLogger("MyApp").log(Level.INFO, "Number format problem", e);
        }
    }

    private void writeResults(String resultsFile) throws FileAlreadyExistsException {
        //write to results file
    }

    private void loadDatabase() throws SQLException {
        //loading MySQL DB
    }

    private void readFile(String someFile) throws FileNotFoundException {
        //reading input data
    }
}
