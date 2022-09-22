package section2_syntax.part5_zoo;

import java.util.List;

public class ZooApp {

    public static void main(String[] args) {
        ZooApp zooApp = new ZooApp();
        zooApp.processZooData(args);
        zooApp.printZooSummary();
    }

    /**
     * Processes the command line data.
     * @param args
     */
    void processZooData(String[] args) {
        //YOUR CODE HERE; pass zoo animals to ZooSpecies
    }

    /**
     * Prints a summary of the zoo.
     */
    void printZooSummary() {
        final List<ZooSpecies> allSpecies = null; //YOUR CODE HERE; fetch all species
        //YOUR CODE HERE
        for (ZooSpecies species : allSpecies) {
            //YOUR CODE HERE
        }
    }
}
