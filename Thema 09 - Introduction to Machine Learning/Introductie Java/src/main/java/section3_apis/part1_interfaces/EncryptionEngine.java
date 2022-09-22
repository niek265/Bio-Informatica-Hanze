package section3_apis.part1_interfaces;

public interface EncryptionEngine {
    /**
     * Encrypts the given message
     * @param message
     * @return encryptedMessage
     */
    String encrypt(String message);

    /**
     * Decrypts the given message, but only if it was the result of the encrypt method
     * of this same instance.
     *
     * @param encryptedMessage
     * @return decryptedMessage
     */
    String decrypt(String encryptedMessage);
}
