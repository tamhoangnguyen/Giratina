from dslk import*
def main():
    ds = DSlienket()
    ds.in_ds()
    print("a : THÊM --------")
    i = 0
    n = int(input("Số phần tử bạn muốn thêm: "))
    for i in range(n):
        so = int(input("Nhập số cần thêm: "))
        ds.them(so)
        i+=1
    ds.in_ds()
    print("b: CHÈN ------------")
    chi_muc = int(input("Nhập vị trí bạn muốn chèn: "))
    gia_tri = int(input("Nhập giá trị bạn muốn chèn: "))
    ds.chen(chi_muc,gia_tri)
    ds.in_ds()

    print("c: TÌM -------------")
    so_can_tim = int(input("Số cần tìm là: "))
    vt = ds.tim(so_can_tim)
    print(f"{so_can_tim} cần tìm ở vị trí: {vt}")

    print("d: XÓA ---------")
    so_can_xoa = int(input("Số cần xóa là: "))
    ds.xoa(so_can_xoa)
    ds.in_ds()

    print("d: CẬP NHẬT -----------")
    vi_tri = int(input("Nhập vị trí cần thay đổi: "))
    gia_tri = int(input("Nhập giá trị muốn đổi: "))
    ds.cap_nhat(vi_tri,gia_tri)
    ds.in_ds()

    yeu_cau = input("Bạn có muốn xóa hết DSLK ?(Y/N): ")
    if yeu_cau == "Y":
        ds.xoa_het()
    ds.in_ds()



if __name__ == "__main__":
    main()