név = input('Kérlek add meg a neved ')
kor = input('Hány éves vagy? ')
kor = int(kor)
év = input('Milyen évet írunk? ')
év = int(év)
születési_év = év - kor
print(név, ',Te', születési_év , '-ban született.', sep='')