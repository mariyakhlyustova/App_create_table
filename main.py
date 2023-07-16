import interface
import func

def main_prog():
    flag = True
    while flag:
        a = interface.hello()
        if a == '1':
            func.create_table()
        elif a == '2':
            func.add_client(interface.client_info())
        elif a == '3':
            func.json_add_client(interface.path_json())
        elif a == '4':
           func.avg_client_age()
        elif a == '5':
            func.get_client()
        else:
            flag = False

main_prog()