import re
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

'''Log example'''
t = 'Jun  5 19:27:48 Panorama.nogle.com 1,2024/06/05 19:27:48,016201041583,TRAFFIC,end,2562,2024/06/05 19:27:40,165.154.129.130,123.51.190.204,165.154.129.130,10.1.31.77,BI-NAT-Internal System_Style.me Gitlab,,,ssl,vsys1,sdwan,vlan31,ethernet1/2,vlan.31,panorama,2024/06/05 19:27:40,1009045,1,34206,443,34206,443,0x400c1a,tcp,allow,4154,739,3415,11,2024/06/05 19:27:25,1,allurl,,7358049596824040546,0x8000000000000000,United Kingdom,Taiwan,,6,5,tcp-rst-from-client,11,0,0,0,,Xinyi-3220,from-policy,,,0,,0,,N/A,0,0,0,0,4b99d56e-8f04-4ef4-8567-03a392f02d9e,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2024-06-05T19:27:41.583+08:00,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,0'

log = ''

'''Parser Logic'''
def paloalto_traffic(log):
    delimiter = '\,'

    parse = re.split(delimiter, {log})
    parsedlogslist = []
    try:
        parsedlogs = list(filter(None, parse))
        parsedlogslist.append(parsedlogs)
        print(parsedlogslist[0])
    except:
        pass

'''Menu Options'''
def menu_def():
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

    while True:
        if user_input == 's':
            print('What log you want to parse?')
            parsing_option = (
                'pa','gws','cs','x'
            )
            start_input = input('Choose log type: ')
        
            if start_input.lower() in parsing_option:
                if start_input == 'pa':
                    pa_log = input('paste the log here: ')
                    paloalto_traffic(pa_log)
                elif start_input == '':
                    print('Log type is not supported')
        if user_input == 'h':
            print('Supported logs:')
            print('pa = Palo Alto - Traffic log')
            print('gws = Google Workspace - Google Drive Report')
            print('x = Cancel')
            print()
            
        if user_input == 'x':
            exit()
    # while True:
    #     if user_input == 'pa':
    #         log = input('Paste the log here: ')
    #         paloalto_traffic()
    #         break
            
menu_def()



# parsing = paloalto_traffic()
# parsing_exec = menu_def(parsing, )









