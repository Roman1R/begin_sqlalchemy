from data import db_session
from data.jobs import Job
import datetime

"""
    team_leader 1
    job deployment of residential modules 1 and 2
    work_size 15
    collaborators 2, 3
    start_date (now)
    is_finished False
"""


def main():
    db_session.global_init("db/jobs.db")
    db_sess = db_session.create_session()

    # db_sess.query(Job).delete()  # FUNCTION TO DELETE

    rand = Job()
    rand.team_leader = 1
    rand.job = "deployment of residential modules 1 and 2"
    rand.work_size = 15
    rand.collaborators = "2, 3"
    rand.start_date = datetime.datetime.now()
    rand.is_finished = False

    db_sess.add(rand)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()