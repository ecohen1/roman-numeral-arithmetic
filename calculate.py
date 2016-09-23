import sys

firstNum = str(sys.argv[1])
operation = str(sys.argv[2])
secondNum = str(sys.argv[3])

expand = {
	'V': 'IIIII',
	'X': 'VV',
	'L': 'XXXXX',
	'C': 'LL',
	'D': 'CCCCC',
	'M': 'DD'
}

largerNumerals = {
	'I': 'VXLCDM',
	'V': 'XLCDM',
	'X': 'LCDM',
	'L': 'CDM',
	'C': 'DM',
	'D': 'M',
	'M': ''
}

contract = {
	'IIIII': 'V',
	'VV': 'X',
	'XXXXX': 'L',
	'LL': 'C',
	'CCCCC': 'D',
	'DD': 'M'
}

contractSecond = {
	'IIII': 'IV',
	'XXXX': 'XL',
	'CCCC': 'CD',
}

def expandNum(numeralString):
	wasNumeralExpanded = True
	expandedNumeral = numeralString
	remainderHash = {
		'I':'',
		'V':'',
		'X':'',
		'L':'',
		'C':'',
		'D':'',
		'M':''
	}
	while wasNumeralExpanded:
		wasNumeralExpanded = False
		numeralHolder = ''
		skipFlag = False
		for index in range(len(expandedNumeral)):
			if not skipFlag:
				num = expandedNumeral[index]
				if index < len(expandedNumeral) - 1:
					nextnum = expandedNumeral[index+1]
					if nextnum in largerNumerals[num]:
						numeralHolder += expand[nextnum]
						remainderHash[num] += num
						skipFlag = True
						wasNumeralExpanded = True
					elif num == 'I':
						numeralHolder += 'I'
					else:
						numeralHolder += expand[num]
						wasNumeralExpanded = True
				else:
					if num == 'I':
						numeralHolder += 'I'
					else:
						numeralHolder += expand[num]
						wasNumeralExpanded = True					
			else:
				skipFlag = False
		expandedNumeral = numeralHolder
	remainder = ''
	for key in remainderHash.keys():
		remainder += remainderHash[key]
		remainderHash[key] = ''
	remainder = numeralSort(remainder)
	expandedRemainder = simpleExpandNum(remainder)
	return 'I'*(len(expandedNumeral) - len(expandedRemainder))

def simpleExpandNum(numeralString):
	wasNumeralExpanded = True
	expandedNumeral = numeralString
	while wasNumeralExpanded:
		wasNumeralExpanded = False
		numeralHolder = ''
		for num in expandedNumeral:
			if num == 'I':
				numeralHolder += 'I'
			else:
				numeralHolder += expand[num]
				wasNumeralExpanded = True					
		expandedNumeral = numeralHolder
	return expandedNumeral

def contractNum(numeralString):
	wasNumeralContracted = True
	contractedNumeral = numeralString
	countHash = {
		'I':'',
		'V':'',
		'X':'',
		'L':'',
		'C':'',
		'D':'',
		'M':''
	}
	while wasNumeralContracted:
		wasNumeralContracted = False
		numeralHolder = ''
		for num in contractedNumeral:
			countHash[num] += num
			if countHash[num] in contract.keys():
				numeralHolder += contract[countHash[num]]
				countHash[num] = ''
				wasNumeralContracted = True
		remainder = ''
		for key in countHash.keys():
			remainder += countHash[key]
			countHash[key] = ''
		contractedNumeral = numeralHolder + remainder
	contractedNumeral = numeralSort(contractedNumeral)
	contractedNumeral = simpleContractNum(contractedNumeral)
	return contractedNumeral

def simpleContractNum(numeralString):
	numeralString = numeralString.replace('IIII','IV')
	numeralString = numeralString.replace('XXXX','XL')
	numeralString = numeralString.replace('CCCC','CD')
	return numeralString

def numeralSort(contractedNumeral):
	finalString = ''
	for letter in ['M','D','C','L','X','V','I']:
		finalString += contractedNumeral.count(letter)*letter
	return finalString

if operation == 'plus':
	firstExpanded = expandNum(firstNum)
	secondExpanded = expandNum(secondNum)
	totalExpanded = firstExpanded + secondExpanded
	print len(firstExpanded)
	print len(secondExpanded)
	print len(totalExpanded)
	answer = contractNum(totalExpanded)
	print answer
elif operation == 'minus':
	firstExpanded = expandNum(firstNum)
	secondExpanded = expandNum(secondNum)
	if len(firstExpanded) <= len(secondExpanded):
		print 'can\'t represent negative value'
	else:
		totalExpanded = firstExpanded
		for i in secondExpanded:
			totalExpanded = totalExpanded[:-1]
		print len(firstExpanded)
		print len(secondExpanded)
		print len(totalExpanded)
		answer = contractNum(totalExpanded)
		print answer
else:
	print 'operation not supported'