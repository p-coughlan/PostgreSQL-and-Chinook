from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, MetaData, String
)

# executing the instructions from our local host "chinook" database
db = create_engine("postgresql:///chinook") # the 3 slashes are used to indicate that the database is on the local host

# Create a MetaData object to hold information about the "chinook" database
meta = MetaData(db)

# Create a variable for the "Artist" table, creates a "Table Object"
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create a variable for the "Album" table, creates a "Table Object"
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# Create a variable for the "Track" table, creates a "Table Object"
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# Making the connection
with db.connect() as connection:

    # Query 1 - Select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - Select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - Select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - Select only by "ArtistId" # 51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select only the albums with "ArtistId" # 51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)


    