from src.screen import screen
from src.subcomponent import subcomponent
from src.database import database
from src.zcc_api import zcc_api
from src.config import username, token
import traceback
import os

class app:
    def __init__(self):
        self.scr = screen()
        try:
            api = zcc_api()
            resp = api.get_tickets(username=username, token=token)

            if 'error' in resp or 'tickets' not in resp:
                contents = self.scr.display_error('Error in api')
                self.display(contents)
                self.display(self.scr.display_exit(1), clear=False)
                traceback.print_exc()
                exit(1)

            tickets = resp['tickets']

            data = database()
            data.set_tickets(tickets)
        except:
            sub = subcomponent(self.scr.screenwidth)
            sub.set_display_str('Unknown error')
            self.display([sub])
            self.display(self.scr.display_exit(1), clear=False)
            traceback.print_exc()
            exit(1)

    def run(self):
        try:
            invalid_command = subcomponent(self.scr.screenwidth)
            invalid_command.set_display_str('Invalid command')
            display_invalid_command = False

            contents = self.scr.create_table_of_contents(1)
            contents = contents + self.scr.get_page_numbers()
            contents = contents + self.scr.table_footer()
            on_page = 'TABLE'
            while True:
                self.display(contents)
                if display_invalid_command:
                    self.display([invalid_command], clear=False)
                    display_invalid_command = False
                command = input('Enter a command: ')
                command = command.strip().lower()

                if command.startswith('exit'):
                    self.display(self.scr.display_exit())
                    exit(0)

                if on_page == 'TABLE':
                    if command.startswith('page'):
                        page_no = command.split()
                        if len(page_no) > 1 and page_no[1].isnumeric():
                            new_contents = self.scr.create_table_of_contents(int(page_no[1]))
                            if new_contents is not None:
                                contents = new_contents
                                contents = contents + self.scr.get_page_numbers()
                                contents = contents + self.scr.table_footer()
                        else:
                            display_invalid_command = True
                    elif command.startswith('ticket'):
                        ticket_no = command.split()
                        if len(ticket_no) > 1 and ticket_no[1].isnumeric():
                            ticket_no = self.scr.current_page_no * 25 + int(ticket_no[1])
                            new_contents = self.scr.create_ticket(ticket_no)
                            if new_contents is not None:
                                contents = new_contents
                                contents = contents + self.scr.ticket_footer()
                                on_page = 'TICKET'
                        else:
                            display_invalid_command = True
                    else:
                        display_invalid_command = True
                else:
                    if command.startswith('back'):
                        page_no = self.scr.current_page_no
                        contents = self.scr.create_table_of_contents(page_no)
                        contents = contents + self.scr.get_page_numbers()
                        contents = contents + self.scr.table_footer()
                        on_page = 'TABLE'
                    else:
                        display_invalid_command = True
        except Exception as e:
            contents = self.scr.display_error('Unknown error')
            self.display(contents)
            self.display(self.scr.display_exit(1), clear=False)
            traceback.print_exc()
            exit(1)


    def display(self, contents, clear = True):
        if clear: os.system('cls||clear')
        for content in contents:
            print(content.get_display())