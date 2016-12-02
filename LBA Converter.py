
### CHS to LBA Converter

## LBA = (((CYLINDER * heads_per_cylinder) + HEAD) * sectors_per_track) + SECTOR - 1

while True: 
    #Hard Disk CHS
    print ()
    print ("""
###########################################
##                                       ##
##     CHS to LBA Address Converter      ##
##                                       ##
###########################################
""")
    print ()
    hd_cylinder = int(input("Enter Number of Hard Drive Cylinders: "))
    hd_head = int(input("Enter Number of Hard Drive Heads: "))
    hd_sector = int(input("Enter Number of Hard Drive Sectors: "))

    # CHS Address
    print ()
    chs_cylinder = int(input("Enter CHS Cylinder Number: "))
    chs_head = int(input("Enter CHS Head Number: "))
    chs_sector = int(input("Enter CHS Sector Number: "))

    # Formula Process

    address = ((((chs_cylinder * hd_head) +chs_head) * hd_sector)+ chs_sector -1)
    
    print ()
    print ("LBA Address: ",address)
    print ()
