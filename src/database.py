class database:
    database = None

    def __init__(self):
        database.database = self

    def set_tickets(self, tickets):
        keys_we_want_to_extract = ['priority', 'organisation_id', 'status', 'due_at', 'assignee_id', 'description', 'subject',  'type', 'created_at']
        keys_to_join = ['email_cc_ids', 'tags']
        self.tickets = []

        for ticket in tickets:
            ticket_to_be_saved = {}

            for key in keys_we_want_to_extract:
                if key in ticket and ticket[key] is not None:
                    ticket_to_be_saved[key] = ticket[key]
                else:
                    ticket_to_be_saved[key] = 'Unspecified'

            for key in keys_to_join:
                if key in ticket and (ticket[key] is not None or ticket[key] is not []):
                    ticket_to_be_saved[key] = ', '.join(ticket[key])
                else:
                    ticket_to_be_saved[key] = ''

            self.tickets.append(ticket_to_be_saved)

    def get_tickets_paginated(self, page_no, page_size=25):
        ranges = list(range(1,len(self.tickets), page_size))
        if page_no > 0 and page_no <= len(ranges):
            return self.tickets[ranges[page_no]: min(ranges[page_no] + page_size, len(self.tickets))]
        else:
            return self.tickets[:min(page_size, len(self.tickets))]

    def get_page_numbers(self, page_size=25):
        return list(range(1, len(range(1, len(self.tickets), page_size)), 1))