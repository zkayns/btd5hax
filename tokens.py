from ReadWriteMemory import ReadWriteMemory
rwm = ReadWriteMemory()
bloonz = rwm.get_process_by_name("BTD5-Win.exe")
bloonz.open()
baseaddress = 0x008E0000+0x003436C4
tokenpointer = bloonz.get_pointer(baseaddress, offsets=[0x0, 0x6C, 0x0, 0x100, 0x0, 0xC0, 0x130])
newtokens = input("New Tokens #: ")
bloonz.write(tokenpointer, int(newtokens))