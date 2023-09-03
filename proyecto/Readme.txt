#===================================
	Proyecto Final - Python
	Juan David Bolivar

 Desarrollo : Aplicación Garantias
 Version: 1.0
#===================================


El proyecto desarrolla una aplicación que permite gestionar las garantías, las empresas, sucursales y el contacto de clientes.
En este sentido, se crean cuatro modelos que almacenan la información:

1. Modelo Garantias:
	-banco (STRING MAX. 50)
	-contrato (STRING MAX. 50)
	-valor (DECIMAL MAX. 10 y DOS decimales)
	-fecha_inicial 
	-fecha_final

2. Modelo Empresas:
	-nombre(STRING MAX. 50)
	-nit(INTEGER)

3. Modelo Contacto:
	-nombre(STRING MAX. 50)
	-apellido(STRING MAX. 50)
	-email(EMAIL)

4. Modelo Sucursal:
	-ciudad (STRING MAX. 50)
	-cantidad_empleados(INTEGER)

Todos los modelos cuentan con una representación (tabla) que permite realizar operaciones de adición, eliminación y modificación de la información, siempre y cuando el 
usuario cuente con un registro previo en la aplicación.

