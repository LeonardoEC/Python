from ntpath import join
from os import remove

Casa_de_Lara = ["el papa de Lara","la mama de Lara","Lara"]
Casa_de_Antonela = ["el hermano de antonela","la mama de antonela","Antonela"]
Cine = []
#Visita a Lara
Casa_de_Lara.append("Andrea")
print("En la casa de Lara estan, {}, {}, {} y llego {}".format(Casa_de_Lara[0],Casa_de_Lara[1],Casa_de_Lara[2],Casa_de_Lara[3]))

#Visita a Antonela
Casa_de_Antonela.extend([Casa_de_Lara[2],Casa_de_Lara[3]])
print("En la casa de Antonela estan, {}, {} y {} hasta que llegaron {} y {}".format(Casa_de_Antonela[0],Casa_de_Antonela[1],Casa_de_Antonela[2],Casa_de_Antonela[3],Casa_de_Antonela[4]))
Casa_de_Lara.remove(Casa_de_Lara[2])
Casa_de_Lara.remove(Casa_de_Lara[2])

#Llego Emilia
Casa_de_Antonela.append("Emilia")

#La mama de Antonela, las lleva al cine

Cine.extend([Casa_de_Antonela[1],Casa_de_Antonela[2],Casa_de_Antonela[3],Casa_de_Antonela[4],Casa_de_Antonela[5]])
print(f"Fueron al cine {Casa_de_Antonela[1]}, {Casa_de_Antonela[2]}, {Casa_de_Antonela[3]}, {Casa_de_Antonela[4]} y {Casa_de_Antonela[5]}")
Casa_de_Antonela.remove(Casa_de_Antonela[1])
Casa_de_Antonela.remove(Casa_de_Antonela[1])
Casa_de_Antonela.remove(Casa_de_Antonela[1])
Casa_de_Antonela.remove(Casa_de_Antonela[1])
Casa_de_Antonela.remove(Casa_de_Antonela[1])

En_cine = ",".join(Cine[:4])

#Resolucin
print("En la casa de Lara quedaron",len(Casa_de_Lara),"y".join(Casa_de_Lara))
print("En la casa de Antonela quedaron",len(Casa_de_Antonela),",".join(Casa_de_Antonela))
print("En el cine estan", En_cine,"y", Cine[4])