import pickle as bin
import os

class Bin:
    def __init__(self):
        self.step = 1
        self.log = ""

    def write_log(self, message):
        self.log += f"{self.step}. {message}\n"
        self.step += 1
 
    def dump(self):
        file_name = os.path.basename(__file__)
        file_name = file_name.rsplit(".", 1)[0]
        #print(file_name)
        self.bin_name = f"{file_name}_bin.pkl"
        with open(self.bin_name, "wb") as binary_file:
            bin.dump(self.log, binary_file)

    def unbin(self):
        with open(self.bin_name, "rb") as binary_file:
            content = bin.load(binary_file)
        
        return content
            
    def __call__(self):
        print(self.unbin())
    
    def __str__(self):
        return self.unbin()
