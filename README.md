## About

This repository contains the work performed to generate a knowledge graph to represent Spotify entities (playlist, track, artist, etc.) and the keywords and topics extracted from a track's lyrics (fetched from Genius). 

Contained within is a generalized script that maps csv columns to neo4j entities and allows for local loading of the entities contained within the csvs. More details in the next section.

This project was completed as part of DSE 203: Data Integration & ETL.

***

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

***

## Entity Fetching and Additonal Processing

The Spotify API calling and entity extraction can be found in data/fetch/spotify_api. 

* Tracks (2 sources)
    - 953 tracks obtained from a Kaggle Dataset
        - Ran Spotify API to fetch Spotify IDs, required fuzzy value matching to identify correct return
    - 1277 tracks obtained from running the Spotify API using track ids coming from the Playlist API

* Playlists 
    - Obtained from Spotify Featured Playlist API
    - The track_ids contained herein were used to gather more tracks with the Tracks API

* Artists & Genre
    - Obtained from Spotify Artist API using the artist ids that came from the Tracks API call
    - Genre is an attribute of Artist

* Audio Features
    - Obtained from Spotify Audio Feature API using track ids as inputs
    - Performed additional transformations as can be found in data/transform/audio_features.ipynb

* Keyword & Topic
    - Extracted from lyrics pulled using the Genius API (data/fetch/genius_api.ipynb)
