'''x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
x=float(input())
y=float(input())

on_left_side=(x==x1) and (y>=y1) and (y<=y2)
on_right_side=(x==x2) and (y>=y1) and (y<=y2)
on_up_side=(y==y1) and (x>=x1) and (x<=x2)
on_down_side=(y==y2) and (x>=x1) and (x<=x2)
if on_left_side or on_right_side or on_down_side or on_up_side:
    print('Border')
else: print('Inside/Outside')'''



'''import math

h = int(input())
x = int(input())
y = int(input())
in_down_rectangle = (0 <= x <= 3 * h) and (0 <= y <= h)
on_border_down_rectangle = (x == 0 or x == 3 * h or y == 0 or y == h) and in_down_rectangle
in_upper_rectangle = (h <= x <= 2 * h) and (h <= y <= 4 * h)
on_border_upper_rectangle = (x == h or x == 2 * h or y == h or y == 4 * h) and in_upper_rectangle
if on_border_down_rectangle or on_border_upper_rectangle:
    print("border")
elif in_down_rectangle or in_upper_rectangle:
    print("inside")
else: print("outside")'''


'''grade=int(input())
if grade>=5.50:
    print('Excellent!')'''


'''import sys
n=int(input())
oddSum=0
evenSum=0
oddMax=-sys.maxsize
evenMax=-sys.maxsize
oddMin=sys.maxsize
evenMin=sys.maxsize
for i in range(1,n+1):
    a=float(input())
    if i%2==1:
        oddSum=oddSum+a
        if a>oddMax:
            oddMax=a
        if a < oddMin:
            oddMin = a
    else:
        evenSum=evenSum+a
        if a>evenMax:
            evenMax=a
        if a < evenMin:
            evenMin = a'''





'''print(f'OddSum={odd_sum}')

if odd_min!=sys.maxsize:
    print(f'OddMin={oddMin}')
else:print(f'OddMin=No')

if oddMax!=-sys.maxsize:
    print(f'OddMax={oddMax}')
else:print(f'OddMax=No')



print(f'EvenSum={evenSum}')
if evenMin!=sys.maxsize:
    print(f'EvenMin={evenMin}')
else:print(f'EvenMin=No')

if evenMax!=-sys.maxsize:
    print(f'EvenMax={evenMax}')
else:print(f'EvenMax=No')
'''




''''sum=0
previoussum=None
diff=0
maxdiff=0
n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=int(input())
    sum=a+b
    if previoussum is not None:
        diff=abs(sum-previoussum)
    if diff>maxdiff:
        maxdiff=diff
    previoussum=sum

if maxdiff!=0:
    print(f"No, maxdiff={abs(maxdiff)}")
else: print(f'Yes, value={sum}')'''



'''n=int(input())
p1=0
p2=0
p3=0
p4=0
p5=0
for i in range(1,n+1):
    a=int(input())
    if a<200:
        p1+=1
    elif a>=200 and a<400:
        p2+=1
    elif a>=400 and a<600:
        p3+=1
    elif a>=600 and a<800:
        p4+=1
    else:
        p5+=1
print(f'{round((p1/n)*100,2)}%')
print(f'{round((p2/n)*100,2)}%')
print(f'{round((p3/n)*100,2)}%')
print(f'{round((p4/n)*100,2)}%')
print(f'{round((p5/n)*100,2)}%')'''

''' n=int(input())
washingmachine=float(input())
toyprice=int(input())
toy=0
money=10
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=(money-1)
        money+=10
    else:
        toy+=1
all_money=toy*toyprice+sum
if all_money-washingmachine>=0:
    print(f'Yes! {all_money-washingmachine:.2f}')
else:
    print(f'No! {washingmachine-all_money:.2f}')
'''

'''inheritance=float(input())
year_till_live=int(input())
yearsold=18
spent=0
for  i in range(1800, year_till_live+1):
    if i%2==0:
        spent+=12000
    else:
        spent+=12000+50*yearsold
    yearsold+=1
if inheritance-spent>=0:
    print(f'Yes! He will live a carefree life and will have {(inheritance-spent):.2f} dollars left.')
else:
    print(f'He will need {(spent-inheritance):.2f} dollars to survive.')'''

