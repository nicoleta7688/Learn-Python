class Book:
    pass

book1 = Book()
book2 = Book()
book3 = Book()

print(type(book1))
print(type(book2))
print(type(book3))

print(book1 is not book2)
'''
Cerință: Creează o clasă numită Book și apoi creează trei obiecte diferite ale acestei clase.

Programul tău trebuie să îndeplinească următoarele condiții:
1. Definește clasa Book.
2. Creează trei obiecte: book1, book2 și book3.
3. Afișează tipul fiecărui obiect folosind type().
4. Verifică dacă book1 și book2 sunt obiecte distincte, folosind operatorul is not.

Rezultatul așteptat, orientativ:
<class '__main__.Book'>
<class '__main__.Book'>
<class '__main__.Book'>
True

Numele modulului din afișarea lui type() poate fi diferit în funcție de mediul în care rulezi programul.
'''