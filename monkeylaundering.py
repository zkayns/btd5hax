from ReadWriteMemory import ReadWriteMemory
rwm = ReadWriteMemory()
bloonz = rwm.get_process_by_name("BTD5-Win.exe")
bloonz.open()
baseaddress = 0x008E0000+0x009FA9B0
mmpointer = bloonz.get_pointer(baseaddress, offsets=[0x0, 0x98, 0x0, 0xB8, 0x20, 0xC0, 0x128])
newmm = input("New Monkey Money #: ")
bloonz.write(mmpointer, int(newmm))