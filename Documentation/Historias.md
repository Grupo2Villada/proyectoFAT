# Historias de usuario
---------------
# Sprint 1

### Tareas Generales
* Configurar settings iniciales, requeriments y dependencias
> Crear requirement.txt en el cual se anoten todos los programas,dependencias y librerias necesarias para que el proyecto funcione
* Crear Base de Datos
> Seguir manual de django admin y cumplir con los requerimientos tomados con anterioridad
* Crear grupo de usuarios segun cargo y funcion
> Grupo de directivos
> Grupo de preceptores
> Grupo de administrativos
> Grupo de secretaria
> Grupo de alumnos 

### COMO usuario QUIERO poder loguearme PARA usar los servicios
* Html base
> footer 
> Navbar 
> background color (light-blue)
* Html login
> Usar html base y agregar
> Label usuario
> Label contraseña
> Button inciar sesion
* Funcion LogIn
> Mostrar error si el usuario o contraseña son incorrectos 
> Si todos los datos son validos re direcciona a la pagina index.html con los permisos habilitados segun el usuario que se logueo
* Funcion LogOut
> Salir de la pagina donde se encuentra en ingresar al login.html
* Urls
> Setear correctamente las urls y patterns como indica el manual de django 

## Desde Django Admin
### COMO directivo QUIERO tener funciones de preceptor
* Registrar model en admin.py
> Setear correctamente segun manual de django las funciones de preceptor y que las pueda hacer el grupo de directivos 
 
### COMO directivo QUIERO CRUD faltas sin limite de tiempo
* Registrar model en admin.py
> Setear correctamente segun manual de django las funciones estrictamente necesarias como directivo con el respectivo permiso necesario 
> Habilitar buttons cuando se inicie sesion como directivo 


### COMO directivo QUIERO C.R.U.D. users PARA administrar personas
* Registrar model en admin.py
> Setear permisos 
> Habilitar formulario en html para poder realizar dichas funciones 

### COMO preceptor QUIERO guardar faltas
* html con cursos por preceptor
> Habilitar html cuando se inicie sesion como preceptor y mostrar los cursos que tiene a cargo 
* html con alumnos por curso
> Crear html que tenga distribucion por cursos y a su ves que muestre que alumno esta matriculado en cada curso especificamente 
* view guardado faltas
> java script si se hace click desaparece 
> No se pueden colocar 2 faltas a la misma persona
* ajax guardado faltas
> cuando se hace click en el button de ausente se debe guardar en la base de datos 
* urls(una con id de curso)
-----------
# Sprint 2
---
##### Mejorar estetica de htmls de sprint 1
##### Correccion bugs
---
### COMO directivo QUIERO C.R.U.D. users PARA administrar personas
---
* html con formulario para registrar
---
* Campo username
> Validar cantidad minima de caracteres
> Posibilidad de caracteres especiales 
> imposibilidad de ser nulo 
> indiferencia entre mayusculas o minusculas 
* Campo firstname
> Validar cantidad minima de caracteres
> Posibilidad de caracteres especiales 
> imposibilidad de nulidad 
> Diferenciacion de mayusculas y minusculas
> No detectar puntos, comas, etc 
* Campo lastname
> Validar cantidad minima de caracteres
> Posibilidad de caracteres especiales 
> imposibilidad de nulidad 
> Diferenciacion de mayusculas y minusculas
> No detectar puntos, comas, etc 
> imposibilidad de ser nulo
* Campo email
> Diferencia entre mayusculas y minusculas
> Deteccion obligatoria de  @gmail, @hotmail,@yaoo, @donbosco 
> Deteccion obligatoria de .com, .org , .edu 
> imposibilidad de ser nulo
* Campo password 
> Ocultar caracteres
> Nivel minimo de seguridad (Cantidad de caracteres, tipo de caracteres, etc)
> Diferenciacion entre mayusculas y minusculas 
> imposibilidad de ser nulo
* Campo repit password 
> Ocultar caracteres
> Validar que sea igual que el campo password
> Diferenciacion entre mayusculas y minusculas 
> imposibilidad de ser nulo
* permiso para de staff para registrar
> Abrir html register cuando el usuario tenga el permiso de directivo  
* funcion render/register
> Registrar el preceptor y renderizar el html 
* urls
> Escribir urls siguiendo los protocolos de django 
* validación de datos
> Comprobar que todos los campos cumplan con las especificaciones y tipo de datos 

