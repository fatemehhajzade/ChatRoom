# سلام عزیزم چت روم شما بررسی شد
# مواردی که انجام نشده:
# 1. کاربر باید یوزرنیمش رو وارد کنه 
# و با اون یوزر نیم در چت روم شناخته بشه
# 2. کاربران انلاین نمایش داده نمیشوند(تنها تعدادشون نمایش داده میشه، 
# باید با کلیک بر روی کاربران انلاین بتونیم لیست کاربران انلاین رو ببینیم.)
# 3. پیغام join و leave داده نمیشود.
# 4. مدیریت دیسکانکت در کلاینت ها درسته ولی در سرور ارور میده
# 5. وقتی یکی لفت میده از تعداد کاربران انلاین کم نمیشه



import socket
import threading


clients=[]

def client(conn,addr):

    clients.append(conn)
    print('New client : ' ,addr )

    while True:
        data=conn.recv(1024)
        data=data.decode()

        online_users=str(len(clients))

        for client in clients:
            if client != conn:
                client.sendall(f"CHAT:{data}\n".encode())

        for client in clients:
            client.sendall(f"ONLINE:{online_users}\n".encode())
                

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind(('0.0.0.0', 60000))
    server.listen()

    while True:
        conn, addr= server.accept()
        t=threading.Thread(target=client ,args=(conn,addr))
        t.start()