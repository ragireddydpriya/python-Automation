import os

#--------------------------------------------------------------------------------------------------------
# 1.ping -n 6 8.8.8.8
#---------------------------------------------------------------------------------------------------------
# (uhnder) PS D:\secondAssignment> ping -n 6 8.8.8.8

# Pinging 8.8.8.8 with 32 bytes of data:
# Reply from 8.8.8.8: bytes=32 time=92ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=38ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=48ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=35ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=88ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=72ms TTL=120

# Ping statistics for 8.8.8.8:
#     Packets: Sent = 6, Received = 6, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 35ms, Maximum = 92ms, Average = 62ms
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# 2.ping -a  8.8.8.8
#---------------------------------------------------------------------------------------------------------
# (uhnder) PS D:\secondAssignment> ping -a 8.8.8.8

# Pinging dns.google [8.8.8.8] with 32 bytes of data:
# Reply from 8.8.8.8: bytes=32 time=53ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=41ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=40ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=38ms TTL=120

# Ping statistics for 8.8.8.8:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 38ms, Maximum = 53ms, Average = 43ms
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# 3.ping -l 64 8.8.8.8
#---------------------------------------------------------------------------------------------------------
# (uhnder) PS D:\secondAssignment> ping -l 64 8.8.8.8

# Pinging 8.8.8.8 with 64 bytes of data:
# Reply from 8.8.8.8: bytes=64 time=37ms TTL=120
# Reply from 8.8.8.8: bytes=64 time=43ms TTL=120
# Reply from 8.8.8.8: bytes=64 time=36ms TTL=120
# Reply from 8.8.8.8: bytes=64 time=80ms TTL=120

# Ping statistics for 8.8.8.8:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 36ms, Maximum = 80ms, Average = 49ms
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# 4.ping 8.8.8.8
#---------------------------------------------------------------------------------------------------------
# (uhnder) PS D:\secondAssignment> ping 8.8.8.8

# Pinging 8.8.8.8 with 32 bytes of data:
# Reply from 8.8.8.8: bytes=32 time=40ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=44ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=35ms TTL=120
# Reply from 8.8.8.8: bytes=32 time=77ms TTL=120

# Ping statistics for 8.8.8.8:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 35ms, Maximum = 77ms, Average = 49ms
#--------------------------------------------------------------------------------------------------------------

def pingtest(option,str):
    if option=='-n':
        response=os.popen(f"ping {option} 6 {str}").read()
        if "Received = 6" in response:
            print(f"Ping successful,Received 6 times")
            return True
        else:
            print(f"ping unsuccessful,not received for 6 times")
            return False
    elif option=='-a':
        response=os.popen(f"ping {option} {str}").read()
        if "dns.google" in response:
            print(f"Ping successful,HostName Found with -a option")
            return True
        else:
            print(f"HostName not found with -a option")
            return False
    elif option == '-l':
        response=os.popen(f"ping {option} 64 {str}").read()
        if "Reply from 8.8.8.8: bytes=64" in response:
            print(f"Ping successful,received 64 byte data")
            return True
        else:
            print(f"ping unsuccessful,not received 64 byte data")
            return False
    else:
        response=os.popen(f"ping {str}").read()
        if "Received = 4" in response:
            print(f"Ping successful,received default=4 times")
            return True
        else:
            print(f"ping unsuccessful")
            return False