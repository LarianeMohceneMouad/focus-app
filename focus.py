import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp = r"C:\Users\HP\Desktop\web\temp"
redirect = '127.0.0.1'
websites = ['www.facebook.com', '.facebook.com', 'www.instagram.com', 'instagram.com', 'www.tiktok.com', 'www.snapchat.com', 'www.pinterest.com']
start = int(input("Start Hour (pm):"))
finish = int(input("Finish Hour (pm):"))
while True:
    working_hours = bool(dt(dt.now().year, dt.now().month, dt.now().day, start) <= dt.now() <= dt(dt.now().year, dt.now().month, dt.now().day, finish))
    print(working_hours)
    if working_hours:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write(redirect + '      ' + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)


