with open('login.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    mac_addr = line.split('|')[0].strip()
    log_time = line.split('|')[1].strip()
    status = line.split('|')[2].strip()
    print(mac_addr, log_time, status)
    break
