import random ,sys
month=sys.argv[1]
print 'month=',month
label='label_'+month+'_backup.txt'
with open(label) as f:
    fdata = [line.strip() for line in f]
    lis=[i for i,x in enumerate(fdata) if x=='1']
    lis_2=[j for j,x in enumerate(fdata) if x=='-1']
    a=len(lis)
    print '# of positive =',a
    b=len(fdata)
    d=b-a
    print '# of negative =',d



data_positive='data_'+month+'_positive.txt'
data_negative='data_'+month+'_negative.txt'
data='data_'+month+'_backup.txt'
g=open(data_positive,'w')
m=open(data_negative,'w')
with open(data) as r:
    rdata=[line.strip() for line in r]
    
    for num in lis: 
#        print 'num=',num
        g.write(rdata[num]+'\n')
#        lis_2=rdata[num]
#    print 'lis_2=',lis_2
    for count in lis_2:
        m.write(rdata[count]+'\n')
m.close()
f.close()
r.close()
g.close()

e=int(d/10)
count=0
m=0
n=9
lis_3=[]
percentage=sys.argv[2]
dup=100/int(percentage)
dup=int(dup)
label_negative_duplicate='label_'+month+'_negative_duplicate.txt'
h=open(label_negative_duplicate,'w')
for i in range(0,e):
    r1=random.randint(m,n)
    m+=dup
    n+=dup
    lis_3.append(r1)
    count+=1
for item in lis_3:
    h.write("%s\n" % item)
print '# of random =',count 
total=count+a
print '# of total row =',total
h.close()

data_duplicate='data_'+month+'_negative_duplicate.txt'
with open(data_duplicate,'w') as dupli:
    with open(data_negative,'r') as nega:
        ndata=[line.strip() for line in nega]
        for num1 in lis_3:
            dupli.write(ndata[num1]+'\n')
nega.close()
dupli.close()
        
data_duplicate_all='data_'+month+'.txt'
filenames = [data_positive, data_duplicate]
with open(data_duplicate_all, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)  
outfile.close()
infile.close() 


#count=# of random
#a=# of positive 
label_duplicate='label_'+month+'.txt'
lab=open(label_duplicate,'w')
lis_4=[]
for i in range(0,a):
    line1='1'
    lis_4.append(line1)
for i in range(0,count):
    line2='-1'
    lis_4.append(line2)
final_string = '\n'.join(lis_4)
lab.write(final_string)
