from os import name,system
file_path=r"C:\Users\your_folder\your_file"
def ccls():
    system("cls" if name=="nt" else "clear")
def oku():
    ccls()
    try:
        with open(file_path,"r",encoding="utf-8") as file:    
            written=file.readlines()
            for p in written:
                print(p)
    except FileNotFoundError:
        print("Dosya bulunamadı, işleme devam edilemiyor.")
def yaz():
    ccls()
    try:
        choice_mode=int(input("1-Ekle     2-Değiştir     3-Baştan Yaz\nSeçim: "))
        if choice_mode not in [1,2,3]:
            raise ValueError("Seçenekler yalnızca 1,2 ya da 3 olabilir.")
    except ValueError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu. Hata mesajı: {e}")
    else:
        if choice_mode==1:
            try:
                with open(file_path,"a",encoding="UTF-8") as file:
                    text=input("Yazmak istediğiniz mesaj:\n")
                    file.write(text+"\n")
            except Exception as e:
                print(f"Mesaj eklenirken beklenmeyen bir hata oluştu. Hata mesajı: {e}")
        elif choice_mode==2:
            try:
                if input("Devam etmek itiyor musunuz? (iptal için 'iptal' giriniz):\n").strip().lower()=="iptal":
                    return
                with open(file_path,encoding="UTF-8") as file:
                    lines=file.readlines()
                if not lines:
                    print("Dosya boş, Değiştirilemez.")
                    return
                print("Değiştirmek istediğiniz satırı seçin: \n")
                for i,t in enumerate(lines):
                    print(f"index: {i} mesaj: {t.strip()}")
                changing_line=int(input("Değiştirilecek satırın index numarasını girin: "))
                if 0<=changing_line<len((lines)):
                    newtext=input(f"{lines[changing_line]} satırı için yeni içeriği girin:\n")
                    lines[changing_line]=newtext + "\n"
                with open(file_path,"w",encoding="UTF-8") as file:
                    file.writelines(lines)
                print("Satır başarıyla değiştirildi.")
            except FileNotFoundError:
                print("Dosya bulunamadı, İşleme devam edilemiyor.")
            except ValueError:
                print("Geçersiz index girişi yapıldı. Dosya değiştirilemiyor.")
            except Exception as e:
                print(f"Beklenmeyen bir hata oluştu. Hata mesajı: {e}")
        elif choice_mode==3:
            if input("Baştan yazmaktan emin misiniz? (iptal etmek için 'iptal' yazınız.): ").strip().lower()=="iptal":
                print("Baştan yazmak iptal edildi.")
                return
            try:    
                with open(file_path,"w",encoding="UTF-8") as file:
                    text= input("Yazmak istediğiniz mesajı giriniz: ")
                    file.write(text+"\n")
            except Exception as e:
                print(f"Dosya baştan yazılırken beklenmeyen bir hata oluştu. Hata mesajı: {e}")


                    

       
while True:
    try:
        choice=int(input("1-OKU\n2-YAZ\n3-TEMİZLE\n4-ÇIK\nSeçiminiz: "))
        if choice<1 or choice>4:
            raise ValueError("Seçenek 0'dan az 5'den çok olamaz.")
    except ValueError as e:
        print(f"Sadece sayısal değer girin! Hata mesajı: {e}")
        ccls()
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu. Hata mesajı: {e}")
    else:
        if choice==1:
            oku()
        elif choice==2:
            yaz()
        elif choice==3:
            ccls()
        elif choice==4:
            if input("İyi günler dilerim. Enter'a bastığınızda kod durdurulacak. (İptal yazarsanız kod kapatılmaycak.)\n").strip().lower()=="iptal":
                continue
            ccls()
            break