'''Menu Options'''
def main_menu_def():
    menu_options = ('s', 'h', 'x')

    while True:
        print('**MENU**')
        print('s = start')
        print('h = help')
        print('x = exit')

        print()
        user_input = input('Enter an option: ')

        if user_input.lower() in menu_options:
            break
        else:
            print('Option is not in the menu!')
    return user_input
def parser_menu_def(user_input):
    while True:
        if user_input == 's':
            print('What log you want to parse?')
            parsing_option = (
                'pa','gws','cs','x'
            )
            start_input = input('Choose log type: ')
            if start_input.lower() in parsing_option:
                abc = start_input
        
        elif user_input == 'h':
            print('Supported logs:')
            print('pa = Palo Alto - Traffic log')
            print('gws = Google Workspace - Google Drive Report')
            print('x = Cancel')
            print()
            
        elif user_input == 'x':
            exit()
        return abc

def parser_submenu_def(abc):
    while True:
        if abc == 'pa':
            logs = input('paste the log here: ')
            break
        elif abc == 'gws':
            logs = input('paste the log here: ')
            break
        elif abc == 'cs':
            logs = input('paste the log here: ')
            break
        elif abc == 'x':
            exit()
        else:
            print('Log type is not supported')
            break
    return logs
    # while True:
    #     if user_input == 'pa':
    #         log = input('Paste the log here: ')
    #         paloalto_traffic()
    #         break
            
main_menu_def()
parser_menu_def()
parser_menu_def()
