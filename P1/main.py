def errorHandler ():
    return 'opcion invalida'

def salir ():
    exit()

def start():
    archive = open('AF.txt', 'r')
    data = archive.read()
    archive.close()
    af = automa(data)

class automa:
    q = []
    f = []
    s = []
    e = []
    d = []
    aux = []

    def __init__(self, data):
        un = data.split('\n')

        for i in range(len(un)):
            if i == 0:
                self.q = un[i].split(',')
            elif i == 1:
                self.f = un[i].split(',')
            elif i == 2:
                self.s = un[i].split(',')
            elif i == 3:
                self.e = un[i].split(',')
            else:
                self.d.append(un[i].split(','))

        #se recorreo el con el rango de lend
        self.af_complet()

    def af_complet(self):
        err = self.q[-1]
        err = int(err) + 1
        self.q.append(str(err))
        for s in self.q:
            for e in self.e:
                if not (s, e) in self.d:
                    self.aux.append(f'{s}, {e}, {err}\n')

        un = "".join(self.aux)
        un = un.split('\n')

        for i in range(len(un)):
            self.d.append(un[i].split(','))
        self.d.pop(-1)

        cadena(self.d)



def cadena (d):
    print(d)

if __name__ == '__main__':
    menu = True
    while True:
        print('''
            Menu de automatas
            1.- Ingresar automata
            2.- Salir
            ''')
        opp = int(input('Opcion: '))

        init = {
            1: start,
            2: salir
        }
        init.get(opp, errorHandler)()


'''
Lista y diccionario
     .append(dato) añadir dato al final
     .extends(seq) añadir secuencia de datos al final
     .insert(idx,dato) insertar dato en el idx
     .remove(dato) Eliminar el elem con el dato
     .pop([idx])->dato remueve y regresa el dato el la posicion idx(ultima posicion default)
     .clear() borrar datos de la lista
     .sort() ordena los datos de forma asendente
     .reverse() ordena los datos de forma desendente
     .index(dato,inicio,fin)  inicio y fin son opcionales
'''
