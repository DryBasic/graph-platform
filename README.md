## About

This repository contains the work performed to generate a knowledge graph to represent Spotify entities (playlist, track, artist, etc.) and the keywords and topics extracted from a track's lyrics (fetched from Genius). 

Contained within is a generalized script that maps csv columns to neo4j entities and allows for local loading of the entities contained within the csvs. More details in the next section.

This project was completed as part of DSE 203: Data Integration & ETL.

***
## Getting spotify data for kaggle dataset

The notebook `kaggle_spotify_fetcher.ipynb` does a few things:

1. Searching spotify for each song in the kaggle dataset using the track name and artist(s) name, and grabbing the best match using jaccard similarity
2. Filters out songs that didn't get a satisfactory match on spotify
3. Gets the audio analysis for all of the kaggle tracks, which has things like tempo, key, and node

## Natural Language Processing on lyrics

The notebook `get_lyrics_keywords_and_topics` takes care of a few things:

1. First, the notebook loads the genius lyrics and does the same jaccard similarity matching as from the previous step, throwing out any songs for which we couldn't retrieve a correct match from genius.
2. Next, the notebook does textrank phrase ranking and RAKE phrase ranking to generate phrases. We didn't end up using these for the final graph as the number of unique phrases was much greater than just keywords and would probably be too much to load into the graph.
3. Finally, the notebook does Latent Dirichlet Allocation (LDA) Topic searching, which is broken into a few parts:
    1. First, we split the lyrics into a vector of words
    2. Next, we remove stopwords and perform lemmatization to get the roots of words, and get rid of anything that isn't a noun, adjective, verb, or adverb.
    3. Finally, we run the LDAmodel and find the top keywords for each topic, and which documents contain which keywords
        * This will be integrated into the graph as Topic Nodes and Keyword Nodes, with songs connect to topics through the keywords but not directly

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
