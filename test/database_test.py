import unittest
from src.database import database

class database_test(unittest.TestCase):
    def test_one(self):
        #test adding tickets one
        db = database()
        db.set_tickets([])
        self.assertEqual(db.tickets, [])

    def test_two(self):
        #test adding tickets two
        db = database()
        db.set_tickets([{}])
        self.assertEqual(db.tickets, [{
            'priority' : 'Unspecified',
            'organisation_id' : 'Unspecified',
            'status' : 'Unspecified',
            'due_at' : 'Unspecified',
            'assignee_id' : 'Unspecified',
            'description' : 'Unspecified',
            'subject' : 'Unspecified',
            'type' : 'Unspecified',
            'created_at' : 'Unspecified',
            'email_cc_ids' : '',
            'tags' : ''
        }])

    def test_three(self):
        # pagination test one
        db = database()
        db.set_tickets([{}] * 26)
        self.assertEqual(len(db.get_tickets_paginated(1)), 25) #first page has 25 items
        self.assertEqual(len(db.get_tickets_paginated(2)), 1) # second page has 1

    def test_four(self):
        #pagination test two
        db = database()
        db.set_tickets([{}])
        self.assertEqual(len(db.get_tickets_paginated(1)), 1)  # first page has 1 item

    def test_five(self):
        #page number test
        db = database()
        db.set_tickets([{}] * 26)
        self.assertEqual(len(db.get_page_numbers()), [1,2])


if __name__ == '__main__':
    unittest.main()
