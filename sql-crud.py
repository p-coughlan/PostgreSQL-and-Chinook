from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# Print statement to verify script execution
print("Script started")

# Database setup
db = create_engine("postgresql:///chinook")
Base = declarative_base()

# Define the Programmer class
class Programmer(Base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# Create a new instance of sessionmaker, then point it to our engine (db)
Session = sessionmaker(bind=db)
session = Session()

# Print statement to verify session creation
print("Session created")

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

# Uncomment these lines if you need to add records
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(hal_9000)

# commit the records to the database
# session.commit()

# updating a single record in the database
# programmer = session.query(Programmer).filter_by(id=7).first()
# if programmer:
#     programmer.famous_for = "Locking Dave out of the spaceship"
#     # commit the records to the database
#     session.commit()
# else:
#     print("Programmer with ID 7 not found")

# Update famous_for in record with ID 21
# programmer = session.query(Programmer).filter_by(id=21).first()
# if programmer:
#     programmer.famous_for = "Locking Dave out of the spaceship"
#     session.commit()
# else:
#     print("Programmer with ID 21 not found")

# Change primary keys so firts itme on table starts at 1 and increments by 1 for each new record
# Reset the primary key sequence

# Drop the existing table to reset the primary key sequence
Base.metadata.drop_all(db)
# Recreate the table
Base.metadata.create_all(db)

# Add the records again
session.add_all([
    ada_lovelace,
    alan_turing,
    grace_hopper,
    margaret_hamilton,
    bill_gates,
    tim_berners_lee,
    hal_9000
])

# Commit the records to the database
session.commit()



# updating multiple records in the database
# people = session.query(Programmer).all()
# print(f"Found {len(people)} programmers")
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
# session.commit()

# deleting a single record from the database
# fname = input("Enter the first name of the programmer to delete: ")
# lname = input("Enter the last name of the programmer to delete: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer record deleted")
#     else:
#         print("Programmer not deleted")
# else:
#   print("No records found")

# deleting multiple records from the database
# programmers = session.query(Programmer)
# for programmer in programmers:
#    session.delete(programmer)
# session.commit()


# query the database to find all programmers
programmers = session.query(Programmer).all()
if not programmers:
    print("No programmers found in the database")
else:
    for programmer in programmers:
        print(
            programmer.id,
            programmer.first_name + " " + programmer.last_name,
            programmer.gender,
            programmer.nationality,
            programmer.famous_for,
            sep=" | "
        )

# Print statement to verify script completion
print("Script completed")

