# coded by h4sski

from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import date, datetime
from itertools import zip_longest
import models
from models import User, Activity, session


def add_activity(user, dist, d, t):
    a = Activity(user_id=user.id, distance=dist, date=d, type=t)
    session.add(a)
    session.commit()


def add_user(user, users):
    '''
    Check if user exists in db based on 'email'. If not then add it into db.
    :param user: User
    :param users: list(User)
    :return: None
    '''
    exist = False
    for u in users:
        if u.email == user.email:
            exist = True
    if not exist:
        session.add(user)
        session.commit()


def users_print(users):
    print('\nUser table:')
    for u in users:
        print(u.id, u.full_name, u.role, u.email, u.password)
    print('- - - - - - - - -')


def main():
    models.create_db()
    user_adam = User(email='adam@gmail.com', \
                     password='1234', \
                     full_name='Adam')
    user_bob = User(email='bob@gmail.com', \
                    password='qwer', \
                    full_name='Bob', \
                    role='admin')

    # users = session.execute(select('*').select_from(User)).all()
    users = session.query(User).all()
    add_user(user_adam, users)
    add_user(user_bob, users)
    users_print(users)

    user_adam = session.query(User).filter_by(email=user_adam.email).first()
    user_bob = session.query(User).filter_by(email=user_bob.email).first()

    print(user_adam.activity)
    # add_activity(user_adam, 1, date(2022, 10, 1), 'bike')
    # add_activity(user_adam, 5, date(2022, 10, 5), 'bike')
    # add_activity(user_adam, 10, date(2022, 10, 10), 'bike')
    # add_activity(user_bob, 2, date(2022, 10, 2), 'bike')
    # add_activity(user_bob, 6, date(2022, 10, 6), 'bike')
    # add_activity(user_bob, 8, date(2022, 10, 8), 'bike')

    '''
    Query and print activities of 1 user at all dates.
    '''
    result = session.query(Activity).filter_by(user_id=user_adam.id)
    for r in result:
        print(r.id, r.user_id, r.distance, r.date, r.type, r.time_created, r.time_updated)

'''
Query and print all activities in db.
'''
'''    result = session.query(Activity).all()
    for r in result:
        print(r.id, r.user_id, r.distance, r.date, r.type, r.time_created, r.time_updated)'''

'''
Print all activities of user_adam
'''
'''    for a in user_adam.activity:
        if a.distance >= 0:
            print(f'{a.distance} \t{a.date} \t{a.type}')'''

if __name__ == '__main__':
    main()
