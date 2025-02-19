from collections import deque

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_kosong(stack):
        return stack.pop()

def is_kosong(stack):
    return len(stack)==0

def reverse_kata(input_kata):
    stack = deque()

    for char in input_kata:
        push(stack, char)

    pembalik_kata = ""
    while not is_kosong(stack):
        pembalik_kata += pop(stack)

    return pembalik_kata

while True:
    input_kata = input("Masukkan kata: ")
    pembalik_kata = reverse_kata(input_kata)
    print("Hasil pembalikan: ",pembalik_kata)
    
    s = input("apakah ingin lanjut?(y/n)")
    if s == 'n'.lower() and 'n':
        break
    else:
        continue