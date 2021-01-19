# Creacion de capa de datos para la entidad persona

### Clase conexion

Esta clase administra la conexion a la base de datos, trabajaremos con localhost, pero puede ser una ip, etc.
- Los atributos subrayados significa que son estaticos.
- Responsabilidad: administrar la conexion a la bd

### Clase PersonaDAO

DAO: Patron de diseño(Data Access Object), permite ejecutar las consultar y operaciones sobre una entidad.

Separa la responsabilidad de la base de datos.
- Lista informacion de la tabla persona.
- Ejecuta consultas y operaciones a la BD.

Responsabilidad: Realiza operaciones sobre la base de datos de la entidad persona.

### Clase Persona

Representa un registro de la tabla persona.

Responsabilidad: Crear objetos de la clase persona

