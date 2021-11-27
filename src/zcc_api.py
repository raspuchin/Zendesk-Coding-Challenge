import requests
import traceback

class zcc_api():

    def __init__(self) -> None:
        pass

    def get_tickets(self, url='https://zccpothukuchi.zendesk.com/api/v2/tickets.json?', username='', token=''):
        try:
            auth = requests.auth.HTTPBasicAuth(username + '/token', token)
            r = requests.get(url, auth=auth)
        except:
            r = {'error' : 'Error occured'}
            f = open('error.log', 'r')
            f.write(traceback.print_exc())

        return r.json()