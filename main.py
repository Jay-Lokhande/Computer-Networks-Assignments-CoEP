import ipaddress

print("You can calculate Network Address & Broadcast Address")
classSelect = input("Select the class (A, B, C): ")

defSubnet = {"A": ["255.0.0.0", "0.0.0.0 to 127.255.255.255", "8"],
             "B": ["255.255.0.0", "128.0.0.0 to 191.255.255.255", "16"],
             "C": ["255.255.255.0", "192.0.0.0 to 223.255.255.255", "24"]}
print(f'Default Subnet mark of class {classSelect} is {defSubnet[classSelect][0]}\nclass {classSelect} IP Address Range: {defSubnet[classSelect][1]}')

numOfSubnet = int(defSubnet[classSelect][2])

var = input("Enter the IP address (eg. 192.168.1.50):\n")

while(True):
    cidr = int(input("CIDR Value: \n/"))
    if (cidr == 8):
        subnetMask = "255.0.0.0"
        break
    elif (cidr == 9):
        subnetMask = "255.128.0.0"
        break
    elif (cidr == 10):
        subnetMask = "255.192.0.0"
        break
    elif (cidr == 11):
        subnetMask = "255.224.0.0"
        break
    elif (cidr == 12):
        subnetMask = "255.240.0.0"
        break
    elif (cidr == 13):
        subnetMask = "255.248.0.0"
        break
    elif (cidr == 14):
        subnetMask = "255.252.0.0"
        break
    elif (cidr == 15):
        subnetMask = "255.254.0.0"
        break
    elif (cidr == 16):
        subnetMask = "255.255.0.0"
        break
    elif (cidr == 17):
        subnetMask = "255.255.128.0"
        break
    elif (cidr == 18):
        subnetMask = "255.255.192.0"
        break
    elif (cidr == 19):
        subnetMask = "255.255.224.0"
        break
    elif (cidr == 20):
        subnetMask = "255.255.240.0"
        break
    elif (cidr == 21):
        subnetMask = "255.255.248.0"
        break
    elif (cidr == 22):
        subnetMask = "255.255.252.0"
        break
    elif (cidr == 23):
        subnetMask = "255.255.254.0"
        break
    elif (cidr == 24):
        host = 00000000
        subnetMask = "255.255.255.0"
        break
    elif (cidr == 25):
        host = 128
        subnetMask = "255.255.255.128"
        break
    elif (cidr == 26):
        host = 192
        subnetMask = "255.255.255.192"
        break
    elif (cidr == 27):
        host = 224
        subnetMask = "255.255.255.224"
        break
    elif (cidr == 28):
        host = 240
        subnetMask = "255.255.255.240"
        break
    elif (cidr == 29):
        host = 248
        subnetMask = "255.255.255.248"
        break
    elif (cidr == 30):
        host = 252
        subnetMask = "255.255.255.252"
        break
    else:
        print("Please put valid CIDR Value from 8-30")


print(f'IP adress is   - {var}')
print(f"Subnet mask is - {subnetMask}")
print(f'Number of Subnet: {2**(32-cidr)}')
print(f'Number of Host per Subnet: {2**(32-cidr) - 2}')
ip_parts = [int(part) for part in var.split('.')]
subnet_parts = [int(part) for part in subnetMask.split('.')]
network_address = [ip & subnet for ip, subnet in zip(ip_parts, subnet_parts)]
broadcast_parts = [(ip | (~subnet)) & 255 for ip, subnet in zip(ip_parts, subnet_parts)]

broadcast_address_str = '.'.join(map(str, broadcast_parts))

network_address_str = '.'.join(map(str, network_address))
broadcast_address_str = '.'.join(map(str, broadcast_parts))
print("Network ID: ", network_address_str)
print("BroadCast ID: ", broadcast_address_str)



















# a = int(bin(var), 2)
# b = int(bin(host), 2)
# hosts = bin(host)
# ones_complement = ''.join('1' if bit == '0' else '0' for bit in hosts[3:])
# print(ones_complement)
# network_address = a & b
# broadcast_address = a | int(ones_complement, 2)
# print(f"Network Address is - 192.168.1.{network_address}")
# print(f"Broadcast Address is - 192.168.1.{broadcast_address}")









# print("Classes	range"
# "A	0 to 127"
# "B	128 to 191"
# "C	192 to 223"
# "D	224 to 239"
# "E	240 to 255")
# print("Classes	Default mask A	255.0.0.0 B	255.255.0.0 C	255.255.255.0")
# rem = ""
# rem2 = ""
# while(var != 0):
#     if (var % 2 == 0):
#         rem += "0"
#     else:
#         rem += "1"
#     var //= 2
#
# while(host != 0):
#     if (host % 2 == 0):
#         rem2 += "0"
#     else:
#         rem2 += "1"
#     host //= 2
#
# print(rem[::-1])
# print(rem2[::-1])



