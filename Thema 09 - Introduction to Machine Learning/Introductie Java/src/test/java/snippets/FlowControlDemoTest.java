package snippets;

import org.junit.jupiter.api.Test;
import snippets.syntax.FlowControlDemo;

class FlowControlDemoTest {
    @Test
    void potjeMetVetTest() {
        FlowControlDemo demo = new FlowControlDemo();
        demo.potjeMetVet();
    }

    @Test
    void switchCase() {
        FlowControlDemo demo = new FlowControlDemo();
        demo.switchCase("Netherlands");
    }

    @Test
    void errorMessageTest() {
        FlowControlDemo demo = new FlowControlDemo();
        String errorMessage = demo.errorMessage(402);
        System.out.println(errorMessage);
        errorMessage = demo.errorMessage(502);
        System.out.println(errorMessage);
    }

}