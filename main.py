""""
1-Crear una funcion que pase de entero >0 y <4000 a romano
2-Cualquier otra entrada debe dar error
3-Limite 3999

Casos de prueba
a)1994 -> MCMXCIV
b)4000 -> RomanNumberError
c)"unacadena" -> RomanNumberError("Debe ser un entero")
d)0 -> RomanNumberError("El valor debe ser mayor de cero")
e)-4 -> RomanNumberError("El vvalor debe ser mator de cero")
f)4.5 -> RomanNumberError("Deber ser un entero")

M -> 1000
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1

"""

dic_entero_romano = {
1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
 10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
1000:"M",2000:"MM",3000:"MMM"
}

class RomanNumberError( Exception ):
    pass

#1994
def entero_a_romano(numero):
    numero = "{:0>4d}".format(numero)
    list_numero = list(numero)#Transformando a lista ['1','9','9','4']
    valor_romano = ""

    cont = 0
    valor_num = 1000
    while cont < len(list_numero):
        list_numero[cont] = int(list_numero[cont])*valor_num
        valor_romano += dic_entero_romano.get(list_numero[cont],"")
        cont+=1
        valor_num /= 10


    return valor_romano

print( entero_a_romano(1994))