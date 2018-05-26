

from google.appengine.ext import ndb


class Temp(ndb.Model):

    id = ndb.StringProperty()
    url = ndb.StringProperty()


    @staticmethod
    def getTemp():
        return Temp.query()


