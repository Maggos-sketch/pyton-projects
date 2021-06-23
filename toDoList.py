# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

base = declarative_base()

class TaskTable(base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())
    def __inint__(self):
        self.task = 'Nothing to do!'
    def __repr__(self):
        return task

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

now = datetime.now()
tupik = 0
def vyv():
    print('''    
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')

while True:
    if tupik == 0:
        vyv()
        action = input()
    else:
        action = input()

    if action == '1':
        today = datetime.today().date()
        rows = session.query(TaskTable).filter(TaskTable.deadline == today).all()
        if rows:
            print('')
            print(f'Today {today.strftime("%d %b")}:')
            for key in rows:
                print(key.task, key.deadline)
        else:
            print("Nothing to do!")

    elif action == '2':
        for i in range(0,8):
            day = now + timedelta(days=i)
            rows = session.query(TaskTable).filter(TaskTable.deadline == day.date()).all()
            if rows:
                count = 1
                print('')
                print (day.strftime("%A %d %b:"))
                for key in rows:

                    print(f'{count}. {key.task} {key.deadline}')
                    count += 1
            else:
                print('')
                print (day.strftime("%A %d %b:"))
                print("Nothing to do!")
            tupik += 1
    elif action =='3':
        rows = session.query(TaskTable).order_by(TaskTable.deadline).all()
        print("")
        print("All tasks:")
        count = 1
        for key in rows:
            print(f'{count}. {key.task}. {key.deadline.strftime("%#d %b")}') # #-убирает отступ
            count +=1
    elif action =='4':
        rows = session.query(TaskTable).filter(TaskTable.deadline < datetime.today().date()).order_by(TaskTable.deadline).all()
        print('Missed tasks:')
        count = 1
        if rows:
            for key in rows:
                print(f'{count}. {key.task}. {key.deadline.strftime("%#d %b")}')
                count +=1
        else:
            print('Nothing is missed!')

    elif action == '5':
        print('''Enter task''')
        task = input()
        print('Enter deadline')
        day_d = input()

        new_row = TaskTable(task = task,
                            deadline = datetime.strptime(day_d, format("%Y-%m-%d")).date())
        session.add(new_row)
        session.commit()
        print('''The task has been added!''')
    elif action == '6':
        rows = session.query(TaskTable).order_by(TaskTable.deadline).all()
        print('Chose the number of the task you want to delete:')
        count = 1
        for key in rows:
            print(f'{count}. {key.task}. {key.deadline.strftime("%#d %b")}') # #-убирает отступ
            count +=1
        numb = int(input())
        cc = 1
        for key in rows:
            if numb == cc:
                d_id = key.id
                session.query(TaskTable).filter(TaskTable.id == d_id).delete()
                session.commit()
                print("The task has been deleted!")
            cc += 1
    elif action == '0':
        print('''
Bye!''')
        quit()
