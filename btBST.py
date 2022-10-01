from ctypes import _NamedFuncPointer


class Nut:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def chen(self,data):
        nut = Nut(data)
        if self is None:
            self = Nut
            return
        else:
            if data < self.data:
                if self.left == None:
                    self.left = nut
                else:
                    self.left.chen(data)
            elif data > self.data:
                if self.right == None:
                    self.right = nut
                else:
                    self.right.chen(data)
            else:
                print("Không được phép trùng số ở cây nhị phân")

class BST:
    def __init__(self,data=None) -> None:
        if data == None:
            self.goc = None
        else:
            self.goc = Nut(data)

    def chen(self,data):
        if self.goc == None:
            self.goc = Nut(data)
        else:
            self.goc.chen(data)
    def duyetLNR(self,goc = 0):
        nut_ht = goc
        if nut_ht == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyetLNR(nut_ht.left)
            for x in kq_trai:
                kq.append(x)
            kq.append(nut_ht.data)
            kq_phai = self.duyetLNR(nut_ht.right)
            for x in kq_phai:
                kq.append(x)
        return kq

    def duyetRNL(self,goc = 0):
        nut_ht = goc
        if nut_ht == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_phai = self.duyetLNR(nut_ht.right)
            for x in kq_phai:
                kq.append(x)
            kq.append(nut_ht.data)
            kq_trai = self.duyetLNR(nut_ht.left)
            for x in kq_trai:
                kq.append(x)
        return kq
    
    def xoa(self,so_can_xoa):
        nut_cha = None
        nut_ht = self.goc
        cha_con = None
        while nut_ht != None:
            if nut_cha == None:
                if nut_ht.left == None and nut_ht.right == None:
                    self.goc = None
                elif nut_ht.left == None:
                    self.goc = nut_ht.right
                    cha_con = "left"
                elif nut_ht.right == None:
                    self.goc = nut_ht.right
                    cha_con = "right"
                else: #có đủ 2 lá:
                    self.goc = nut_ht.right
                    temp = self.goc
                    while temp != None:
                        temp = temp.left
                    temp.left = nut_ht.left
            else: #nut_cha != None
                if nut_ht.left == None and nut_ht.right == None:
                    if cha_con == "left":
                        if nut_ht.left == None:
                            nut_cha.left = None
                        else:
                            nut_cha.right = None
                elif nut_ht.left == None:
                    if cha_con == "left":
                        nut_cha.left = nut_ht.right
                    else:
                        nut_cha.right = nut_ht.right
                elif nut_ht.right == None:
                    if cha_con == "left":
                        nut_cha.left = nut_ht.left
                    else:
                        nut_cha.right = nut_ht.left
                else: #node gồm đủ lá
                    if cha_con == "left":
                        nut_cha.left = nut_ht.right
                    else:
                        nut_cha.right = nut_ht.right
                    if nut_ht.right.left == None:
                        nut_ht.right.left = nut_ht.left
                    else:
                        temp = nut_ht.right
                        while temp != None:
                            temp = temp.left
                        temp.left = nut_ht.left
                del temp
                break
                        
                    
                       
def main():
    cay = BST()
    i = 0
    n = int(input("Nhập số lượng phần tử: "))
    for i in range(n):
        inp = int(input(f"Phần tử thứ {i}: "))
        cay.chen(inp)
    print(cay.duyetLNR())
    print(cay.duyetRNL())

main()
