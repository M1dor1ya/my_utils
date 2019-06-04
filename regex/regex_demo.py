def judge_legal_ip(ip):
	#  正则匹配方法,判断一个字符串是否是合法IP地址
	compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
	if compile_ip.match(ip):
		return True
	else:
		return False