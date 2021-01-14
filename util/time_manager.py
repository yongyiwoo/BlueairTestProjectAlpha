import time

class TimeManager(object):
    @staticmethod
    def set_time_24h(time_delay: int):
        """
        set the time for the schedule based on the current time 24h format
        :param time_delay: add n minutes delay to the current time
        :return: a delayed time in str, format "hh:mm"
        """
        # check if the minute + time_delay minute is equal greater than 60, like the time is 17:59
        if int(time.strftime("%M", time.localtime())) + time_delay >= 60:
            minute = str(int(time.strftime("%M", time.localtime())) + time_delay - 60)
            if (int(time.strftime("%H", time.localtime())) + 1) >= 24: # if hour is 23 or 12h format 12
                hour = str(int(time.strftime("%H", time.localtime())) + 1 - 24)
            else:
                hour = str(int(time.strftime("%H", time.localtime())) + 1)
        else:
            minute = str(int(time.strftime("%M", time.localtime())) + time_delay)
            hour = time.strftime("%H", time.localtime())
        time_text = hour + ":" + minute
        return time_text

    @staticmethod
    def set_time_12h(time_delay: int):
        """
        set the time for the schedule based on the current time 12h format
        :param time_delay: add n minutes delay to the current time
        :return: a delayed time in str, format "hh:mm"
        """
        # check if the minute + time_delay minute is equal greater than 60, like the time is 17:59
        if int(time.strftime("%M", time.localtime())) + time_delay >= 60:
            minute = str(int(time.strftime("%M", time.localtime())) + time_delay - 60)
            if (int(time.strftime("%H", time.localtime())) + 1) >= 12: # if 12h format 12
                hour = str(int(time.strftime("%H", time.localtime())) + 1 - 12)
            else:
                hour = str(int(time.strftime("%H", time.localtime())) + 1)
        else:
            minute = str(int(time.strftime("%M", time.localtime())) + time_delay)
            hour = time.strftime("%H", time.localtime())
        time_text = hour + ":" + minute
        return time_text