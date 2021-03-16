"""Find out-of-place quotation marks."""
import re


def is_balanced(str):
	c = str.count('"')
	if c % 2 == 0:
		return True
	else:
		return False


def replace(str):
	pattern = '(?<=[a-zA-Z])\"(?=[a-zA-Z])'
	repl = "'"
	res = re.sub(pattern, repl, str)
	return res
