# -*- coding: UTF-8 -*-
import random ,sys
import numpy as np

##==== count the number of positive and negative ==============

month=sys.argv[1]
print 'month=',month
label='label_'+month+'_all.txt'
order_positive='order_of_positive.txt'  
order_negative='order_of_negative.txt'
ofp=open(order_positive,'w') 
ofn=open(order_negative,'w')
with open(label) as f:
    fdata = [line.strip() for line in f] #remove the space in the head and tail of label_month_all.txt
    lis=[i for i,x in enumerate(fdata) if x=='1'] #only list can use enumerate function
    ofp.write('\n'.join(map(str,lis)))    #only str can use join, write list element into ofp with new line
    lis_2=[j for j,x in enumerate(fdata) if x=='-1'] 
    ofn.write('\n'.join(map(str,lis_2)))
    a=len(lis)
    print '# of positive =',a  #number of positive rows
    b=len(fdata)  #number of total rows
    d=b-a
    nega=len(lis_2)
    print '# of negative =',d #number of negative rows
ofp.close()
ofn.close()
ofp_list=[]
#ofp_list.insert(line,1) 
#str1='# of positive ='+a='\n'+'# of negative='+d+'\n'


data_positive='data_'+month+'_positive.txt'
data_negative='data_'+month+'_negative.txt'
data='data_'+month+'_all.txt'
g=open(data_positive,'w')
m=open(data_negative,'w')
with open(data) as r:
    rdata=[line.strip() for line in r]    
    for num in lis: 
        g.write(rdata[num]+'\n')
    for count in lis_2:
        m.write(rdata[count]+'\n')
m.close()
f.close()
r.close()
g.close()

##======================================================


##===== randomly choose ================================

percentage=sys.argv[2]
percentage=int(percentage)
count=0
m=0
n=99
d_one_hundred=d/100 #d=number of negative
d_one_hundred=int(d_one_hundred)
lis_3=[]
label_negative_duplicate='label_'+month+'_negative_duplicate.txt'
h=open(label_negative_duplicate,'w')
for i in range(0,d_one_hundred):
    for j in range(0,percentage): 
        r1=random.randint(m,n)
        lis_3.append(r1)
    m+=100
    n+=100
    count=count+percentage
for item in lis_3:
    h.write("%s\n" % item)
print '# of randomly choose=',count 
residue=d%100
total=count+a #d+a=total*(100/percentage)+residue 
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
        

## ======= merge two files ================================

data_duplicate_all='data_'+month+'.txt'
filenames = [data_positive, data_duplicate]
with open(data_duplicate_all, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)  
outfile.close()
infile.close() 

##===========end of merging ================================

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

onedim_arr=np.zeros((1,b),dtype=np.int16)

##==== order.txt=======================================

ofp=open(order_positive,'r')
lnd=open(label_negative_duplicate,'r')
for line in ofp.readlines():
    line=int(line)
#    onedim_arr.put((0,line),1)
    onedim_arr.put(line,1)
for line2 in lnd.readlines():
    line2=int(line2)
    #onedim_arr.put((0,line2),-1)
    onedim_arr.put(line2,-1)
order=open('order.txt','w')
np.savetxt(order,onedim_arr,fmt="%d",delimiter="\n")
np.set_printoptions(threshold=np.inf)
order.close()

##======================================================


order=open('order.txt','r')
order_data=open('order_data.txt','w')
tmp=[]

data_all=open(data,'r')
order_line=order.readlines()
tmp=[i for i,element in enumerate(order_line) if element !='0\n']
data_all_list=[i for i in data_all.readlines()] #read the file and put every line into list element

for j in range(0,len(tmp)):
    for i,element in enumerate(data_all_list):
        #print 'i={},element={}'.format(i,element)
        if i==tmp[j]:
            order_data.write(element)
            continue
            
data_all.close()
order.close()
order_data.close()
        

##====== write number of positive and negative into d_record.txt ===============

with open("d_record.txt","a") as d_re:
    d_re.write("Month= %s" %month)
    d_re.write("   duplicate= %d" % percentage+'\n')
    d_re.write("# of positive = %d" % a+'\n') 
    d_re.write("# of negative = %d" % d+'\n')
    d_re.write("# of random negative = %d" %count+'\n')  #number of randomly chose negative 
    d_re.write("# of total row = %d" %total+'\n')  #total=count+a 
    d_re.write('\n')
d_re.close() 

## ============ end of step =======================================================
