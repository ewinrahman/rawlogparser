import json

# Example nested JSON content
# json_content = r'''{"actor":{"email":"ck.chong@nogle.com","profileId":"100010624688399114977"},"etag":"\"7ZXXkx9deOwnsnM0BDqnP0Ppr5sUNSSSAkJ9tGcjgWU/QI6G1QY3CvpcndWmdGdpoOTxj0c\"","events":[{"name":"view","parameters":[{"boolValue":true,"name":"primary_event"},{"boolValue":true,"name":"billable"},{"boolValue":false,"name":"owner_is_shared_drive"},{"name":"owner","value":"hera.chen@nogle.com"},{"name":"doc_id","value":"1fsuowSb_d3pDsHxSrIbgblb7SNZYDfMUKdLeWYWjgPY"},{"name":"doc_type","value":"spreadsheet"},{"boolValue":false,"name":"is_encrypted"},{"name":"doc_title","value":"EP/ SPass Process"},{"name":"visibility","value":"shared_internally"},{"name":"originating_app_id","value":"1082607815231"},{"boolValue":false,"name":"actor_is_collaborator_account"},{"boolValue":false,"name":"owner_is_team_drive"}],"type":"access"}],"id":{"applicationName":"drive","customerId":"C044erl4x","time":"2024-06-21T04:24:44.522Z","uniqueQualifier":"-3983025742742309355"},"ipAddress":"2601:644:9385:58c0:1452:662d:95ee:be04","kind":"admin#reports#activity"}

data = input('here: ')





def print_nested_json(data, indent=0):
    data = data.replace('\\"', '')
    data = json.loads(data)
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + f'{key}:')  # Print the key with indentation
            print_nested_json(value, indent + 1)  # Recursive call for nested data
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print('  ' * indent + f'[{i}]:')  # Print the index with indentation
            print_nested_json(item, indent + 1)  # Recursive call for list items
    else:
        print('  ' * indent + str(data))  # Print the value with indentation

# Print the entire JSON structure
print_nested_json(data)