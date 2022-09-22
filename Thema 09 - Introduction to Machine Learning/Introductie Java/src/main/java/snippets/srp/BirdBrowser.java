package snippets.srp;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class BirdBrowser {
    public static void main(String[] args) {
        BirdBrowser browser = new BirdBrowser(args[0]);
    }

    public BirdBrowser(String queryString){
        loadBirdData();
        lookForBirds(queryString);
    }

    private void lookForBirds(String queryString) {

    }

    private void loadBirdData() {
        try(BufferedReader reader = Files.newBufferedReader(Paths.get("data/Clements-Checklist-v2018.csv"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("line = " + Arrays.toString(line.split(" ")));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
