package snippets.ninjas;

public class Game {
    public static void main(String[] args) {
        //spawn (instantiate) a Ninja
        Ninja ninja = new Ninja();

        //change its name
        ninja.name = "Rogue Bastard";
        //print some values of the ninja
        System.out.println("Ninja name      = " + ninja.name);
        System.out.println("Ninja energy    = " + ninja.energyLevel);
        System.out.println("Ninja position  = ["
                + ninja.topCoordinate
                + ":"
                + ninja.leftCoordinate
                + "]");

        //spawn an opponent
        GameCharacter opponent = new GameCharacter();
        opponent.name = "Delirious Troll";

        //change position twice
        ninja.move(2, 9);
        ninja.move(-6.4, 3.5);
        System.out.println("Ninja position  = ["
                + ninja.topCoordinate
                + ":"
                + ninja.leftCoordinate
                + "]");

        //attack opponent
        ninja.attack(5, opponent);

        //energy of both has changed
        System.out.println("Ninja energy    = " + ninja.energyLevel);
        System.out.println("Opponent name   = " + opponent.name);
        System.out.println("Opponent energy = " + opponent.energyLevel);
    }
}
