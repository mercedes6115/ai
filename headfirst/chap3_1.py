found = {}


found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

print(found)
found['e'] = found['e'] + 1 # 키 값을 통한 밸류값 증가
print(found)

for k in found:
    print(k, 'was found',found[k],'time(s)')