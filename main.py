#EXPRESIÓN: Vf = Vi+A*T
Vi=20       #Velocidad inicial
A=9.8       #Aceleración
T=30        #Tiempo

Vf=Vi+A*T       #Velocidad final
print ("Vf = ", Vf)     #Imprimir velocidad final

Vi=Vf-(A*T)     #Velocidad inicial
print ("Vi = ", Vi)     #Imprimir velocidad inicial

A=(Vf-Vi)/T     #Aceleración
print ("A = ", A)       #Imprimir aceleración

T=(Vf-Vi)/A     #Tiempo
print ("T = ",T)        #Imprimir tiempo