'''period=int(input())
treated=0
untreated=0
doctors=7
for i in range(1,period+1):
    if i%3==0:
        if untreated>treated:
            doctors+=1
    patients=int(input())
    if doctors>=patients:
        treated+=patients
    else:
        treated+=doctors
        untreated+=patients-doctors


print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')'''

# n=int(input())
# print('+', end='')
# for i in range(n-2):
#     print(' -', end='')
# print(' +')
#
# for i in range(n-2):
#     print('|', end='')
#     for column in range(n-2):
#         print(' -', end='')
#     print(' |')
#
# print('+', end='')
# for i in range(n-2):
#     print(' -', end='')
# print(' +')

# n=int(input())
# for row in range(n+1):
#     stars='*'*row
#     spaces=' ' * (n-row)
#     print(spaces, end='')
#     print(stars, end='')
#     print(' | ', end='')
#     print(stars, end='')
#     print(spaces)




# n=int(input())
# print('*'*(2*n), end='')
# print(' '*n, end='')
# print('*'*(2*n), end='')
# print()
#
# for i in range(n-2):
#
#     print('*', end='')
#     print('/' * ((2 * n) - 2), end='')
#     print('*', end='')
#
#     if i==(n-1)//2-1:
#         print('|'*n, end='')
#     else: print(' '*n, end='')
#
#     print('*', end='')
#     print('/' * ((2 * n) - 2), end='')
#     print('*', end='')
#     print()
#
# print('*'*(2*n), end='')
# print(' '*n, end='')
# print('*'*(2*n), end='')


# import math
# n=int(input())
# stars=1
# if n%2==0:
#     stars+=1
# roof_length=math.ceil(n/2)
# for i in range(roof_length):
#     padding=(n-stars)%2
#     line='-'*padding + '*'*stars + '-'*padding
#     print(line)
#     stars+=2
#
# for i in range(n//2):
#     line='|'+'*'*(n-2)+'|'
#     print(line)

# n=int(input())
# spaces=(n-1)%2
# for i in range(0, (n-1)%2):
#     spaces+=1
#     print('-'*spaces, end='')
#     print('*', end='')
#     mid = n - 2 * spaces - 2
#     if mid>=0:
#         print('-'*mid, end='')
#         print('*', end='')
#     print('-'*spaces)


#
#
# while True:
#     try:
#         print('Enter even number: ', end='')
#         n=int(input())
#         if n%2==0:
#             print(f'Even number entered: {n}')
#             break
#     except ValueError:
#         print('Invalid number.')


# n=int(input())
# num=1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num, end=' ')
#         num+=1
#         if col>=row:
#             print()
#         if num>n:
#             break
#     if num>n:
#         break


#n=int(input())

# result=''
# for i1 in range(1,10):
#     for i2 in range(1,10):
#         for i3 in range(1,10):
#             for i4 in range(1,10):
#                 for i5 in range(1,10):
#                     if i1*i2*i3*i4*i5==n:
#                         result+=(''+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+ ' ')
#
# print(result)



# n=int(input())
# for i in range(1111, 10000):
#
#     while n>0:
#         p=n%10
#
#     if p!=0:
#         if i%p==0:
#             print(i)
#     else: break
#     n=n//10


# x=int(input())
# y=int(input())
# inout=False
# if 2<=x<=12 and 1>=y>=-3:
#     inout=True
# elif 4<=x<=10 and 3>=y>=-5:
#     inout=True
# else:
#     inout=False
# if inout:
#     print('in')
# else:
#     print('out')


# d=int(input())
# m=int(input())
# nextday=d+5
# if m==4 or m==6 or m==9 or m==11:
#     if nextday>30:
#         m+=1
#         nextday-=30
# elif m==2:
#     if nextday>28:
#         m+=1
#         nextday-=28
# else:
#     if nextday>31:
#         m+=1
#         nextday-=31
# if m>12:
#     m-=12
# if m<10:
#     print(f'{nextday}.0{m}')
# else:
#     print(f'{nextday}.{m}')




