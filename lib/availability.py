class Availability:
 def __init__(self, id, date, status, space_id):
  self.id = id
  self.date = date
  self.status = status
  self.space_id = space_id
  
 def __eq__(self, other):
  return self.__dict__ == other.__dict__
    
 def __repr__(self):
  return f"Availability({self.id}, {self.date}, {self.status}, {self.space_id})"