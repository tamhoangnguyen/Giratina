from random import randint


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def chen(self,data):
        node = Node(data)
        if self is None:
            self = node
            return
        else:
            if data < self.data:
                if self.left == None:
                    self.left = node
                else:
                    self.left.chen(data)
            elif data > self.data:
                if self.right == None:
                    self.right = node
                else: self.right.chen(data)
            else:
                print("Trùng số rồi !")
        
class BST:
    def __init__(self,data = None):
        if data == None:
            self.goc = None
        else:
            self.goc = Node(data)
    def chen(self,data):
        if self.goc == None:
            self.goc = Node(data)
        else:
            self.goc.chen(data)
    
    def xoa(self,so_can_xoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        while nut_ht != None:
            if so_can_xoa < nut_ht.data:
                nut_cha = nut_ht
                nut_ht = nut_ht.left
                cha_con = "left"
            elif so_can_xoa > nut_ht.data:
                nut_cha = nut_ht
                nut_ht = nut_ht.right
                cha_con = "right"
            else:
                if nut_cha == None:
                    if nut_ht.left == nut_ht.right == None:
                        self.goc = None
                    elif nut_ht.left == None:
                        self.goc = nut_ht.right
                    elif nut_ht.right == None:
                        self.goc = nut_ht.left
                    else: #có đủ 2 lá:
                        self.goc = nut_ht.right
                        temp = self.goc
                        while temp != None:
                            temp = temp.left
                        temp.left = nut_ht.left
                else:
                    if nut_ht.left == None and nut_ht.right ==  None:
                        if cha_con == "left":
                            nut_cha.left = None
                        else:
                            nut_cha.right = None
                    elif nut_ht.left == None:
                        if cha_con =="left":
                            nut_cha.left = nut_ht.right
                        else:
                            nut_cha.right = nut_ht.right
                    elif nut_ht.right == None:
                        if cha_con == "left":
                            nut_cha.left = nut_ht.left
                        else:
                            nut_cha.right = nut_ht.left
                    else:
                        if cha_con == "left":
                            nut_cha.left = nut_ht.right
                        else:
                            nut_cha.right = nut_ht.right
                        if nut_ht.right.left == None:
                            nut_ht.right.left = nut_ht.left
                        else:
                            temp = nut_ht.right
                            while temp.left != None:
                                temp = temp.left
                            temp.left = nut_ht.left
                    del nut_ht
                    break  

    # def duyet_LNR(self,goc = 0):
    #     nut_ht = goc
    #     if goc == 0:
    #         nut_ht = self.goc
    #     if nut_ht == None:
    #         return []
    #     else:
    #         kq = []
    #         kq_trai = self.duyet_LNR(nut_ht.left)
    #         for x in kq_trai:
    #             kq.append(x)
    #         kq.append(nut_ht.data)
    #         kq_phai = self.duyet_LNR(nut_ht.right)
    #         for x in kq_phai:
    #             kq.append(x)
    #         return kq
    # def duyet_RNL(self,goc = 0):
    #     nut_ht = goc
    #     if goc == 0:
    #         nut_ht = self.goc
    #     if nut_ht == None:
    #         return []
    #     else:
    #         kq = []
    #         kq_phai = self.duyet_RNL(nut_ht.right)
    #         for x in kq_phai:
    #             kq.append(x)
    #         kq.append(nut_ht.data)
    #         kq_trai = self.duyet_RNL(nut_ht.left)
    #         for x in kq_trai:
    #             kq.append(x)
    #         return kq
        
    def duyet_NRL(self,goc = 0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq.append(nut_ht.data)
            kq_phai = self.duyet_NRL(nut_ht.right)
            for x in kq_phai:
                kq.append(x)
            kq_trai = self.duyet_NRL(nut_ht.left)
            for x in kq_trai:
                kq.append(x)
            return kq
    
    def tim(self,so_can_tim):
        if self.goc == None:
            return
        nut_ht = self.goc
        kq = ''
        while nut_ht != None and nut_ht.data != so_can_tim:
            kq += f'{nut_ht.data} -> '
            if so_can_tim <= nut_ht.data:
                nut_ht = nut_ht.left
            else:
                nut_ht = nut_ht.right
        if nut_ht == None:
            print("Tìm không thấy !")
        else:
            kq += f"{nut_ht.data}"
            return kq


def main():
    cay_nhi_phan = BST()
    i=0
    my_array = set()
    for i in range(10):
        so = randint(-100,100)
        my_array.add(so)
    print(my_array)
    for x in my_array:
        cay_nhi_phan.chen(x)
    print(cay_nhi_phan.duyet_NRL())
    so_can_tim = int(input("Số cần tìm là?: "))    
    so_can_xoa = int(input("Số cần xóa là?: "))
    print(cay_nhi_phan.tim(so_can_tim))
    (cay_nhi_phan.xoa(so_can_xoa))
    print(cay_nhi_phan.duyet_NRL())

main()

    
        


