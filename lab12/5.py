print ('введите год')
k = int ( input ())
b=int
c=int

if k<1984:
    b=((abs(k-1983))%12)*(-1)+11
    c=(((abs(k-1983))%10)//2)*(-1)+4
else:
    b=(k-1984)%12
    c=((k-1984)%10)//2

if c==0:
    if b==0:
        print('год зелёной крысы')
    if b==1:
        print('год зелёной коровы')
    if b==2:
        print('год зелёного тигра')
    if b==3:
        print('год зелёного зайца')
    if b==4:
        print('год зелёного дракона')
    if b==5:
        print('год зелёной змеи')
    if b==6:
        print('год зелёной лошади')
    if b==7:
        print('год зелёной овцы')
    if b==8:
        print('год зелёной обезьяны')
    if b==9:
        print('год зелёной курицы')
    if b==10:
        print('год зелёной собаки')
    if b==11:
        print('год зелёной свиньи')
        
if c==1:
    if b==0:
        print('год красной крысы')
    if b==1:
        print('год красной коровы')
    if b==2:
        print('год красного тигра')
    if b==3:
        print('год красного зайца')
    if b==4:
        print('год красного дракона')
    if b==5:
        print('год красной змеи')
    if b==6:
        print('год красной лошади')
    if b==7:
        print('год красной овцы')
    if b==8:
        print('год красной обезьяны')
    if b==9:
        print('год красной курицы')
    if b==10:
        print('год красной собаки')
    if b==11:
        print('год красной свиньи')
        
if c==2:
    if b==0:
        print('год жёлтой крысы')
    if b==1:
        print('год жёлтой коровы')
    if b==2:
        print('год жёлтого тигра')
    if b==3:
        print('год жёлтого зайца')
    if b==4:
        print('год жёлтого дракона')
    if b==5:
        print('год жёлтой змеи')
    if b==6:
        print('год жёлтой лошади')
    if b==7:
        print('год жёлтой овцы')
    if b==8:
        print('год жёлтой обезьяны')
    if b==9:
        print('год жёлтой курицы')
    if b==10:
        print('год жёлтой собаки')
    if b==11:
        print('год жёлтой свиньи')
        
if c==3:
    if b==0:
        print('год белой крысы')
    if b==1:
        print('год белой коровы')
    if b==2:
        print('год белого тигра')
    if b==3:
        print('год белого зайца')
    if b==4:
        print('год белого дракона')
    if b==5:
        print('год белой змеи')
    if b==6:
        print('год белой лошади')
    if b==7:
        print('год белой овцы')
    if b==8:
        print('год белой обезьяны')
    if b==9:
        print('год белой курицы')
    if b==10:
        print('год белой собаки')
    if b==11:
        print('год белой свиньи')

if c==4:
    if b==0:
        print('год чёрной крысы')
    if b==1:
        print('год чёрной коровы')
    if b==2:
        print('год чёрного тигра')
    if b==3:
        print('год чёрного зайца')
    if b==4:
        print('год чёрного дракона')
    if b==5:
        print('год чёрной змеи')
    if b==6:
        print('год чёрной лошади')
    if b==7:
        print('год чёрной овцы')
    if b==8:
        print('год чёрной обезьяны')
    if b==9:
        print('год чёрной курицы')
    if b==10:
        print('год чёрной собаки')
    if b==11:
        print('год чёрной свиньи')
    