import json


def main():
    info_file = open('info.json', 'r')
    info_str = json.load(info_file)
    print(info_str)
    print(info_str['hobbies'])
    print(len(info_str['hobbies']))

    children_dict = info_str['children']
    if children_dict[0]['age'] > children_dict[1]['age']:
        print(children_dict[0]['firstName'])
    else:
        print(children_dict[1]['firstName'])

    info_str['email'] = 'jone@company.com'
    info_str['phone'] = 83836638
    file_json2 = open('info2.json', 'w')
    file_json2.write(json.dumps(info_str))

main()
