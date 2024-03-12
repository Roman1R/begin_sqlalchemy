from data import db_session
from data.users import User

"""
    surname Scott
    name Ridley
    age 21
    position captain
    speciality research engineer
    address module_1
    email scott_chief@mars.org
"""


def main():
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()

    # db_sess.query(User).delete()  # FUNCTION TO DELETE

    cap = User()
    cap.surname = "Scott"
    cap.name = "Ridley"
    cap.age = 21
    cap.position = "captain"
    cap.speciality = "research engineer"
    cap.address = "module_2"
    cap.email = "scott_chief@mars.org"

    boatswain1 = User()
    boatswain1.surname = "Mr.Smith"
    boatswain1.name = "Tom"
    boatswain1.age = 25
    boatswain1.position = "member"
    boatswain1.speciality = "boatswain"
    boatswain1.address = "module_2"
    boatswain1.email = "mr_tom@mars.org"

    boatswain2 = User()
    boatswain2.surname = "Absolutely_Hz"
    boatswain2.name = "Hz"
    boatswain2.age = 27
    boatswain2.position = "member"
    boatswain2.speciality = "boatswain"
    boatswain2.address = "module_2"
    boatswain2.email = "hz_hz_hz@mars.org"

    cooker = User()
    cooker.surname = "Mrs.Cook"
    cooker.name = "Sussan"
    cooker.age = 27
    cooker.position = "spec_member"
    cooker.speciality = "cooker"
    cooker.address = "module_1"
    cooker.email = "recipe_for_life@mars.org"

    db_sess.add(cap)
    db_sess.add(boatswain1)
    db_sess.add(boatswain2)
    db_sess.add(cooker)

    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()