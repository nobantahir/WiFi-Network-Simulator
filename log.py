import pickle as bin

class Bin:
    def __init__(self, type, name = ""):
        self.step = 1
        self.log = ""
        type = str(type)
        name = str(name)
        self.bin_name = f"{type}_{name}_bin.pkl"
        
    def write_log(self, message):
        self.log += f"{self.step}. {message}\n"
        self.step += 1
 
    def dump(self):
        with open(self.bin_name, "wb") as binary_file:
            bin.dump(self.log, binary_file)

    def unbin(self):
        with open(self.bin_name, "rb") as binary_file:
            content = bin.load(binary_file)
        
        return content
            
    def __call__(self):
        self.dump()
        print(self.unbin())
    
    def __str__(self):
        self.dump()
        return self.unbin()
