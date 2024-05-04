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
    
    def search_by_date(self, start_date, end_date):
        """
        Search journal entries by date range.

        Args:
        start_date (datetime.date): Start date of the date range.
        end_date (datetime.date): End date of the date range.

        Returns:
        list: A list of Journal objects that fall within the specified date range.
        """
        return [journal for journal in self.journals if start_date <= journal.creation_date <= end_date]
    
    def search_by_tags(self, tags):
        """
        Search journal entries by tags.

        Args:
        tags (list): A list of tags to search for.

        Returns:
        list: A list of Journal objects that match the specified tags.
        """
        return [journal for journal in self.journals if any(tag in journal.tags for tag in tags)]
    
    def delete_journal(self, journal_id):
        """
        Deletes a journal entry from the journalbook.

        :param journal_id: The id of the journal entry to delete.
        :type journal_id: int

        :return: None
        :rtype: None
        """
        for journal in self.journals:
            if journal.id == journal_id:
                self.journals.remove(journal)
                return True
        return False
