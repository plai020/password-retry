# 密碼重試程式
# pw = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有__次機會!"
pw = 'a123456'
chance = 3
while True:
	user_input = input('請輸入密碼(最多輸入3次):')
	if user_input == pw:
		print('登入成功!')
		break
	elif user_input != pw:
		chance -= 1
		if chance >= 1:
			print(f'密碼錯誤! 還有{chance}次機會!')
		elif chance == 0:
			print('已經嘗試3次了，不能再試了!')
			break