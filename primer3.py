#! /usr/bin/python2

class Kvader(object):
    kajjeto = "geom objekt"            #vsi kvadri
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def ploscina(self):
        return self.a * self.b
    def mojafunkcija(*args, **kwargs)
        print(args)
        print(repr(kwargs))


#class inheritance -> podeduje funkcije inpol gradis dodatne funkcije na klasu
#kvadrat podeduje funkcije
class Kvadrat(Kvader):
    def __init__(self,a):
        super(Kvadrat, self).__init__(a,a)#klices init funkcijo kvadra samo 2x y ajem


def main():
    kv = Kvader(1.0,2.0)#nardis objekt
    print(repr(kv.ploscina()))
    kvadrat = Kvadrat(2.0)
    print(repr(kvadrat.ploscina()))

if __name__== "__main__":
    main()