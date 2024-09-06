A={'Tamil':92,'English':56,'Maths':88,'Science':97,'Social':89}
B={'Tamil':78,'English':68,'Maths':88,'Science':97,'Social':56}
for keys,values in A.items():
    for keys2,values2 in B.items():
        if keys==keys2:
            if values==values2:
                print(keys,values,'is present in A and B')
            