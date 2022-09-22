package snippets.syntax;

public class FlowControlDemo {
    boolean isWinter = true;

    public static void main(String[] args) {
//        for(;;) {
//            System.out.println("Hello ");
//        }

//        while(true) {
//            System.out.println("Hello");
//        }

//        while(true) {
//            int answer = getUserInput();
//            if (answer == 42) break;
//        }

        String[] nucleotides = {"Adenine", "Cytosine", "Guanine", "Thymine"};
        int i = nucleotides.length - 1;
        for( ; i >= 0; --i) {
            System.out.println("nucleotide " + i + " is " + nucleotides[i]);
        }

        for( String nucleotide : nucleotides) {
            System.out.println("nucleotide = " + nucleotide);
        }

    }

    private static int getUserInput() {
        return 0;
    }


    public void potjeMetVet() {
        for(int i = 1; i <= 100; i++) {
            String append = (i > 1 && i < 20 && (i != 8)) ? "de" : "ste";
            System.out.println("Ik heb een potje met vet, al op de tafel gezet, ik heb een potje potje " +
                    "potje potje veeeeheeet al op de tafel gezet\n" +
                    "Dit was het " + i + append + " couplet.");
        }
    }

    public void switchCase(String country) {
        switch (country) {
            case "Netherlands":
                System.out.println("Some weather, huh?");
//                break;
            case "Belgium":
                System.out.println("It is Belgian fries!");
//                break;
            default:
                System.out.println("Have a beer?");
        }
    }

    public String errorMessage(int errorCode) {
        String message;
        switch (errorCode) {
            case 401:
            case 402:
            case 403:
            case 405:
                message = "You are trying to do something that is not allowed";
                break;
            case 404:
            case 503:
                message = "Resource not found";
                break;
            default:
                message = "Some exotic error occurred. Try again later";
        }
        return message;
    }
}
