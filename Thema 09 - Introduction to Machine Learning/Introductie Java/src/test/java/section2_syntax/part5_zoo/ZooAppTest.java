package section2_syntax.part5_zoo;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

class ZooAppTest {

    @Test
    void processZooData() {
        String[] args = {"Mouse", "Rat", "Adder", "Rat", "Pig", "Rat", "Pig"};
        ZooApp app = new ZooApp();
        app.processZooData(args);
        final List<ZooSpecies> allSpecies = ZooSpecies.getAllSpecies();
        assertThat(allSpecies.size()).isEqualTo(4);
        for (ZooSpecies zooSpecies : allSpecies) {
            if (zooSpecies.getSpeciesName().equals("Rat")) {
                assertThat(zooSpecies.getIndividualCount()).isEqualTo(3);
            }
        }
    }

}