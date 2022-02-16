# View >> Syntax


print("Anyway...")


def make_class(x):
	class Dog:
		def __init__(self, name):
			print(x)

	return Dog

cls = make_class(10)
print(cls)

print'hello world'
print("hello world")

