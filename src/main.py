import datetime

#Store the next available id for all new diaries or recent ones
last_id = 0

class Journal:
   '''Represents a journal entry'''
   def __init__(self, memo, tags=' '):
       '''Initialises a new journal entry with memo and tags. Creation date of new journal and id are automatically set'''
       self.memo = memo
       self.tags = tags
       self.creation_date = datetime.date.today()
       global last_id
       last_id +=1
       self.id = last_id  

   def match(self, filter):
        '''checks if the journal matches the filter text.
        Return true if it matches exactly, false if it does not match. 
        Filter is case-sensitive'''  
        if filter in self.memo:
            return True
        for tag in self.tags:
            if filter in tag:
                return True
        return False
