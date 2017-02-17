from SPARQLWrapper import SPARQLWrapper, JSON, XML

def get_data_in_json(query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(city_pops)  # the previous query as a literal string
    results = sparql.query().convert()
    return results


# Query to get the population of countries
country_pops = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX : <http://dbpedia.org/resource/>
    PREFIX dbpedia2: <http://dbpedia.org/property/>
    PREFIX dbpedia: <http://dbpedia.org/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX yago:<http://dbpedia.org/class/yago/>

    SELECT ?country_name ?population
    WHERE {
        ?country_name a dbo:Country .
        ?country_name a yago:WikicatCountries .
        
        ?country_name dbpedia2:populationEstimate ?population . 
    }
    """

# Query to get the population of cities
city_pops = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX : <http://dbpedia.org/resource/>
    PREFIX dbpedia2: <http://dbpedia.org/property/>
    PREFIX dbpedia: <http://dbpedia.org/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX yago:<http://dbpedia.org/class/yago/>

    SELECT ?city_name ?enName ?population
    WHERE {
        ?city_name a dbo:City .
        OPTIONAL { ?city_name dbo:populationTotal ?population . }
    }
    """

if __name__=="__main__":
    Z = get_data_in_json(country_pops)
    print(Z)

