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


class Project:
    p_count = 0
    p_dur = 5

    def __init__(self, p_name, p_location, p_notes):  # setting attributes
        self.p_name = p_name
        self.p_location = p_location
        # self.p_realtime = p_realtime
        self.p_notes = p_notes

        Project.p_count += 1  # num of projects

    def nowtime(self):  # method must take in the instance 'self'
        return time.strftime("%Y-%m-%d %H:%M:%S", ts)

    def set_duration(self, u_dur):  # u for unique duration. this is setting the class variable to a unique value for instance self
        self.p_dur = u_dur
        return self.p_dur

    @classmethod
    def set_default_dur(cls, n_dur):  # n for new. set a new default dur
        cls.p_dur = n_dur
        return cls.p_dur

    @classmethod
    def from_string(cls, proj_str, separator=None):
        seps = ["-", ",", "/", ";", ":"]
        for i in seps:
            try:
                p_name, p_location, p_notes = proj_str.split(i)
                # for i in seps:
                #     p_name, p_location, p_notes = proj_str.split(i)

            except ValueError:
                pass
        try:
            if p_name:
                # print p_name
                # if cls(p_name, p_location, p_notes):
                return cls(p_name, p_location, p_notes)
        except UnboundLocalError as e:
            print("\n******* The sepparator is not in our array ******** ", e)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

# try:
#      p_name, p_location, p_notes = proj_str.split(i)
# except Exception as e:
#     raise e
# else:
#     pass


class Tasks(Project):
    p_dur = .5

    def __init__(self, p_name, p_location, p_notes, t_diff):  # setting attributes
        super().__init__(p_name, p_location, p_notes)
        self.t_diff = t_diff


bot_1 = Project("bot", "home", "fun")
print(bot_1.p_name, bot_1.p_dur)

groceries = Tasks("groceries", "Irma or Netto", "no", "high")
print(groceries.p_name, groceries.p_dur)

# dishes = Tasks("dishes", "home", "why", "low")

# str_bot_2 = 'bot2/desk/cool'
# bot_2 = Project.from_string(str_bot_2)

# print bot_2.p_name, bot_2.p_notes


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
