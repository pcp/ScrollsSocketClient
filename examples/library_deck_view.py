import os
import sys
# add the parent dir to the path for this example
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from ScrollsSocketClient import ScrollsSocketClient

email = 'user@example.com'
password = 'password'
deck = 'Growth Preconstructed'


def run(message):
    """ This function is executed upon receiving the 'SignIn' event """

    # unsubscribe from the SignIn event
    scrolls.unsubscribe('SignIn')

    # subscribe to the LibraryView event with function library_view()
    scrolls.subscribe('LibraryView', library_view)
    scrolls.send({'msg': 'LibraryView'})

    # subscribe to the DeckCards event with function deck()
    scrolls.subscribe('DeckCards', deck_view)
    scrolls.send({'msg': 'DeckCards', 'deck': deck})


def library_view(message):
    """ This function is executed upon receiving the 'LibraryView' event """

    # unsubscribe from the LibraryView event
    scrolls.unsubscribe('LibraryView')
    print message


def deck_view(message):
    """ This function is executed upon receiving the 'DeckCards' event """

    # unsubscribe from the DeckCards event
    scrolls.unsubscribe('DeckCards')
    print message

    # quit
    print 'Exiting...'
    scrolls.quit()


# give the client our username/password
scrolls = ScrollsSocketClient(email, password)

# subscribe to the SignIn event with function run()
scrolls.subscribe('SignIn', run)

# login to the server
scrolls.login()
