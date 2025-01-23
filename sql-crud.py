from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker

# executing the instructions from our local host "chinook" database
db = create_engine("postgresql:///chinook") # the 3 slashes are used to indicate that the database is on the local host
Base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(Base):
    __tablename__ = "Programmer"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point it to our engine (db)
Session = sessionmaker(bind=db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
Base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(

    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

hal_9000 = Programmer(
    first_name="HAL",
    last_name="9000",
    gender="non-specific",
    nationality="Space-born",
    famous_for="singing Daisy"
)

# add each instance of our Programmer class to the session
#session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(hal_9000)

# commit the records to the database
session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )