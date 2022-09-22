package section4_oop.part3_consensus_creator;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ConsensusSequenceCreatorTest {
    @Test
    public void testCreateConsensus_A() {
        String[] sequences = new String[4];
        sequences[0] = "GAAT";
        sequences[1] = "GAAA";
        sequences[2] = "GATT";
        sequences[3] = "GAAC";
        String expResult = "GAWH";
        ConsensusSequenceCreator csc = new ConsensusSequenceCreator();
        String result = csc.createConsensus(sequences, true);
        assertEquals(expResult, result);
    }

    @Test
    public void testCreateConsensus_B() {
        String[] sequences = new String[4];
        sequences[0] = "GAAT";
        sequences[1] = "GAAA";
        sequences[2] = "GATT";
        sequences[3] = "GAAC";
        String expResult = "GA[A/T][A/C/T]";
        ConsensusSequenceCreator csc = new ConsensusSequenceCreator();
        String result = csc.createConsensus(sequences, false);
        assertEquals(expResult, result);
    }

    @Test
    public void testCreateConsensus_C() {
        String[] sequences = new String[5];
        sequences[0] = "CGAATA";
        sequences[1] = "CGAAAA";
        sequences[2] = "GGATTA";
        sequences[3] = "GGAACA";
        sequences[4] = "TGAACA";
        String expResult = "[C/G/T]GA[A/T][A/C/T]A";
        ConsensusSequenceCreator csc = new ConsensusSequenceCreator();
        String result = csc.createConsensus(sequences, false);
        assertEquals(expResult, result);
    }

    @Test
    public void testCreateConsensus_D() {
        String[] sequences = new String[5];
        sequences[0] = "CGAATA";
        sequences[1] = "CGAAAA";
        sequences[2] = "GGACTA";
        sequences[3] = "GGAACA";
        sequences[4] = "TGAACA";
        String expResult = "BGAMHA";
        ConsensusSequenceCreator csc = new ConsensusSequenceCreator();
        String result = csc.createConsensus(sequences, true);
        assertEquals(expResult, result);
    }

}