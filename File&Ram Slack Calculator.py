
import math

# File Slack & Ram Slack Caluator


def greeting ():
    print ("""\n
###################################################
#                                                 #
#           File & Ram Slack Calculator           #
#                                                 #
###################################################
\n""")

def bytes_sector ():
    valid = False
    while valid == False:
        try:
            sector_bytes = int(input("Please Enter Number of Bytes per Sector: "))
            valid = True
        except:
            print ("\nPlease Enter Intergers Only\n")
    return sector_bytes

def num_sectors ():
    valid = False
    while valid == False:
        try:
            sector_num = int(input("Please Enter Number of Sectors Per Cluster: "))
            valid = True
        except:
            print ("\nPlease Enter Intergers Only\n")
    return sector_num

def file_size ():
    valid = False
    while valid == False:
        try:
            size_file = int(input("Please Enter File Size: "))
            valid = True
        except:
            print ("\nPlease Enter Intergers Only\n")
    return size_file


def ram_file_slack (bytes_sector,num_sector,file_size):
    cluster_size = (bytes_sector*num_sector)
    sectors_need = math.ceil(file_size/bytes_sector)
    s_total_bytes = (sectors_need*bytes_sector)
    ram_slack = (s_total_bytes-file_size)
    cluster_need = math.ceil(sectors_need/num_sector)
    c_total_bytes = (cluster_need*cluster_size)
    total_bytes_slack_c = (c_total_bytes-file_size)
    file_slack =(total_bytes_slack_c-ram_slack)
    
    print ("\t\tResults\n")
    print ("File Size:\t\t", file_size)
    print ("Sector Size:\t\t",bytes_sector)
    print ("# of Sectors:\t\t",num_sector)
    print ("Cluster Size:\t\t",cluster_size)
    print ("Ram Slack:\t\t",ram_slack)
    print ("File Slack:\t\t", file_slack)
    print ("Total Slack(Cluster):\t",total_bytes_slack_c)

# Main Program
greeting()
bytes_sector = bytes_sector()
num_sector = num_sectors()
file_size = file_size()
print ()
ram_file_slack (bytes_sector,num_sector,file_size)
print()
input ("Please any Key to Exit")


