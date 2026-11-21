# Arquitectura del sistema Software FJ

## Descripción general

Software FJ es un sistema de gestión de clientes, servicios y reservas desarrollado en Python mediante programación orientada a objetos.

## Arquitectura

El proyecto está organizado en módulos:

- clases: contiene las entidades, clientes, servicios y reservas.
- excepciones: contiene las excepciones personalizadas.
- logs: almacena los eventos y errores.
- evidencias: almacena las capturas de funcionamiento.
- documentacion: contiene la documentación técnica.

## Principios de programación orientada a objetos

### Abstracción
Se implementa mediante las clases abstractas Entidad y Servicio.

### Encapsulamiento
Los atributos internos se protegen mediante el uso de atributos privados por convención y propiedades.

### Herencia
Cliente y Servicio heredan de Entidad. Los servicios especializados heredan de Servicio.

### Polimorfismo
Los servicios especializados implementan sus propios métodos calcular_costo y describir.

### Sobrecarga
Se utilizan parámetros opcionales en calcular_costo para permitir diferentes variantes de cálculo con impuestos y descuentos.

## Manejo de excepciones

El sistema utiliza excepciones personalizadas para controlar errores de clientes, servicios, validaciones y reservas.

Los errores se registran automáticamente en el archivo eventos.log.

## Almacenamiento

El sistema utiliza objetos y listas en memoria. No utiliza bases de datos.
Los archivos se utilizan exclusivamente para registrar eventos y errores.