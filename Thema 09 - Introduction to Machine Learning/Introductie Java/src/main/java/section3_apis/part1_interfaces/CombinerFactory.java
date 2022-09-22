package section3_apis.part1_interfaces;

public class CombinerFactory {
    /**
     * This method serves a StringCombiner that will surround the given arguments with double quotes,
     * separated by spaces and the result surrounded by single quotes.
     *
     * For example, the call
     *      combiner.combine("one", "two")
     * will return '"one" "two"'
     * @return quotedCombiner
     */
    static StringCombiner getQuotedCombiner() {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }

    /**
     * This method serves a StringCombiner that will combine the given arguments reversed and original,
     * concatenated with a space in between.
     *
     * For example,
     *      combiner.combine("one", "two")
     * will return "oneeno twoowt"
     *
     * (the quotes are not included in the return value).
     * @return reversedCombiner
     */
    static StringCombiner getReversedCombiner() {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }

    /**
     * <strong>Challenge!</strong>
     * This method serves a StringCombiner that will combine the given arguments so that the characters of both
     * arguments are converted to their ASCII values and then the summed. These numbers are combined with a space
     * in between and returned.
     *
     * For example,
     *      combiner.combine("one", "two")
     * will return "322 346"
     * Because 111 + 110 + 101 = 322 and 116 + 119 + 111 = 346.
     *
     * Hint: a char IS AN integer behind the scenes
     *
     * @return reversedCombiner
     */
    static StringCombiner getAsciiSumCombiner() {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }

}
