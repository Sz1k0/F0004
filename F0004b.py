név = input('Mi a neved? ')
kor = input('Hány éves vagy? ') 
kor = int(kor) 
év = input('Milyen évet irunk? ')
év = int(év)
születésiév = év - kor
érettségi_év = születésiév + 18
print(név, ', kend ',érettségi_év, '-ban érettségizik.', sep='')