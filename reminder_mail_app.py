# Arayüzümüz

from tkcalendar import DateEntry
from tkinter import * # Tkinter import ettik.

# Arayüz Oluşturma
arayuz = Tk() # Arayüz nesnesini oluşturduk.

# Pencere Başlığı
arayuz.title("Hatırlat Bana") # Pencere Başlığını Oluşturduk.

# Pencere Fotoğrafı
img = PhotoImage(file='C:\\icon.png') # iconu img ye atadık.
arayuz.iconphoto(False,img) # İconumuzu oluşturduk.

# Canvas'ımızı oluşturuyoruz.
canvas = Canvas(arayuz,height=600,width=500)
canvas.pack() # arayuze gönderdik.

# Framework oluşturma.

ust_frame = Frame(arayuz,bg="#EEDFCC")
ust_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.28)

alt_frame = Frame(arayuz,bg="#CDC0B0")
alt_frame.place(relx=0.05,rely=0.35,relwidth=0.9,relheight=0.6)

# Label yazı fontunu değişkene atıyoruz.

label_font = ("Comic Sans MS", 7, "bold")

# Labelları Oluşturuyoruz.

hatirlatma_detaylari_label = Label(ust_frame,text="Hatırlatma Detayları",font=("Comic Sans MS",12,"bold"),bg="#EEDFCC")
hatirlatma_detaylari_label.pack(padx=5,pady=5,side="top")

tarih_label = Label(ust_frame,bg="#EEDFCC",text="Tarih",font=label_font)
tarih_label.pack(padx=5,pady=5,side="left")

hatirlatma_mesaji_label = Label(alt_frame,bg="#CDC0B0",text="Hatırlatma Mesajı",font=label_font)
hatirlatma_mesaji_label.pack(padx=5,pady=5,anchor="nw")


# Tarih Seçme Aracımızı oluşturuyoruz.

tarih_secici = DateEntry(ust_frame, background="#EEDFCC",foreground="black",borderwidth=1,locale="de_DE")
tarih_secici._top_cal.overrideredirect(False)
tarih_secici.pack(padx=5,pady=5,side="left")


saat_label = Label(ust_frame,font=label_font,bg="#EEDFCC",text="Saat")
saat_label.pack(padx=5,pady=5,side="left")

text_box = Text(ust_frame,height=1,width=8)
text_box.pack(pady=5,padx=5,side="left")
text_box.insert(END,"00:00")

# Açılır Menü Ekleme.

acilir_menu_islem = StringVar(ust_frame)
acilir_menu_islem.set("\t")

acilir_menu = OptionMenu(ust_frame,acilir_menu_islem,"Doğum Günü","Proje-Ödev","Etkinlik","Özel Gün")
acilir_menu.pack(padx=5,pady=20,side="right")

# E-posta atılacak mail adresinin girişi için alan oluşturuyoruz:

# Label

email_label = Label(ust_frame,text="E-mail Adresi",font=label_font,bg="#EEDFCC")
email_label.place(x=5,y=135)

# Textbox

bos_metin = "Lütfen Göndermek İstediğiniz E-posta Adresini Giriniz..."

email_textbox = Text(ust_frame,height=1,width=45)
email_textbox.tag_configure('style',foreground="#bfbfbf",font=("Verdana",7,"bold"))
email_textbox.place(x=80,y=137)
email_textbox.insert(END,bos_metin,'style')

# Bir diğer label oluşturuyoruz.

hatirlatma_turu_label = Label(ust_frame,bg="#EEDFCC",text="Hatırlatma Türü",font=label_font)
hatirlatma_turu_label.pack(padx=5,pady=5,side="right")

# Mesajın Yazılacağı alanı yazıyoruz.

mesaj_alani = Text(alt_frame,height=12,width=54)
mesaj_alani.tag_configure('style',foreground="#bfbfbf",font=("Verdana",7,"bold"))
mesaj_alani.pack()

# Default karşılama metni oluşturma.

karsilama_metni = "Mesajınızı buraya giriniz..."
mesaj_alani.insert(END,karsilama_metni,'style')

# Değerleri Alma İşlemi

"""
acilir_menu_deger = acilir_menu_islem.get()
tarih_deger = tarih_secici.get_date()
mesaj_deger = mesaj_alani.get("1.0","end")
"""

# Butonun yapacağı işlem için metodumuzu oluşturuyoruz.

from datetime import datetime
import time
from tkinter import messagebox # Daha sonra kullanılması üzere import ediyoruz.

