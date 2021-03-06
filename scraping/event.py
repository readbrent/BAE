# -*- coding: utf-8 -*-
'''
Event object.

Created by Alice Kroutikova '15
'''
import datetime

class Event(object):
    name = ""
    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()
    info = ""
    category = ""
    
    def __init__(self, name, starttime, endtime, info, category):
        self.name = name 
        self.starttime = starttime
        self.endtime = endtime
        self.info = info
        self.category = category
    
    def __str__(self):
        ret_string = self.name + '\n' + str(self.starttime) + '---' + str(self.endtime) + '\n'
        if isinstance(self.info, unicode):
            ret_string = ret_string + self.info.encode('utf-8')
        else:
            try:
                ret_string = ret_string + self.info
            except UnicodeDecodeError:
                ret_string = ret_string + unicode(self.info, errors='ignore')
        ret_string = ret_string + '\n' + self.category
        return ret_string
    
    def set_info(self, info):
        self.info = info
    
    