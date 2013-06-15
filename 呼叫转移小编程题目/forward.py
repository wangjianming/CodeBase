#coding=UTF-8
import re
import sys
#假定从文件读入记录
inputFile = "input.txt"
f = open(inputFile)

def handle_error(errmsg):
	"""
	异常检测的处理，直接打印错误信息后退出
	"""
	print errmsg
	sys.exit(0)

def getRecords():
	"""
	返回结果需包含两个值
	第一个值是要计算的日期
	第二个值是list，其中每个元素是一个tuple表示一条记录，内含4个元素，分别是被叫号码，呼转至的号码，呼转开始日，呼转结束日（含）
	"""
	
	#通过一个正则表达式来匹配一行呼叫转移记录是否正确，如果匹配，就可以直接通过匹配组找出需要的记录
	dataPattern = re.compile(r"""^\s*
							 (?P<first>\d{4})\s+           #the first number
							 (?P<second>\d{4})\s+          #the second number
							 (?P<startForwardDate>\d+)\s+  #start date
							 (?P<length>\d+)\s*            #len
							 $""",re.VERBOSE)
	theDate = 1
	records = []
	for index,data in enumerate(f.xreadlines()):
		if index == 0: # 第一行，呼叫转移的记录数
			try:
				recordNum = int(data)
			except:
				handle_error(u"data format error:<%s> at line %d" %(data.strip(),index+1))
		elif recordNum > 0:#普通呼叫转移记录
			matcher = dataPattern.match(data)
			if matcher:
				first = matcher.group("first")
				second = matcher.group("second")
				startForwardDate = int(matcher.group("startForwardDate")) 
				length = int(matcher.group("length"))
				records.append((first,second,startForwardDate,startForwardDate+length-1))
			else:
				handle_error(u"data format error:<%s> at line %d" %(data.strip(),index+1))			
			recordNum = recordNum - 1
		else:#这里是最后一行了
			try:
				theDate = int(data)
			except:
				handle_error(u"data format error:<%s> at line %d" %(data.strip(),index+1))
	return theDate,records
	
def calculate(theDate,records):
	"""
	根据题目给定条件计算并打印结果
	"""
	#找出符合如下条件的记录：如果要统计的天数在记录的开始和结束日中间
	theRecordsToday = [item for item in records if item[2] <=theDate<=item[3]]
	#结果组成一个map，key是呼入号，value是呼出号，如果出现一个人呼转至多个人的情况，后面的覆盖前面的数据
	recordsMap = dict([(item[0],item[1]) for item in  theRecordsToday] )
	if len(theRecordsToday) != len(recordsMap):
		handle_error(u"A same number have been forward more than once,pls check")
		
	#找出所有的号码,用set去掉重复
	allNumbers = set([item[0] for item in  theRecordsToday] + [item[1] for item in  theRecordsToday]) 
	maxForwardCallDepth = 0
	#从每个号码开始查找转移记录，并记录哪个最长
	for currentNumber in allNumbers:
		currentDepth = 0
		callee = recordsMap.get(currentNumber,None)
		while callee != None:
			callee = recordsMap.get(callee,None)
			currentDepth = currentDepth + 1			
			if currentDepth > len(recordsMap):
				#如果最大深度是否超过总记录，那么一定出现环路，由于set无序，所以很可能检测到的开始号码不是第一个出现环路的
				handle_error(u"loop occurred,pls check from number %s" %currentNumber)
		if currentDepth > maxForwardCallDepth:
			maxForwardCallDepth = currentDepth
	print u"第%d天共有%d条呼叫转移设置" %(theDate,len(recordsMap))
	print u"第%d天最长的呼叫转移是%d次" %(theDate,maxForwardCallDepth)

if __name__ == "__main__":
	theDate,records = getRecords()
	calculate(theDate,records)