### COMO preceptor QUIERO Crear, administrar y mover alumnos PARA gestionar alumnos 
* html crear alumnos
> Utilizar html base y agregar formulario que contenga los siguientes campos.
* Campo firstname 
> Validar cantidad minima de caracteres
> Posibilidad de caracteres especiales 
> imposibilidad de nulidad 
> Diferenciacion de mayusculas y minusculas
> No detectar puntos, comas, etc 
* Campo lastname 
> Validar cantidad minima de caracteres
> Posibilidad de caracteres especiales 
> imposibilidad de nulidad 
> Diferenciacion de mayusculas y minusculas
> No detectar puntos, comas, etc 
* Campo dni 
> Validar cantidad de caracteres y el tipo (numericos unicamente)
> Eliminar puntos y tomar el dni sin numeros para guardarlo
> imposibilidad de nulidad 
* Campo student tag 
> Validar cantidad de caracteres y el tipo (numericos unicamente)
> Eliminar puntos y tomar el dni sin numeros para guardarlo
> imposibilidad de nulidad 
* Campo list_number
> Validar el tipo de caracter (numerico unicamente)
> imposibilidad de nulidad 
* Campo birthday
> Validar que el tipo de dato ingresado sea el valido  
> imposibilidad de nulidad 
* Campo address 
> imposibilidad de nulidad 
* Campo neighbourhood
> imposibilidad de nulidad 
* Campo city
> Validar que la ciudad exista 
> imposibilidad de nulidad 
* Campo year
> imposibilidad de nulidad 
* Campo status
> imposibilidad de nulidad 
* Campo food_obvs
> Posibilidad de nulidad 
* html editar alumnos
> Posibilidad de editar todos los datos que posee un alumno 
* view crear alumnos
> Clean code 
* view editar alumnos
> Clean code 
* urls
> Escribir urls siguiendo los protocolos de django 

-----------
## SPRINT 3

### COMO preceptor QUIERO registrar llegadas tardes -> 13sp
* html llegada tarde
> Mostrar todos los alumnos del curso del preceptor activo con su respectivo botón para demarcar la llegada tarde
> Descartar alumnos marcados

* view llegada tarde
> Dependiendo de la hora y/o porcentaje el símbolo que tendrá el alumno en la falta

* urls
> Escribir urls siguiendo los protocolos de django 

### COMO preceptor QUIERO retiros anticipados -> 13sp
* html retiros anticipados
> Mostrar todos los alumnos del curso del preceptor activo con su respectivo botón para demarcar el retiro anticipado tarde.

* view llegada tarde
> Dependiendo de la hora y/o porcentaje el símbolo que tendrá el alumno en la falta.

* urls
> Escribir urls siguiendo los protocolos de django.

### COMO preceptor QUIERO Justificar faltas dentro de 48 hs -> 5sp
* html justificar falta
> Mostrar todos los alumnos del curso del preceptor activo que hayan faltado con su respectivo botón para justificar y en el caso que se pueda, adjuntar el justificativo.

* view justificar falta
> Cambiar el estado de la falta del día correspondiente del alumno a justificada.

* urls
> Escribir urls siguiendo los protocolos de django 

### COMO directivo QUIERO tener permisos de preceptor -> 1sp
* Director podrá hacer todo lo demarcado anteriormente para el preceptor

### COMO directivo QUIERO modificar faltas sin limite de tiempo PARA poder justificarlas -> 2sp
* Desde el mismo html que el preceptor justifica, que el directivo lo haga, pero sin límite de tiempo.

### COMO tester QUIERO testear optimamente todos los sprints PARA que no haya errores atrasados -> 8sp

-----------
# Sprint 4

### Mejoras sprint planning -> 5sp
* Mejorar estética tarjetas elección de curso
* Cambiar la especifidad de la pestaña administrar
* Sacar la necesidad de campos que no hacen falta, incluyendo la modificación de los htmls.

### COMO sistema QUIERO generar Excels -> 21sp
* View para generar un excel mensual
> Generar un excel con nombres, fechas y faltas dependiendo a cada curso correspondientes al mes o día deseado.

* Crear botón en la view necesaria para generar un excel por curso
> Botón por curso que desprenda una selección de día o mes

### COMO sistema QUIERO enviar mails -> 5sp
* View para mandar el mail correspondiente al comedor
> La view necesita recolectar el número de alumnos en el día y sus menús particulares para mandar esas especificaciones al comedor

### COMO secretaría QUIERO recibir Excels mensuales PARA llevar registros de la gestión de los alumnos -> 5sp
* View para mandar el mail correspondiente a secretaría
> La view necesita recolectar el número de alumnos en el día para mandar esas especificaciones a secretaría

### COMO preceptor QUIERO recibir Excels mensuales PARA llevar registros de la gestión de los alumnos -> 1sp
* View para mandar el mail correspondiente al preceptor
> La view necesita recolectar el número de alumnos en el día esas especificaciones al preceptor

### COMO directivo QUIERO recibir Excels mensuales PARA llevar registros de la gestión de los alumnos -> 1sp
* View para mandar el mail correspondiente al directivo
> La view necesita recolectar el número de alumnos en el día esas especificaciones al directivo

### COMO administración QUIERO recibir Excels mensuales PARA llevar registros de la gestión de los alumnos -> 1sp
* View para mandar el mail correspondiente al administración
> La view necesita recolectar el número de alumnos en el día esas especificaciones al administración

* Html para elección de mail al que se mandan la cantidad de alumnos
> Poder cambiar el mail predeterminado al cual se le manda el mail con los datos diarios

-----------------
# Sprint 5

### COMO comedor QUIERO recibir cantidad de alumnos presentes diarios PARA hacer la comida 

### COMO administración QUIERO recibir un reporte diario PARA saber la cantidad de alumnos presentes
### COMO secretaría QUIERO recibir un reporte diario PARA saber la cantidad de alumnos presentes
### COMO directivo QUIERO recibir un reporte diario PARA saber la cantidad de alumnos presentes

### COMO comedor QUIERO recibir especificaciones especiales de alumnos PARA hacer dietas especiales
------------
