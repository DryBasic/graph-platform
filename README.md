## Loading Data to neo4j

Required packages: `neo4j`

1. Create database in your neo4j instance.
2. Install the APOC extension on your database.
3. Download the csvs from the `data/clean` directory, and add them to your neo4j database's import directory.
4. Update the `config/neo4j_load_csv.yml` with your database URI and credentials.
    - The default username is "neo4j"
    - The default URI is "bolt://localhost:7687"
5. Run the `load_graph.py` script 
    - Ensure the `neo4j` package is installed in your environment
    - Ensure your neo4j database is active/started

Helpful links: [query neo4j from python](https://neo4j.com/docs/python-manual/current/query-simple/), [csv imports in neo4j](https://neo4j.com/developer/guide-import-csv/)