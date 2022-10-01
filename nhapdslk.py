class Nut:
    def __init__(self,data):
        self.data = data
        self.next = None
class DSLK:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def chen(self,data):
        nut = Nut(data)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.next = nut
            self.cuoi = nut
    def print(self):
        truoc = Nut(None)
        hien_tai = self.dau
        truoc.next = hien_tai
        while hien_tai != None:
            if truoc.data != hien_tai.data:
                truoc = hien_tai
                print(hien_tai.data)
            else:
                truoc.next = hien_tai.next
                del hien_tai.data
            hien_tai = hien_tai.next
        
def main():
    ds = DSLK()
    for i in range(5):
        data = int(input("Nhập số: "))
        ds.chen(data)
    ds.print()
main()
