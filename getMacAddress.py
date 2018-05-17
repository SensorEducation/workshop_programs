def getMAC():
    try:
        mac_addr = open('/sys/class/net/wlan0/address').read()
        return mac_addr[0:17]
    except Exception as e:
        return e
    
mac_address = str(getMAC())
print mac_address.replace(":","")
