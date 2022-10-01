class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.next = None
class DSlienket:
    def __init__(self):
        self.dau = None
        self.cuoi = None

    def in_ds(self):
        stt = 0
        hien_tai = self.dau
        kq = ' DS [ '
        while hien_tai != None:
            stt +=1
            if stt == 1:
                kq += ' ' + str(hien_tai.gia_tri)
            else:
                kq += ' -> ' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.next
        kq += " ]"
        print(kq)

    def them(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.next = nut
            self.cuoi = nut
            
    def chen(self,chi_muc,gia_tri):
        nut = Nut(gia_tri)
        truoc = None
        hien_tai = self.dau
        i = 0
        while i < chi_muc and hien_tai != None:
            i+=1
            truoc = hien_tai
            hien_tai = hien_tai.next
        if truoc == None:
            nut.next = self.dau
            self.dau = nut
            if self.cuoi == None:
                self.cuoi = nut
        else:
            if hien_tai == None:
                self.cuoi.next = nut
                self.cuoi = nut
            else:
                truoc.next =  nut
                nut.next = hien_tai

    def tim(self,gia_tri):
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            hien_tai = hien_tai.next
            vi_tri +=1
        if hien_tai == None:
            return None
        else:
            return vi_tri

    def xoa(self,gia_tri):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.next
        if hien_tai != None:
            if hien_tai == self.dau and hien_tai == self.cuoi:
                self.dau = self.cuoi = None
            elif hien_tai == self.dau:
                self.dau = self.dau.next
            elif hien_tai == self.cuoi:
                truoc.next = None
                self.cuoi = truoc
            else:
                truoc.next = hien_tai.next
            del hien_tai

    def cap_nhat(self, vi_tri, gia_tri):
        hien_tai = self.dau
        i = 0
        while i < vi_tri and hien_tai != None:
            i+=1
            hien_tai = hien_tai.next
        if hien_tai != None:
            hien_tai.gia_tri = gia_tri

    def xoa_het(self):
        hien_tai = self.dau
        self.dau = None
        self.cuoi = None
        while hien_tai != None:
            temp = hien_tai
            hien_tai = hien_tai.next
            del temp







