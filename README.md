# ER Modeling SQL Schema Design Project
_A collaboration with William Chen and Matthew Liu_

## Introduction

In this project, I worked with a sizable dataset downloaded from the eBay web site and stored in JSON format. My challenge was to transform this semi-structured data into a well-organized relational database schema. After designing the database schema, I wrote a Python program to convert the data from JSON to SQLite's load file format. This project tested my understanding of data manipulation, schema design, and SQL queries.

## Phase 1: Understanding the JSON Data Files

To kick off the project, I downloaded and examined a JSON-encoded auction dataset. This dataset contained approximately 20,000 auctions, totaling around 38MB of text data. After familiarizing myself with the data schema, my main objective was to translate this data into relations and load it into my AuctionBase database. 

## Phase 2: Designing the Relational Schema

Instead of simply dumping all auction data into a single relation, I designed a better schema, documented in design.pdf. This design started with an Entity-Relation (ER) diagram and text form relational schema definitions. I ensured to include the attributes for each relation and clearly indicated the primary keys in the schema. 

## Phase 3: Data Transformation Program

Next, I wrote a Python program to transform the JSON data into SQLite load files, consistent with the relational schema I designed. To ensure efficient performance, I implemented duplicate elimination within the Python parser and made sure the program ran smoothly even on the full dataset.

## Phase 4: Loading Data into SQLite

The data was then loaded into SQLite, using a set of commands from a command file create.sql. This file contained SQL commands to create all necessary tables according to my schema design. Another command file, load.txt, was created to load the data into these tables.

## Phase 5: Testing the SQLite Database

The final step was to test the newly loaded database by running a set of SQL queries. To ensure correctness, I started with simple queries over one relation and gradually moved to more complex queries involving joins and aggregation. Some specific tasks included finding the number of users in the database, the number of users from New York, the number of auctions belonging to exactly four categories, etc.

## Conclusion

This project provided a hands-on experience in handling large volumes of data, designing an efficient relational database schema, transforming data between different formats, and querying the database to fetch desired results. This repository showcases my abilities in data management, Python scripting, and SQL database design and management. I hope this project piques your interest and I look forward to the possibility of discussing it further.
