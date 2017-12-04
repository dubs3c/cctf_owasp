def decrypt(enc,key):
	flag_part1='CCTF{this_is'
	counter=0
	decrypted_flag=''
	for f in enc:
		if counter==len(key):
			counter=0
		decrypted_flag+=chr(ord(f)^ord(key[counter]))
		counter+=1
	if decrypted_flag.startswith('CCTF{this_is'):
		print decrypted_flag
	
alpha='abcdefghijklmnopqrstuvwxyz'
key_part2_words=['not','chalmers','and','am','with','playing','this','playing','is','planet','crypto','ctf','the','ninja','what','explain','key','hack','reversing','just']

flag=''
encrypted_flag=open("flag.enc", "rb").read()
print encrypted_flag

key_part1='code'
for w1 in key_part2_words:	
	for w2 in key_part2_words:
		for w3 in key_part2_words:
			key_part2=w1+'_'+w2+'_'+w3
			for k3 in key_part2_words:
				enc_key=key_part2+'_'+k3+'_'+key_part1
				decrypt(encrypted_flag,enc_key)

	