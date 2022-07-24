import datetime, time


class Date():

    def __init__(self, date):
        self.date = date

    def date_history(self):
        time_str = {0: " hours ago...", 1: " minutes ago...", 2: " seconds...", 3:" ago..."}

        date_note = datetime.datetime.fromtimestamp(self.date)
        date_now = datetime.datetime.fromtimestamp(int(time.time()))
        time_duration = str(date_now - date_note).split(", ")
        if len(time_duration) == 1:
            time_duration = str(time_duration[0]).split(":")
            for i in range(len(time_duration)):
                result = int(time_duration[i])
                if result > 0:
                    return (str(result) + time_str[i])
        else:
            return (time_duration[0] + time_str[3])


