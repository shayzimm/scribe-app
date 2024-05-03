import datetime

#Store the next available id for all new journals or recent ones
last_id = 0

class Journal:
    def __init__(self, memo, tags=' '):
        """
        Initialises a new journal entry with memo and tags. Creation date of new journal and id are automatically set.
        :param memo: The content of the journal entry.
        :type memo: str
        :param tags: Optional tags for the journal entry. Default is an empty string.
        :type tags: str, optional
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id  

    def match(self, filter):
        """
        Checks if the journal matches the filter text.
        Return True if it matches exactly, False if it does not match.
        Filter is case-sensitive.

        :param filter: The text to search for in the journal's memo and tags.
        :type filter: str

        :return: True if the journal matches the filter, False otherwise.
        :rtype: bool
        """  
        if filter in self.memo:
            return True
        for tag in self.tags:
            if filter in tag:
                return True
        return False

class JournalBook:   
    '''Represent a collection of journals'''
    def __init__(self):
        '''
        Initialise journalbook with an empty list.

        This method initialises a new instance of JournalBook, which is a collection of Journal entries.
        It creates an empty list to store the journals.

        :return: None
        :rtype: None
        '''
        self.journals = []

    def new_journal(self, memo, tags=''):
        """
        Creates a new journal entry in the journalbook.

        :param memo: The content of the journal entry.
        :type memo: str
        :param tags: Optional tags for the journal entry. Default is an empty string.
        :type tags: str, optional

        :return: None
        :rtype: None
        """
        self.journals.append(Journal(memo, tags))

    def search_journal(self, filter):
        """
        Searches all journal entries that match the filter.

        :param filter: The text to search for in the journal's memo and tags.
        :type filter: str

        :return: A list of Journal objects that match the filter.
        :rtype: list
        """
        return [journal for journal in self.journals if journal.match(filter)]
