#!/usr/bin/env python

def domain(usuario):
	for i in range(len(usuario)):
		for j in range(len(usuario[i])):
			if usuario[i][j] == "@":
				return (domain[i])
					
def mail(correo):
	for i in range(len(correo)):
		if correo[i] == "@":
			m = correo[:+ 1:] 
			return (mail[i])
def main(args):
	usuario = ("Carlos","Migal Riaño","PC1","192.168.6.2","carlosmigria@gmail.com")
	correo = mail(usuario)
	dominio = domain(mail)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
