<p align="left">
  <img width="150"  src=https://github.com/CodeSystem2022/AsistenciaCodeStyle/blob/main/assets/CodeStyleTransparent.png>
  2023
</p>

<h1 align="center">Proyecto Integrador Centro Nutricional Online   </h1>

## Descripción

El proyecto consiste en un sitio web  destinado a proporcionar servicios de asesoramiento y seguimiento nutricional personalizado

### A partir de un Dashboard se podra realizar :

* **Evaluaciones completas:** Realiza evaluaciones de la condición física y de salud de los clientes para diseñar planes nutricionales adaptados a sus necesidades individuales.
* **Enfoque personalizado:** Proporciona planes de alimentación personalizados que consideran las necesidades calóricas, los requerimientos nutricionales y las restricciones alimentarias de cada cliente.
* **Seguimiento y apoyo continuo:** Ofrece seguimiento regular y apoyo a los clientes para garantizar el cumplimiento de los planes nutricionales y lograr resultados exitosos.

## Tecnologías a usar para el Backend
|Tecnologías|   |
 |------|-------|
 | Python | <code><img height="20" alt="python" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> |
 | Postgresql | <code><img height="20" alt="PostgreSQL" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/postgresql/postgresql.png"></code> |

## Tecnologías a usar para el frontend

  |Tecnologías|  |
  |------|-------|
|  Html  | <code><img height="20" alt="HTML" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code> |
| Css   | <code><img height="20" alt="CSS" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code> |
| javaScript | <code><img height="20" alt="javascript" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>|
| Boostrap | <code><img height="20" alt="bootstrap" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png"></code>|


## Proceso

**En esta primera instancia se esta implementado pruebas con la base de datos realizando CRUDs para hacer conexiones**

<h2 align="center"><img width= "500"src="https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/blob/main/Documentaci%C3%B3n/DER-pacientes.png"> </h2>

### lo que se puede hacer:
  - [x]  Ingresar un nuevo paciente
  - [x]   Editar paciente
  - [x]   Eliminar paciente
  - [x]   Buscar paciente
  - [x]   Listado de pacientes
  - [x]   Listado de pacienes eliminados


**Usamos el siguiente UML**
<h2 align="center"><img width= "500"src=https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/blob/main/Documentaci%C3%B3n/UML-centroNutricional.png> </h2>

## Pasos para ejecutar el CRUD en la base de datos por consola

 * Descargar la base de datos Centro Nutricional
 * abrir pgAdmin4 pestaña File opción preferences
![image](https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/assets/91083049/e3f62f1c-fd18-41e4-a3d6-f19b8edd2fee)

* dentro de Paths opcion Binary paths copiar tu ruta de instalación de Postgresql del archivo bin como en el ejemplo de la imagen y guardar
  ![image](https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/assets/91083049/0707a54d-cd9c-40d5-a350-de5b4b28750c)

* crear una nueva base de datos con el mismo nombre de la bbdd descargada en el primer paso
  * click derecho en Database --> create --> Database
  ![image](https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/assets/91083049/55cbf433-0132-4bbb-a559-18bb63d4db96)

* en la nueva base de datos creada click derecho -->opcion  "Restore"
  * en Filename buscar la bbdd descargada en el primer paso
![image](https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023/assets/91083049/1b250b7f-6546-46d1-87aa-2ddbfff6f22f)

* Datos importantes para la configuración
* 
            class Conexion:
              _DATABASE='centronutricional'
              _USERNAME= 'postgres'
              _PASSWORD= 'admin'
              _DB_PORT= '5432'
              _HOST = '127.0.0.1'

-------

  ### **Como nos manejamos en el proyecto:** visita nuestra wiki :books:
  
  [Wiki Centro Nutricional](https://github.com/CodeSystem2022/integrador_CodeStyle_Centronutricional_2023.wiki.git)
  
  





