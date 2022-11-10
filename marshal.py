import os,marshal

os.system('clear')

f = input('Masukan file yg mau di encript : ')
o = input('Disimpan ke mana? : ')
b = open(f, "r").read()

c = compile(b, "", "exec")
en = marshal.dumps(c)
b2 = open(o, "w")

b2.write("import marshal\n")
b2.write("exec(marshal.loads"+repr(en)+"))")

print(en)
