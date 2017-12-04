key_part1='code'
alpha='abcdefghijklmnopqrstuvwxyz'

key_part2=#this part is missing
key_part2_words=['not','chalmers','and','am','with','playing','this','playing','is','planet','crypto','ctf','the','ninja','what','explain','key','hack','reversing','just']

key_part3=#this part is missing

flag_part1='CCTF{this_is'
flag_part2=#this part is missing
flag_part3=#this part is missing
flag=flag_part1+flag_part2+flag_part3
encrypted_flag=''

if len(flag)==77:
	k1=''
	for c in key_part1:
		if c in alpha:
			k1+=c
		if len(k1)==4:
			break
	
	k2=''
	key_part2=key_part2.split('_')
	if len(key_part2)==3:
		for w in key_part2:
			if w in key_part2_words:
				k2+=w
				if key_part2[2]!=w:
					k2+='_'
				else:
					break
	
	enc_key=''
	if (len(key_part3)==4) and (key_part3 in key_part2_words):
		enc_key=k2+'_'+key_part3+'_'+k1
	
	counter=0
	for f in flag:
		if counter==len(enc_key):
			counter=0
		encrypted_flag+=chr(ord(f)^ord(enc_key[counter]))
		counter+=1
	
	flag_file = open("flag.enc", "w")
	flag_file.write(encrypted_flag)
	flag_file.close()

	