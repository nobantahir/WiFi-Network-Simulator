import pickle as bin

class Bin:
    def __init__(self):
        self.step = 1
        self.log = ""

    def write_log(self, message):
        self.log += f"{self.step}. {message}\n"
        self.step += 1
 
    def dump(self):
        with open("access_controller.pkl", "wb") as binary_file:
            bin.dump(self.log, binary_file)

    def unbin(self):
        with open("access_controller.pkl", "rb") as binary_file:
            content = bin.load(binary_file)
        
        return content
            
    def __call__(self):
        print(self.unbin())
    
    def __str__(self):
        return self.unbin()