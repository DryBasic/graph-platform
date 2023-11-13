## Loading Data to neo4j

Required packages: `neo4j`

1. Create database in your neo4j instance.
2. Install the APOC extension on your database.
3. Download the csvs from the `data/clean` directory, and add them to your neo4j database's import directory.
4. Update the `config/neo4j_load_csv.yml` with your database URI and credentials.
5. Run the `load_graph.py` script.

Helpful links: [query neo4j from python](https://neo4j.com/docs/python-manual/current/query-simple/), [csv imports in neo4j](https://neo4j.com/developer/guide-import-csv/)