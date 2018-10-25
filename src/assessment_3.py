
INVALID_NEXT_IP = '255.255.255.255'

def nextip(ipaddr):
    '''To find next possible IP address available'''
    # if the input IP is max IP then no addr other that it
    if ipaddr == INVALID_NEXT_IP:
        return "No more IP address available"
    ip = ipaddr.split(".")
    # convert the string list to int list
    ip = list(map(lambda x:int(x),ip))
    ip[3]+= 1
    # reverse the list
    for i in range(len(ip)-1,0,-1):
        if ip[i] > 255:
            ip[i-1] += 1
            ip[i] = 0
    # convert int list to a string
    nextipaddr = '.'.join(str(i) for i in ip)
    return nextipaddr

myip = "255.252.255.255"
print("Next IP address available is",nextip(myip))