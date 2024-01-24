# variabel string
nama = 'lulu'

print(f'hi {nama}')

#accessing string elemens
str = "python string"
print(str[0])
print(str[1])

str= "luthfiyah syaharani"
print(str[-3])

# operasi bilangan integers
print(20+20)
print(20-20)
print(20*20)
print(20/20)
print(20**2)
print(20//2)
print(20%9)

# float sama dengan integers tapi untuk angka desimal
print(2+1.0)

# underscores in numbers
count = 10_000_000_000
print(count)

# type convertions

price = input('masukan harga: ')
tax = input('tax rate: ')

tax_amount = int(price) * int(tax) / 100
print(f'pajaknya segini sis : {tax_amount}')

#if else
age = input('enter your age: ')
if int(age) >= 18:
    print('Youre eligible to vote')
else:
    print('youre not eligible to vote')

# for loop
# range(start, stop, step)

#while loop
command = ''

# while command.lower() != 'quit':
#     command = input('>')
#     print(f'Echo: {command}')

#break
for index in range(0, 10):
    print(index)
    if index == 3:
        break

#continue
for index in range(5):
    if index == 3:
        continue
    print(index)

