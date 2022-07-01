import random as r
def oyin():
    l=0
    l1=0
    l2=0
    b=5
    g=0
    b1=0
    print(
            "Assalomu Aleykum\n <<<'quduq, qaychi,qog'oz'>>>\n o'yiniga xush kelibsiz"
            "\nO'yinni boshlash uchun quydagilardan birini tanlang:\n"
            "variantni tanlang:>>>")
    while b:
        b1+=1
        a=input("Kiriting>>>\n")
        variant =r.choice(['quduq','qaychi','qog\'oz'])
        if a=='quduq' and variant=='qaychi' or a=='qaychi' and variant=='qog\'oz' or a=='qog\'oz' and variant=='quduq':
            print(f"Tabriklaymiz siz yutdingiz!\n Kompyuter {variant} ni tanladi, Siz tanladingiz {a}:")
            l+=1
        elif a=='quduq' and variant=='quduq' or a=='qaychi' and variant=='qaychi' or a=='qog\'oz' and variant=='qog\'oz':
            print(f"Natija durrang bo'ldi: siz {a} ni kompyuter {variant} ni tanladi:")
            l2+=1
        else:
            print(f"Kompyuter g'olib bo'ldi! siz {a} ni kompyuter {variant} ni tanladi:")
            l1+=1  
        b-=1     
        if b1==5:
            print(f"Natijalar soni: Siz {l}\n Natijalar soni: Kompyuter {l1}\n durranglar soni: {l2}")
        while b1==5:
            g=int(input("Yana o'ynaymizmi?\n ha bo'lsa 1 ni\nyoq bo'lsa 2 ni bosing\n"))
            if g==1:
                b=5
                b1=0
                continue
            if g==2:
                print("O'yin tugadi!!!!")
                break
            else:  
                print("ERROR??? Qayta urining!")
                continue
oyin()


