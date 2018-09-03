a = raw_input()
curr = ord('a') - 1
for i in a:
    if ord(i) == curr + 1:
        curr += 1
    elif ord(i) <= curr:
        continue
    else:
        print "NO"
        exit(0)
print "YES"
