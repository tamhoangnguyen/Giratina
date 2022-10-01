class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.next = None
class DSLK:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def xoa_phan_tu_lap_lai(self):
        truoc = None
        hien_tai = self.dau
        while hien_tai != None:
            truoc = hien_tai
            if truoc.next == hien_tai:
                truoc.next = hien_tai.next
            
                
        
            

    def them(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.next = nut
            self.cuoi = nut
        
def main():
    ds = DSLK()
    i = 0
    n = int(input("Nhập số lượng phần tử bạn muốn thêm: "))
    for i in range(n):
        so = int(input("Nhập số bạn muốn thêm: "))
        ds.them(so)
        i+=1
    ds.xoa_phan_tu_lap_lai(so)
main()
 
            
            
                


                
            


        
