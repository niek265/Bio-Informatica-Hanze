package snippets.ninjas;

public class Ninja {
    //Here are the properties every Ninja will HAVE
    //We call these INSTANCE VARIABLES
    String name;
    int energyLevel = 100;
    double topCoordinate;
    double leftCoordinate;

    //Here are the methods - what every Ninja can DO
    void move(double top, double left) {
        this.topCoordinate += top;
        this.leftCoordinate += left;
    }

    void attack(int power, GameCharacter opponent) {
        //energy is drawn from its own reserve for an attack
        this.energyLevel -= power;
        //but has double effect on its opponent
        opponent.drainEnergy(power * 2);
    }
//end of the class
}
