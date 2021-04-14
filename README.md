# isd-utils

## subnetcal
Dado una forwarding table, calcula el puerto de salida del paquete
utilizando LPM (longest prefix match)

* Se debe crear un archivo con el sigueinte formato 
ip1/mascara1"\n"
ip2/mascara2"\n"
ip3/mascara3"\n"
...
ipN/mascaraN"\n"

* Ejecucion: python3 ./subnetcalc 
Se van introduciendo las ips y el el programa devolverá el puerto de salida

## pckfragcalc
Calcula la tabla de fragmentacion de un paquete a lo largo de una conexion
formada por N routers
* 
* Ejecucion: python3 ./pckfragcalc -r "cantidad de routers" -p "payload inicial"
