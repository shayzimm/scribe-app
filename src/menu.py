import sys
from main import Journal, JournalBook

class Menu:
 ''' Displays a list of choices on the terminal for  the user to run '''
 def __init__(self):
      self.journalbook = JournalBook()
      self.choices = {
           "1" : self.show_journals,
           "2" : self.add_journal,
           "3" : self.search_journals,
           "4" : self.quit
        }

 def display_menu(self):
       print(""" 
             Welcome to Scribe
             What would you like to do today?
             1. Show journal entries
             2. Add journal
             3. Search journals
             4. Quit program
             """)

 def run(self):
     ''' Display menu and respond to user choices '''
     while True:
           self.display_menu()
           choice = input("Enter an option: " )
           action = self.choices.get(choice)
           if action:
                action()
           else:
              print("{0} is not a valid choice".format(choice))

 def show_journals(self, journals=None):
     ''' Display all journal entries in journalbook '''
     if not journals:
        journals = self.journalbook.journals
     for journal in journals:
       print("{0}".format(journal.memo))

 def add_journal(self):
     ''' Add a new journal in the JournalBook '''
     memo = input("Your entry: " )
     self.journalbook.new_journal(memo)
     print("Your entry has been added")   

 def search_journals(self):
     ''' Search for a specific journal in the journalbook using the match filter '''
     filter = input("Search for:  ")
     journals = self.journalbook.search_journal(filter)
     self.show_journals(journals)

 def quit(self):
      ''' quit or terminate the program '''
      print("Thank you for using Scribe today")
      sys.exit(0)

if __name__ == "__main__":
    Menu().run()
