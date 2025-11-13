from lib.availability import Availability



class AvailabilityRepository:

    def __init__(self, connection):
        self._connection = connection
        
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE id= %s',[id])
        row = rows[0]

        return Availability(row['id'], row['date'], row['status'], row['space_id'])
    
    def findByDate(self, space_id, date):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE space_id=%s AND date= %s',[space_id, date])
        row = rows[0]

        return Availability(row['id'], row['date'], row['status'], row['space_id'])

    def getSpaceDates(self, space_id):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE space_id= %s ORDER BY date',[space_id])
        dates = []
        for row in rows:
            date = Availability(row['id'], row['date'], row['status'], row['space_id'])
            dates.append(date)
        return dates 
    
    def getAvailableSpaceDates(self, space_id):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE space_id= %s AND status=\'Available\' ORDER BY date',[space_id])
        dates = []
        for row in rows:
            date = Availability(row['id'], row['date'], row['status'], row['space_id'])
            dates.append(date)
        return dates 
    
    def addRange(self, space_id, start_date, end_date):
        self._connection.execute('INSERT INTO availabilities(date, space_id) SELECT gs::date, %s FROM generate_series(%s::date, %s::date, \'1 day\'::interval) AS gs' ,[space_id, start_date, end_date])
        
        return None
    
    def book(self, id):
        self._connection.execute('UPDATE availabilities SET status=\'Booked\' WHERE id = %s' ,[id])
        
        return None
    