import os



#entries = os.listdir('/Users/Oriordanc/Desktop')

for filename in os.listdir('/Users/Oriordanc/Desktop'):
    if filename.endswith('.txt'):
        print(filename)
        
BL = dict(filename)
