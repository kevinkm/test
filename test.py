list1=['rt-ac54u.lan (192.168.101.1) at 20:76:93:31:2b:30 on en0 ifscope [ethernet]',
       'tina.lan (192.168.101.46) at 6c:8d:c1:ac:a3:29 on en0 ifscope [ethernet]',
       '? (192.168.101.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]',
       '? (192.168.101.255) at ff:ff:ff:20:76:93 on en0 ifscope [ethernet]'
       ]

listip,listmac=[],[]
for i in range(len(list1)):
    if '20:76:93' in list1[i]:
        s=list1[i]
        print(s)

        a=s[s.find("(")+1:s.find(")")]
        b=s[s.find("at")+2:s.find("on")].strip()
        print (a)
        print (b)
        listip.append(a)
        listmac.append(b)
print('final: ')
print((listip) +listmac)


