import re
import time

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
            return user_input
        else:
            print('Option is not in the menu!')

def parser_menu_def(user_input):
    if user_input == 's':
        print('What log do you want to parse?')
        parsing_options = ('pa', 'gws', 'cs', 'x')
        
        while True:
            start_input = input('Choose log type: ')
            if start_input.lower() in parsing_options:
                return start_input
            else:
                print('Log type is not supported')
                
    elif user_input == 'h':
        print('Supported logs:')
        print('pa = Palo Alto - Traffic log')
        print('gws = Google Workspace - Google Drive Report')
        print('cs = Custom log')
        print('x = Cancel')
        print()
        
    elif user_input == 'x':
        exit()

def parser_submenu_def(log_type):
    if log_type in ('pa', 'gws', 'cs'):
        logs = input('Paste the log here: ')
        return logs
    elif log_type == 'x':
        exit()
    else:
        print('Log type is not supported')
        return None

def pa_parser(logs):
    delimiter = ','
    parse = re.split(delimiter, logs)
    # print(parse)
    parsedlogs = list(filter(None, parse))
    # print(parsedlogs)
    for field in parsedlogs:
        print(field)
    return parsedlogs
    



def main():
    user_input = main_menu_def()
    if user_input == 's':
        log_type = parser_menu_def(user_input)
        if log_type == 'pa':
            logs = parser_submenu_def(log_type)
            if logs:
                print(f"Log received: {logs}")
                print()
                print('Processing...')
                time.sleep(2)
                pa_parser(logs)
                return pa_parser
        elif log_type == 'gws':
            logs = parser_submenu_def(log_type)
            if logs:
                print(f"Log received: {logs}")
                print()
                print('Processing...')
                time.sleep(2)
                pa_parser(logs)
                return pa_parser
    elif user_input == 'h':
        parser_menu_def(user_input)

# Run the main function
main()