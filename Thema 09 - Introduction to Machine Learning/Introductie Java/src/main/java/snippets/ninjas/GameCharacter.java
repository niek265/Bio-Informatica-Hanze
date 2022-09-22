package snippets.ninjas;

public class GameCharacter {
    String name;
    public int energyLevel = 100;

    public void drainEnergy(int amount) {
        this.energyLevel -= amount;
    }
}
