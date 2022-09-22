package section3_apis.part1_interfaces;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class CaesarCypherTest {

    @Test
    @DisplayName("Testing simple encryption using Caesar Cypher")
    void encrypt() {
        CaesarCypher caesarCypher = new CaesarCypher();
        final String observed = caesarCypher.encrypt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG");
        final String expected = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD";
        assertThat(observed).isEqualTo(expected);
    }

    @Test
    @DisplayName("Testing advanced encryption using Caesar Cypher")
    void encrypt2() {
        CaesarCypher caesarCypher = new CaesarCypher();
        final String observed = caesarCypher.encrypt("The Quick Brown Fox: jumps!");
        final String expected = "Qeb Nrfzh Yoltk Clu: grjmp!";
        assertThat(observed).isEqualTo(expected);
    }


    @Test
    @DisplayName("Testing simple decryption using Caesar Cypher")
    void decrypt() {
        CaesarCypher caesarCypher = new CaesarCypher();
        final String observed = caesarCypher.decrypt("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD");
        final String expected = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG";
        assertThat(observed).isEqualTo(expected);
    }

    @Test
    @DisplayName("Testing advanced decryption using Caesar Cypher")
    void decrypt2() {
        CaesarCypher caesarCypher = new CaesarCypher();
        final String observed = caesarCypher.decrypt("Qeb Nrfzh Yoltk Clu: grjmp!");
        final String expected = "The Quick Brown Fox: jumps!";
        assertThat(observed).isEqualTo(expected);
    }

}