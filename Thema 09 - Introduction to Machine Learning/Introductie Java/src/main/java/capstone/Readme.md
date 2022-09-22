# Capstone project
## Implementing a bird browser

This is the capstone project of the course. You will work on an application that can be used to browse a "database" of all known bird species.


## Learning outcomes

* Creating a "data model" design
* Working with collections and sorting
* Working with enums
* Algorithm development

## The assignment

In the `data` folder, you will find a txt file called `birds_observado_org.csv`. This file holds some information on all known bird species of the world, downloaded from [observado.org](https://observation.org/download.php). Here are the first few lines:

```
"id";"name";"Scientific name";"obscure";"rarity";"SPECIESGROUP";"SPECIESGROUP";"species type";"species type";"euring";"pons";"searchkey";"family";"AUTHOR";"list";"status";"refer_to";"plantlistid";"name order";
"693286";"";"Androrchis spec.";"0";"0";"1";"birds";"M";"multispecies";"0";"0";"";"";"";" unknown";"Native";"0";"";"";
"682516";"";"Coccycolius spec.";"0";"0";"1";"birds";"M";"multispecies";"0";"0";"";"";"";" unknown";"Native";"0";"";"";
"73939";"Swallow Flycatcher";"Hirundinea bellicosa";"0";"2";"1";"birds";"S";"species";"0";"0";"";"";"";" unknown";"Native";"0";"";"999";
"71881";"Flame rumped Sapphire";"Hylocharis pyropygia";"0";"2";"1";"birds";"S";"species";"0";"0";"";"";"";" unknown";"Native";"0";"";"989";
"71881";"Flame-rumped Sapphire";"Hylocharis pyropygia";"0";"2";"1";"birds";"S";"species";"0";"0";"";"";"";" unknown";"Native";"0";"";"999";
"75027";"San Cristobal Melidectes";"Melidectes sclateri";"0";"2";"1";"birds";"S";"species";"0";"0";"";"";"";" unknown";"Native";"0";"";"999";
"690370";"";"Melidectes spec.";"0";"0";"1";"birds";"M";"multispecies";"0";"0";"";"";"";" unknown";"Native";"0";"";"";
"680113";"";"Passerculus spec.";"0";"0";"1";"birds";"M";"multispecies";"0";"0";"";"";"";" unknown";"Native";"0";"";"";
```

The database browsing application should receive its arguments from the command-line, always assuming the bird data file is in the current directory under `data/birds_observado_org.csv` (so you do not have to provide that at the command line).


You have to program an application that supports these use cases: 

1. Give the details of a bird by its ID:

    ```
    java -jar BirdBrowser.jar id 680113
    ```

    This should print all information of the species, including its subspecies, sorted by scientific name.
     
2.  Search species by wildcard search, supporting regex patterns:

    ```
    java -jar BirdBrowser.jar wildcard "[^ ]owl"
    ```

    This should print all matching species: id, english name and scientific name.  
    **_Challenge_**: with match uppercased, sorted by english name.

3. Filter species by three fields: (1) (part of-) the (scientific) name, (2) minimal "rarity" level and (3) "species type". It should be supported something like this:

    ```
    java -jar BirdBrowser.jar filter "bee|3|subspecies"
    ```

Maybe you can think of some nice additional use cases!  

The real challenge here is not to make it work, but more to make a well-designed and well-coded object-oriented application.  

There are no JUnit tests; you are strongly encouraged to create your own.
