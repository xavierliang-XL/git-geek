class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def wash(self):
        print("wash clothes")
        print(self.width)
        print(self.height)

washer = Washer(10,100)
#washer.width=200
#washer.height=1000

print(f'washer width is {washer.width}')
print(f'washer height is {washer.height}')