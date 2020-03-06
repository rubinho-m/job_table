from data import db_session
from flask import Flask, render_template

from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(f'db/mars_explorer.db')
    app.run()


def add_job():
    session = db_session.create_session()
    job = Jobs(id=2, team_leader=1, job='ship cleaning', work_size=15, collaborators='2, 3',
               is_finished=False)
    session.add(job)
    session.commit()


@app.route("/")
def index():
    session = db_session.create_session()
    news = session.query(Jobs).all()
    users = session.query(User.name, User.surname).all()
    for i in range(len(users)):
        users[i] = ' '.join(users[i])
    return render_template("index.html", jobs=news, users=users)


if __name__ == '__main__':
    main()
