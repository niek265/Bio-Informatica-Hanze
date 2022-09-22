package section2_syntax.part5_zoo;

import java.util.*;

public class ZooSpecies {
    private static Map<String, ZooSpecies> zooAnimals = new HashMap<>();
    private final String speciesName;
    private int individualCount;

    /**
     * A private constructor; instances will only be created within the factory method "registerSpeciesFromString".
     * @param speciesName
     */
    private ZooSpecies(String speciesName) {
        this.speciesName = speciesName;
    }

    /**
     * serves the species name.
     * @return species name
     */
    public String getSpeciesName() {
        return this.speciesName;
    }

    /**
     * serves the individual count for the species.
     * @return count
     */
    public int getIndividualCount() {
        return this.individualCount;
    }

    /**
     * This is a static factory method that registers ZooAnimal instances.
     * The keyword `static` marks a variable or method to be class-level.
     * This means it is not associated with an object (instance) but with the class: all instances of the class share
     * the same datafield. If one of them changes it, all instances share that changed field.
     * @param speciesName the species name
     */
    public static void registerSpeciesFromString(String speciesName) {
        ZooSpecies zooSpecies;
        if (! zooAnimals.containsKey(speciesName)) { // it is not registered yet
            zooSpecies = new ZooSpecies(speciesName);
            zooAnimals.put(speciesName, zooSpecies);
        } else { // already know species
            zooSpecies = zooAnimals.get(speciesName);
        }
        zooSpecies.individualCount++;
    }

    /**
     * Serves all registered species in this Zoo.
     * @return allSpecies
     */
    public static List<ZooSpecies> getAllSpecies() {
        List<ZooSpecies> species = new ArrayList<>();
        species.addAll(ZooSpecies.zooAnimals.values());
        return species;
    }
}
