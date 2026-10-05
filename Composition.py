# class Processor:
#     def __init__(self,brand, cores):
#         self.brand = brand
#         self.cores = cores
# class Computer:
#     def __init__(self, name, processor):
#         self.name = name
#         self.processor = processor

# my_processor = Processor("Hp","Intel Core")
# my_computer = Computer("Anmol Laptop",my_processor)

# print(f"Laptop Name: {my_computer.name}")
# print(f"Processor Brand: {my_computer.processor.brand}")
# print(f"Processor Cores: {my_computer.processor.cores}")


class Processor:
    def __init__(self, brand,cores):
        self.brand = brand
        self.cores = cores
class Computer:
    def __init__(self,name,processor_brand,processor_cores):
        self.name = name
        self.processor = Processor(processor_brand,processor_cores)
computer = Computer("Anmol Laptop", "Intel", 8)

print(f"Laptop Name: {computer.name}")
print(f"Brand: {computer.processor.brand}")
print(f"Cores: {computer.processor.cores}")
