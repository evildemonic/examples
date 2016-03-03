def trip():
	fakeReasonToIndent = 1
	if fakeReasonToIndent == 1:
		someCheck = 1
		if someCheck == 1:
			print("""
				text that
				follows normal indenting
				in source
				whitespace to my left is preserved
				and appears on output
				""")


def fixedTrip():
	fakeReasonToIndent = 1
	if fakeReasonToIndent == 1:
		someCheck = 1
		if someCheck == 1:
			print("""
text that
BREAKS normal indenting
in source
whitespace to my left is AVOIDED
so as not to appear on output
				""")

def easyMistake():
	fakeReasonToIndent = 1
	if fakeReasonToIndent == 1:
		someCheck = 1
		if someCheck == 1:
			print("""oops i put something here and it doesn't end up aligned
				text that
				follows normal indenting
				in source
				whitespace to my left is preserved
				and appears on output
				""")

def normalMethod():
	fakeReasonToIndent = 1
	if fakeReasonToIndent == 1:
		someCheck = 1
		if someCheck == 1:
			print("\n"
				"this\n"
				"may be\n"
				"a better way\n"
				"to handle this\n"
				"it looks cleaner in code\n"
				"and is more C-like\n")

trip()
fixedTrip()
easyMistake()
normalMethod()
