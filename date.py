import datetime, time


class Date():

    def __init__(self, date):
        self.date = date

    def date_history(self):
        date_note = datetime.datetime.fromtimestamp(self.date)
        date_now = datetime.datetime.fromtimestamp(int(time.time()))
        time_duration = str(date_now - date_note).split(", ")
        if len(time_duration) == 1:
            if time_duration[0][:1] == '0':
                if time_duration[0][2] == '0':
                    if time_duration[0][3] == '0':
                        result = '1 minute ago...'
                    else:
                        result = time_duration[0][3] + ' minutes ago...'
                else:
                    result = time_duration[0][2:4] + ' minutes ago...'
            else:
                result = time_duration[0][:1] + ' hours ago...'
        else:
            result = time_duration[0] + ' ago...'
        return result


