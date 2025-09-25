t=int(input("Nhap Vao So Giay(t): "))

Gio= (t//3600)%24
Phut= (t/3600)//60
Giay= (t%3600)%60

print(" ",Gio," ",Phut," ",Giay)