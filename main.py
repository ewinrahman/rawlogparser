import re
import json
import time

''' Raw log splitter information/template (Important fields only):
    end,2562,2024/06/05 19:27:40,165.154.129.130,123.51.190.204,165.154.129.130,10.1.31.77,BI-NAT-Internal System_Style.me Gitlab,,,ssl,vsys1,sdwan,vlan31,ethernet1/2,vlan.31,panorama,2024/06/05 19:27:40,1009045,1,34206,443,34206,443,0x400c1a,tcp,allow,4154,739,3415,11,2024/06/05 19:27:25,1,allurl,,7358049596824040546,0x8000000000000000,United Kingdom,Taiwan,,6,5,tcp-rst-from-client,11,0,0,0,,Xinyi-3220,from-policy,,,0,,0,,N/A,0,0,0,0,4b99d56e-8f04-4ef4-8567-03a392f02d9e,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2024-06-05T19:27:41.583+08:00,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,0 
    - [1]  -> Event Timestamp (2024/06/05 19:27:48)
    - [3]  -> Event Type (TRAFFIC)
    - [4]  -> 
    - [7]  -> Source IP 
    - [8]  -> Destination IP
    - [9]  -> NAT Source IP 
    - [10] -> NAT Destination IP
    - [11] -> Rule Policy
    - [12] -> Application
    - [22] -> Source Port
    - [23] -> Destination Port
    - [24] -> NAT Source Port
    - [25] -> NAT Destination Port
ref: 
- Traffic: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/traffic-log-fields#idbe18d2d4-9eb8-4966-bec8-df3a6de70e66
- Threat: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/threat-log-fields#id83052cb2-4798-4f9c-abf8-e0b929ce7a3b
'''


'''Menu & Sub-Menu Functions'''
def main_menu_def():
    menu_options = ('s', 'h', 'x')

    while True:
        print('')
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
    
'''Parser Functions'''
def pa_parser(logs):
    delimiter = ','
    parse = re.split(delimiter, logs)
    parsedlogs = list(filter(None, parse))
    for field in parsedlogs:
        print(field)
    return parsedlogs

def gws_parser(logs, indent=0):
    if isinstance(logs, dict):
        for key, value in logs.items():
            print('  ' * indent + f'{key}:')  # Print the key with indentation
            gws_parser(value, indent + 1)  # Recursive call for nested data
    elif isinstance(logs, list):
        for i, item in enumerate(logs):
            print('  ' * indent + f'[{i}]:')  # Print the index with indentation
            gws_parser(item, indent + 1)  # Recursive call for list items
    else:
        print('  ' * indent + str(logs))  # Print the value with indentation

def main():
    user_input = main_menu_def()
    if user_input == 's':
        log_type = parser_menu_def(user_input)
        if log_type == 'pa':
            logs = parser_submenu_def(log_type)
            if logs:
                print(f"Log received: {logs}")
                print('Processing...')
                time.sleep(2)
                pa_parser(logs)
                return pa_parser
        elif log_type == 'gws':
            logs = parser_submenu_def(log_type)
            if logs:
                print(f"Log received: {logs}")
                logs = logs.replace('\\"', '')
                logs = json.loads(logs)
                print()
                print('Processing...')
                time.sleep(2)
                gws_parser(logs)
                return gws_parser
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