def button_func():

    uyari_mesaji = ""

    # Girilen tarih ve saati alma:
    # Aynı zamanda girilen bilgilerin doğruluğunu test etme işlemini de gerçekleştiriyoruz.
    
    try:
        saat = text_box.get("1.0","end") # string time
        secili_tarih = tarih_secici.get_date() # Datetime object
        
        string_year = datetime.strftime(secili_tarih,"%Y")
        string_month = datetime.strftime(secili_tarih,"%m")
        string_day = datetime.strftime(secili_tarih,"%d")

        int_year = int(string_year)
        int_month = int(string_month)
        int_day = int(string_day)

        saat_in_list = saat.split(":")

        int_saat = int(saat_in_list[0])
        int_dakika = int(saat_in_list[1])

        girilen_tarih = datetime(int_year,int_month,int_day,int_saat,int_dakika)
        
        # Şimdiki saati ayarlama işlemleri:

        simdiki_tarih = datetime.now()

        simdiki_tarih_int_year = int(datetime.strftime(simdiki_tarih,"%Y"))
        simdiki_tarih_int_month = int(datetime.strftime(simdiki_tarih,"%m"))
        simdiki_tarih_int_day = int(datetime.strftime(simdiki_tarih,"%d"))
        
        simdiki_tarih_int_hour = simdiki_tarih.hour
        simdiki_tarih_int_minutes = simdiki_tarih.minute
        simdiki_tarih_int_seconds = simdiki_tarih.second

        simdiki_tarih_kullanilacak = datetime(simdiki_tarih_int_year,simdiki_tarih_int_month,simdiki_tarih_int_day,simdiki_tarih_int_hour,simdiki_tarih_int_minutes,simdiki_tarih_int_seconds)
    
    except Exception as err:
        uyari_mesaji = "Lütfen girilen tüm bilgilerin doğru formatta girildiğinden emin olunuz!"
        messagebox.showerror("İşlem Başarısız!",uyari_mesaji)
        arayuz.destroy()

    # İstenilen zamanda e-postayı gönderme işlemi.

    # Tarih farkı kapandığında maili gönderecek. O zamana kadar uyuyacak.
    
    if (girilen_tarih.timestamp() - simdiki_tarih_kullanilacak.timestamp()) <= 0:
        hata_mesaji = "Lütfen İleri Bir Tarih Giriniz!"
        messagebox.showerror("İşlem Başarısız!",hata_mesaji)
        arayuz.destroy()
    else:
        uyari_mesaji = "Lütfen Hatırlatma Maili Gönderilene Kadar Uygulamayı Kapatmayınız. Bu Bilgi Penceresini Kapatabilirsiniz."
        messagebox.showinfo("İşlem Başarılı",uyari_mesaji)
        time.sleep(girilen_tarih.timestamp() - simdiki_tarih_kullanilacak.timestamp())
    # Bekleme işlemini gerçekleştirdik. Şimdi maili gönderme işlemine geçiyoruz.

    from smtplib import SMTP
    import emailim

    acilir_menu_deger = acilir_menu_islem.get()
    tarih_deger = tarih_secici.get_date()
    mesaj_alani_deger = mesaj_alani.get("1.0","end")

    genel_mesaj = ""

    try:
        content = "{} \n\nKonu: {} Tarih: {} Saat:{}:{}".format(mesaj_alani_deger,acilir_menu_deger,tarih_deger,saat_in_list[0],saat_in_list[1]) # Asıl mesaj içeriği
        
        # Gönderen bilgisi
        email = emailim.email # Benim emailim
        password = emailim.password # Benim password'um

        # Alıcı Bilgisi

        gonderilen_email = email_textbox.get("1.0","end")

        sendTo = gonderilen_email

        mail = SMTP("smtp.gmail.com", 587) # Gmail ile göndereceğimiz için bu şekilde gmail.com

        # Mail bağlantısını yapıyoruz.

        mail.ehlo() # Mail bağlantısını yapıyoruz.
        mail.starttls() # Mesajı gizli atacağımız için starttls metodunu kullanıyoruz.
        mail.login(email,password) # Login işlemimizi yapıyoruz.
        mail.sendmail(email, sendTo, content.encode("utf-8")) # Gönderen, gönderilecek ve mail içeriğini giriyoruz.
        # encode utf-8 yaparak türkçe sıkıntı olmasın istiyoruz.

        genel_mesaj = "Mail Gönderme İşleminiz Başarılı!"
        messagebox.showinfo("İşlem Başarılı",genel_mesaj)

    except Exception as err:
        genel_mesaj = "Mail Gönderme İşleminiz Başarısız! Lütfen Her Detayı Doğru Girdiğinizden Emin Olun."
        messagebox.showerror("İşlem Başarısız",genel_mesaj)
    finally:
        arayuz.destroy()

# Buton Ekleme

gonder_buton = Button(alt_frame,text="Gönder",width=20,command=button_func)
gonder_buton.pack(anchor=S,pady=20)

# Arayuzumuzu çalıştırıyoruz.
arayuz.mainloop()