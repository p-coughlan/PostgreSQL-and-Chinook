from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker

# executing the instructions from our local host "chinook" database
db = create_engine("postgresql:///chinook") # the 3 slashes are used to indicate that the database is on the local host
Base = declarative_base()

# Create a class-based model for the "Artist" table
class Artist(Base):
    __tablename__ = "Artist"
    
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# Create a class-based model for the "Album" table
class Album(Base):
    __tablename__ = "Album"
    
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# Create a class-based model for the "Track" table
class Track(Base):
    __tablename__ = "Track"
    
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point it to our engine (db)
Session = sessionmaker(bind=db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
Base.metadata.create_all(db)

# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist).all()
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" | ") # print the results using a loop and separator

# Query 2 - Select only the "Name" column from the "Artist" table
# artists = session.query(Artist.Name).all()
# for artist in artists:
#    print(artist.Name)

# Query 3 - Select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - Select only by "ArtistId" # 51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - Select only the albums with "ArtistId" # 51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51).all()
# for album in albums:
#    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen").all()
for track in tracks:
    print(track.TrackId, track.Name, track.Composer, sep=" | ")

 