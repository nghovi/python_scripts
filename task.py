#!/user/bin/python
import time
import datetime
import sqlite3_api
class MyTask:
	"""DO NOT USE THIS SCRIPT
		MyTask is used for test Python tutorial, and will be useful later

		Attributes:
			id -- auto increment in database
			type -- 0: daily, 1: scheduled
			brief -- short description of task
			description -- details of task
			start_date -- start_date time
			end_date -- end_date time
			status -- 0 unfinished or expired, 1 don"e
						rate -- range from 1, 10
	"""
	def __init__(self,
		type,
		brief,
		description,
		start_date=datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y %H:%M:%S'),
		end_date='12-03-2090 23:59:59',
		status=0,
		rate=0,
		id=0):
		self.type = type
		self.brief = brief
		self.description = description
		self.start_date = start_date
		self.end_date = end_date
		self.status = status
		self.rate = rate
		self.id = id

	def rate(self, rating):
		self.rate = rate

	def set_state(self, status):
		self.status = status

	def show(self):
		return str(self.type) + self.get_delimeter() + str(self.status) + self.get_delimeter() + self.brief + self.get_delimeter() + self.description + self.get_delimeter() + str(self.start_date) + self.get_delimeter() + str(self.end_date) + self.get_delimeter() + str(self.rate) + "\n"

	def toTuple(self):
		return self.type, self.brief, self.description, self.start_date, self.end_date, self.status, self.rate

	#todo update
	def save_to_database(self):
		new_row = self.type, self.brief, self.description, self.start_date, self.end_date, self.status, self.rate
		if not self.id:
			sqlite3_api.insert(db_name='C:\Python27\python_scripts\\task.db', query_str="insert into task(type, brief, description, start_date, end_date, status, rate) values(?,?,?,?,?,?,?)", data=new_row)
		else:
			sqlite3_api.update(db_name='C:\Python27\python_scripts\\task.db', query_str="update task set type={0}, brief={1}, description={2}, start_date={3}, end_date={4}, status={5}, rate={6} where id={7}".format(
				new_row + (self.id,)))

	@staticmethod
	def get_delimeter():
		return "||||"


############################### Task Management ###########################################3
def manage_task():
    """This is simple GUI for task management

    """
    choice = 1
    while choice:
        print '=================Task Management Menu========================'
        print '0: Exit'
        print '1: View unfinished task'
        print '2: Add new task'
        print '3: Finish task'
        print 'Your select:'
        choice = int(raw_input().strip())
        if choice == 0:
            print 'Goodbye, sir'
            break
        elif choice == 1:
            print_unfinished_task()
        elif choice == 2:
            create_new_task()
        elif choice == 3 :
            finish_task()
        else:
            print 'Your choice is not in database!'

def create_new_task():
    print "Type: (0:daily, 1: scheduled):"
    type = int(raw_input().strip())
    print "Brief:"
    brief = raw_input().strip()
    print "Description:"
    description = raw_input().strip()
    print "start_date:"
    start_date = raw_input().strip()
    print "end_date:"
    end_date = raw_input().strip()
    new_task = MyTask(type, brief, description, start_date, end_date);
    new_task.save_to_database()

def print_all_task():
    tasks = sqlite3_api.select('C:\Python27\python_scripts\\task.db', query_str='select * from task')
    for task_i in tasks:
        for k, v in task_i.iteritems():
            print k, ': ', v
        print "------------------------------------------------------------------------------"

def print_unfinished_task():
    tasks = sqlite3_api.select('C:\Python27\python_scripts\\task.db', query_str="SELECT * FROM task;")
    for task_i in tasks:
        for k, v in task_i.iteritems():
            print k, ': ', v
        print "------------------------------------------------------------------------------"

def finish_task():
    print "Choose task id to finish:"
    id = raw_input().strip()
    print "Your rate:"
    rate = raw_input().strip()
    sqlite3_api.update('C:\Python27\python_scripts\\task.db', query_str='update task set status = 1, rate = {0} where id={1}'.format(rate, id))