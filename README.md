# dbpedia-graph-convertor
This repository will make a SPARQL query at the dbpedia endpoint and it will convert the resulting JSON result as a Property Graph and store it as a GraphML file.

## Instructions to run the script
Create a sub-directory in the folder which has the name "z_ttl" and download all the files mentioned in the *files.txt* file.
Download the files and extract it in the same directory. 
A file would be created by the name of **test.graphML** once the script has run successfully. To change this name, the argument of the function **build_graph** should be changed on line # 98 in dbpedia.py.
```bash
    python3 dbpedia.py
```
