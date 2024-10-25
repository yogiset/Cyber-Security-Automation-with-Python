import re

def valid_ip(suspect_ip):
    log_file = """eraab 2022-05-10 6:03:41 192.168.152.148 
    iuduike 2022-05-09 6:46:40 192.168.22.115 
    smartell 2022-05-09 19:30:32 192.168.190.178 
    arutley 2022-05-12 17:00:59 1923.1689.3.24 
    rjensen 2022-05-11 0:59:26 192.168.213.128 
    aestrada 2022-05-09 19:28:12 1924.1680.27.57 
    asundara 2022-05-11 18:38:07 192.168.96.200 
    dkot 2022-05-12 10:52:00 1921.168.1283.75 
    abernard 2022-05-12 23:38:46 19245.168.2345.49 
    cjackson 2022-05-12 19:36:42 192.168.247.153 
    jclark 2022-05-10 10:48:02 192.168.174.117 
    alevitsk 2022-05-08 12:09:10 192.16874.1390.176 
    jrafael 2022-05-10 22:40:01 192.168.148.115 
    yappiah 2022-05-12 10:37:22 192.168.103.10654 
    daquino 2022-05-08 7:02:35 192.168.168.144"""
    
    pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    valid_ip_addresses = re.findall(pattern, log_file)
    
    print(valid_ip_addresses)
    
    if suspect_ip in valid_ip_addresses:
        print("IP Authorized")
    else:
        print("IP Unauthorized")

valid_ip('192.168.152.148')
