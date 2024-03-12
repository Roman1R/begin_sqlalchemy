from data import db_session
from data.users import User


def main():
    db_session.global_init(f"db/{input()}")
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
        print(user)

    # app.run()


if __name__ == '__main__':
    main()