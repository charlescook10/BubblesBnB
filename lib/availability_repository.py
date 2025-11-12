from lib.availability import Availability


class AvailabilityRepository:

    def __init__(self, connection):
        self._connection = connection
    def getDates(self, space_id):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE space_id= %s',[space_id])
        dates = []
        for row in rows:
            date = Availability(row['id'], row['date'], row['status'], row['space_id'])
            dates.append(date)
        return dates 
        

    