files = {"readme.txt": "You are using a shell written in python it doesnt has access to your files but emulating a storage", "dir": {"text.txt": "yeh."}}
dir = files
def changeto(directory,directories):
	if directory in directories:
		return directories[directory]
	else:
		print('Directory doesnt exist')
def path(path,root):
	pth = root
	for i in path.split('/'):
		try:
			pth = pth[i]
		except:
			print(f'Folder "{i}" Does not exist')
		beforepth = pth
	return pth
def remove(path,element):
	if element in path:
		del path[element]
	else:
		print(f'File/Folder "{element}" Does not exist')
def createdir(path,name):
	path[name] = {}
def touch(path,name):
	path[name] = ''
def edit(path,name):
	if name in path:
		if type(path[name]) == str:
			print('Type "exit."" to exit')
			while True:
				m = input(f'{name} > ')
				if m != "exit.":
					path[name]+=m+"\n"
				else:
					break
		else:
			print('Not a file.')
	else:
		print("File doesnt exist")
def read(path,name):
	if name in path:
		if type(path[name])==str: print(path[name])
	else:
		print("File doesnt exist")
print("Welcome to the python os")
print('Type "help" for list of commands')

while True:
	inpt = input('> ')
	try:
		argv = inpt.split()[1::]
		cmd = inpt.split()[0]
	except:
		argv=[]
		cmd=""
	if cmd == "goto" and len(argv) > 0:
		dir = changeto(argv[0],dir)
	elif cmd == "list":
		for i in dir:
			print(i,end=' ')
		print()
	elif cmd == 'read' and len(argv) > 0:
		read(dir,argv[0])
	elif cmd == 'rem' and len(argv) > 0:
		remove(dir,argv[0])
	elif cmd == 'create' and len(argv) > 0:
		touch(dir,argv[0])
	elif cmd == 'createdir' and len(argv) > 0:
		createdir(dir,argv[0])
	elif cmd == 'write' and len(argv) > 0:
		edit(dir,argv[0])
	elif cmd == 'setpath' and len(argv) > 0:
		dir = path(argv[0], files)
	elif cmd == 'home':
		dir = files
	elif cmd == 'print':
		print(' '.join(argv))
	elif cmd == 'help':
		print('''goto - Go to an directory
list - Lists all files in directory
read - Prints text in file
rem - Removes file
create - Opposite of rem
createdir - Creates dir
write - Writes to a file. Make sure to not make a error/typo
setpath - Sets path to specified path
home - Sets path to home
help - Prints this text
note - Prints note
print - Prints specified text
helloworld - Example program''')
	elif cmd == "helloworld":
		print("Hello, World!")
	elif cmd == 'note':
		print("I know that you cant make a operating system in python, its just a tiny operating system emulator which has no your files access")
	else:
		print("No arguments specified or not a valid program")