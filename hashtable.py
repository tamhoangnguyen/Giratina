
from turtle import right


class Nut():
    def __init__(self,value):
        self.value = value
        self.next = None
class Hashtable:
    def __init__(self,size = 10):
        self.danh_sach = [None for _ in range(size)]

    def __str__(self):
        kq = "["
        stt_1 = 0
        for x in self.danh_sach:
            stt_1 +=1
            if stt_1 != 1:
                kq += ","
            if x is None:
                kq += "None"
            else:
                kq = kq + "["
                stt_2 = 0
                for e in x:
                    stt_2 += 1
                    if stt_2 != 1:
                        kq += ","
                    
                kq = kq +']'
        kq += "]"
        return kq
    def bam(self,key):
        size = len(self.danh_sach)
        return hash(key) % size
    def lay(self,key):
        hash_index = self.bam(key)
        if self.danh_sach[hash_index] is None:
            return None
        else:
            for x in self.danh_sach[hash_index]:
                if x[0] == key:
                    return x[1]
            else:
                print("Không tìm thấy")

    def them(self,key,value): 
        nut = Nut(value)      
        hash_index = self.bam(key) 
        previous = None
        right_now = nut
        if self.danh_sach[hash_index] == None:
            self.danh_sach[hash_index] = nut
        else:
            previous = right_now
            right_now.next = nut
    def __setitem_(self,key,value):
        self.them(key,value)
    
    def __getitem__(self,key):
        return self.lay(key)

def main():
    bang_bam = Hashtable(10)
    import random
    print(bang_bam)
    i = 0
    for i in range(18):
        key = random.randint(0,10)
        value = random.randint(0,100)
        print(f"* Them khoa: {key}, gia tri: {value} vao bang bam")
        bang_bam.them(key,value)
        print(bang_bam)
        print("")
        i+=1
    so_can_lay = int(input("Số cần lấy: "))
    gia_tri = bang_bam[so_can_lay]
    print(f"Số cần lấy {so_can_lay} có giá trị là: {gia_tri}")
    
main()
            


            

                
            





            

        


            