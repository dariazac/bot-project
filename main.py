# this is for a task manager

# using classes

# for timestamp later
import time
import datetime


ts = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
# 2018-09-20 19:08:38

y = int(time.strftime("%Y", ts))
m = int(time.strftime("%m", ts))
d = int(time.strftime("%d", ts))
my_date = datetime.date(y, m, d)


# OFF TOPIC


# is_date = time.strftime("%Y-%m-%d", ts)

# if my_date == is_date:
#     print "YES"
# else:
#     print "NOOO"
# print my_date
# print is_date

# methode is a function associated with a class
# new class Project


class Tasker:
    t_count = 0
    t_dur = 0.5

    def __init__(self, t_action, t_obj):  # setting attributes in dunder init
        self.t_action = t_action
        self.t_obj = t_obj
        # self.task = t_action + ' ' + t_obj

        Tasker.t_count += 1  # num of projects
        # print("\ninicialised ", self.task)  # PRINT TEST

    @property
    def task(self):
        return '{} {}'.format(self.t_action, self.t_obj)

    @task.setter
    def task(self, action):
        self.t_action, self.t_obj = action.split(' ')

    @task.deleter
    def task(self):
        print('Delete Name!')
        self.t_action = None
        self.t_obj = None

    def nowtime(self):  # method must take in the instance 'self'
        return time.strftime("%Y-%m-%d %H:%M:%S", ts)

    def set_duration(self, u_dur):  # u for unique duration. this is setting the class variable to a unique value for instance self
        self.t_dur = u_dur
        return self.t_dur

    @classmethod
    def set_default_dur(cls, n_dur):  # n for new. set a new default dur
        cls.t_dur = n_dur
        return cls.t_dur

    @classmethod
    def from_string(cls, proj_str, sep=None):
        if sep is None:

            seps = ["-", ",", "/", ";", ":", " "]
            for i in seps:
                try:
                    t_action, t_obj = proj_str.split(i)

                except ValueError:
                    pass
            try:
                if t_action:
                    # print p_name
                    return cls(t_action, t_obj)
            except UnboundLocalError as e:
                print("\n******* The sepparator is not in our array ******** ", e)
        else:
            t_action, t_obj = proj_str.split(sep)
            return cls(t_action, t_obj)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    # Dunder methods
    def __repr__(self):
        return "Tasker('{}', '{}')".format(self.t_action, self.t_obj)

    def __str__(self):
        return '{} - {}h'.format(self.task, self.t_dur)

    def __add__(self, other):
        a = self.t_dur + other.t_dur
        return "{} and {} will take {}h".format(self.task, other.task, a)


class Project(Tasker):
    t_dur = 2

    def __init__(self, t_action, t_obj, tasks_li=None):  # setting attributes
        super().__init__(t_action, t_obj)

        if tasks_li is None:
            self.tasks_li = []
        else:
            self.tasks_li = tasks_li

    def add_task(self, t):
        if t not in self.tasks_li:
            self.tasks_li.append(t)

    def delete_task(self, t):
        if t in self.tasks_li:
            self.tasks_li.remove(t)

    def print_tasks(self):
        c = 0
        for t in self.tasks_li:
            c += 1
            print('---> ', c, t.task)
        print('\n')

    def __repr__(self):
        return "Project('{}', '{}')".format(self.t_action, self.t_obj)


bot_1 = Project("build", "a bot")
# print(bot_1.task, bot_1.t_dur)
# print(bot_1)

groceries = Tasker("get", "groceries")
print(groceries.task, groceries.t_dur)

# groceries.task = 'bike food'
del groceries.task

print(groceries.task, groceries.t_dur)

dishes = Tasker("clean", "dishes")
# print(dishes.task, dishes.t_dur)

# print(groceries + dishes)

# prj_1 = Project('do', 'something', [dishes])
# print(prj_1.task)
# prj_1.print_tasks()

# prj_1.add_task(groceries)
# prj_1.print_tasks()
###

# str_bot_2 = 'make bot2'
# bot_2 = Project.from_string(str_bot_2)

# # print (bot_2.t_action, bot_2.t_obj)
# print (bot_2.task)


# doesn't work because the sepparator isn't known
# str_bot_3 = 'bot3+table+mooo'
# bot_3 = Project.from_string(str_bot_3)
# print bot_3.p_name, bot_3.p_notes

# print Project.is_workday(my_date)  # DATE

# print "\n"
# print bot_1.p_name, bot_1.set_duration(1)

# print(bot_1.p_name, bot_1.p_dur)
# print(groceries.p_name, groceries.p_dur)

# # print(Project.nowtime(bot_1))
# print "\nchanging default"
# Project.set_default_dur(3)


# print(bot_1.p_name, bot_1.p_dur)
# print(groceries.p_name, groceries.p_dur)

# # print bot_1.p_name, bot_1.set_duration(1)

# print(bot_1.p_name, bot_1.p_dur)
# print(groceries.p_name, groceries.p_dur)
