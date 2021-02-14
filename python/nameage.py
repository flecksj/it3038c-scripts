import time

start_time = time.time()

print('what is your name?')
myname = input()
print('Hello, ' + myname + '. That is a good name, how old are you?')
myAge = int(input())
programAge = int(time.time() - start_time)
print('%s? Thats funny, Im only %s seconds old' % (myAge, programAge))
print("I wiSH i was %s years old" % (myAge *2))

time.sleep(3)
print('im tired')
