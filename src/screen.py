from src.subcomponent import subcomponent
from src.database import database

class screen:
    def __init__(self, screenwidth=100):
        self.screenwidth = screenwidth
        self.current_page_no = 1

    def display_error(self, error):
        sub = subcomponent(self.screenwidth)
        sub.set_display_str('Error: ' + error)
        return [sub]

    def display_exit(self, exit_code=0):
        sub = subcomponent(self.screenwidth)
        if exit_code == 0:
            sub.set_display_str('Goodbye')
        else:
            sub.set_display_str('Exiting')

        return [sub]

    def table_footer(self):
        contents = [
            'Available actions:',
            '\t enter page number to go to that page e.g. page 1',
            '\t enter ticket number on the table to go to the ticket e.g. ticket 5',
            '\t enter exit to exit'
        ]

        subs = []
        for content in contents:
            sub = subcomponent(self.screenwidth)
            sub.set_display_str(content)
            subs.append(sub)

        return subs

    def ticket_footer(self):
        contents = [
            'Available actions:',
            '\t enter back to return to the table page',
            '\t enter exit to exit'
        ]

        subs = []
        for content in contents:
            sub = subcomponent(self.screenwidth)
            sub.set_display_str(content)
            subs.append(sub)

        return subs

    def create_table_of_contents(self, page_no=1):
        if database.database is None:
            return None

        db = database.database

        if page_no <= 0 or page_no > max(db.get_page_numbers()):
            return None
        self.current_page_no = page_no
        tickets = db.get_tickets_paginated(page_no)
        header = subcomponent(self.screenwidth)
        header.set_display_str('Number ::: subject ::: created date')
        contents = [header]
        for cnt, ticket in enumerate(tickets):
            sub = subcomponent(self.screenwidth)
            ticket_subject = ticket['subject']
            created_at = ticket['created_at']
            sub.set_display_str(str(cnt + 1) + ' ::: ' + ticket_subject + ' :::  ' + created_at)
            contents.append(sub)

        return contents

    def get_page_numbers(self):
        if database.database is None:
            return None

        db = database.database

        page_range = [str(x) for x in db.get_page_numbers()]
        sub = subcomponent(self.screenwidth)
        sub.set_display_str('\n\nPage Range to choose from: ' + ','.join(page_range))

        return [sub]

    def create_ticket(self, ticket_no):
        features_in_order_of_display = ['status', 'priority', 'due_at', 'type',
                                        'email_cc_ids', 'organisation_id', 'subject',
                                        'description', 'created_at', 'assignee_id', 'tags']
        if database.database is None:
            return None

        db = database.database

        if ticket_no <= 0 or ticket_no > len(db.tickets):
            return None

        ticket = db.tickets[ticket_no]
        ticket_display = []

        for feature in features_in_order_of_display:
            print(feature)
            sub = subcomponent(self.screenwidth)
            disp = str(ticket[feature]) if feature in ticket else ' '
            disp = self.snake_to_words(feature) + ': ' + disp
            sub.set_display_str(disp)
            ticket_display.append(sub)

        return ticket_display

    def snake_to_words(self, text):
        return ' '.join(x.capitalize() for x in text.split('_'))