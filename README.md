# N5 - Challenge
## Tony Yu - tonyyucen@gmail.com

### Repositorio Github

```
https://github.com/confixyu/n5-challenge-tony
```

### Ingresar al admin panel
Al admin panel de ingresa de manera directo, no tiene control de usuario u autenticación.

Ejemplo:
````commandline
http://localhost/admin
````

### Ingresar al Swagger

Ejemplo:
````commandline
http://localhost/docs
````

## Ejecutar el proyecto.

### Maquina
````commandline
pip install -r requirements.text

fastapi dev src/main.py
````

### Docker
Docker repositorio
````commandline
docker pull confixyu/n5-challenge-tony

or

https://hub.docker.com/repository/docker/confixyu/n5-challenge-tony/general
````
Ejecutar la image
````commandline
docker run -d -p 80:80 confixyu/n5-challenge-tony
````

Ejecutar con Dockerfile
````commandline
docker run -it -p 80:80 $(docker build -q .)
````

## Endpoints

### Cargar Multa
Este endoint se necesita un Bearer Token para poder realizar la petición, para obtener el token debe ingresar al admin panel /admin y crear un official de policia de manera automatica se le asigna un Bearer token, cada token identifica a un oficial.
```
curl --location 'localhost/cargar_infraccion' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RlIjoxMDAyfQ._PkPVnWavCveOI21vNH1OTlqGUHcixMDRPkCBfuVMbg' \
--data '{
  "plate": "AAA104",
  "comment": "Multa por obtrucción de tráfico"
}'
```



### Ver reporte
En este endpoint se lista todos los vehiculos con infracciones en caso de que lo tenga que le pertenece a la persona consultada por medio del email.

```
curl --location 'localhost/generar_informe/juan@mail.com'
```

### Propuesta de arquitectura

![img.png](img.png)

En esta arquitectura contemplando salida a producción fargate es una buena opcion debido a que los costos son menores aunque un EC2 tambien es buena opción, se usa una RDS postgres para la percistencia de datos, el fargate y la RDS se le asigana una VPC para controlar el ingreso no deseado por externos manajando la seguridad, se usa Route 53 para asignar un dominio y un Application Load Balancer para manejar el alto tráfico, agregando el WAF ayuda a mantener seguro el servicio evitando ataque cibernetico, el Secret key manager para manejo de credenciales. 


#### Muchas Gracias por darme la oportunidad de participar.