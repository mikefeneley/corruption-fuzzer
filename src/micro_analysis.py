



class MicroAnalysis:
    """
    Class to solve microcorruption ctf problems by 
    emulating the functionality of the MSP430 pseudo architecture
    and using brute force techniques to find password unlocks.
    """
    def __init__(self):
        self.pc = 0x4400  
        self.sp = 0x0000  
        self.sr = 0x0000  
        self.cg = 0x0000
        self.r4 = 0x0000  
        self.r5 = 0x0000  
        self.r6 = 0x0000  
        self.r7 = 0x0000
        self.r8 = 0x0000  
        self.r9 = 0x0000  
        self.r10 = 0x0000  
        self.r11 = 0x0000
        self.r12 = 0x0000  
        self.r13 = 0x0000  
        self.r14 = 0x0000  
        self.r15 = 0x0000
    
        self.print_reg()

    def print_reg(self):
        print("PC: " + hex(self.pc))
        print("SP: " + hex(self.sp))
        print("SR: " + hex(self.sr))
        print("CG: " + hex(self.cg))
        print("R4: " + hex(self.r4))
        print("R5: " + hex(self.r5))
        print("R6: " + hex(self.r6))
        print("R7: " + hex(self.r7))
        print("R8: " + hex(self.r8))
        print("R9: " + hex(self.r9))
        print("R10: " + hex(self.r10))
        print("R11: " + hex(self.r11))
        print("R12: " + hex(self.r12))
        print("R13: " + hex(self.r13))
        print("R14: " + hex(self.r14))
        print("R15: " + hex(self.r15))

    
    def analyze(self, filename):
        print(filename)
        striped_filename = self.strip_headers(filename)

    def strip_headers(self, filename):
        """ 
        Strip newline characters and header information from the 
        """
        
        striped_filename = filename[:len(filename)-2]
        
        origin = open(filename, 'r')
        strip = open(striped_filename, 'w')
        
        for line in origin:
            if "\n" != line and line[4] == ':':
                #print(line)
                strip.write(line)

        strip.close()
        origin.close()        
        return striped_filename


if __name__ == '__main__':
    analyst = MicroAnalysis()
    analyst.analyze('new_orleans.s')
