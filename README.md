# Problema 1: compromiso de sesiones de clientes

Este programa lo hice para la Fase 5 (evaluación final) del curso Fundamentos de Programación de la UNAD. Trabaja con una matriz en la que cada fila es una sesión de un cliente en una plataforma digital, con este formato:

```
[ID del cliente, duración de la sesión en segundos, número de clics]
```

A partir de la duración y de los clics, el programa clasifica cada sesión con un nivel de compromiso y muestra un informe en la consola.

## Requisitos

Solo se necesita Python 3. Yo lo probé con Python 3.12 en Linux. No usa librerías externas, así que no hay que instalar nada más.

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```bash
python3 problema_1.py
```

En Windows el comando suele ser `python problema_1.py` o `py problema_1.py`.

## Reglas de clasificación

La función `clasificar_compromiso(duracion, clics)` revisa las condiciones en este orden y se queda con la primera que se cumple:

1. **Alto**: la duración es mayor que 180 segundos y hay más de 8 clics.
2. **Bajo**: la duración es menor que 60 segundos o hay menos de 3 clics.
3. **Medio**: cualquier otro caso.

El orden importa. Una sesión de 300 segundos con 2 clics es larga, pero como tiene menos de 3 clics no cumple la regla de Alto y termina en Bajo. También hay que fijarse en que las comparaciones son estrictas: una sesión de exactamente 180 segundos con 12 clics queda en Medio, porque 180 no es mayor que 180.

## Uso

Al arrancar aparece un menú:

```
1. Usar datos de prueba
2. Ingresar sesiones manualmente
Elija una opción:
```

Si se escribe algo distinto de 1 o 2, el programa vuelve a pedir la opción.

### Opción 1: datos de prueba

Carga una matriz fija con cinco sesiones. Sirve para revisar rápido que el programa funciona o para comparar con la prueba de escritorio. La salida es esta:

```
MATRIZ DE SESIONES
ID		Duración (s)	Clics
1		240		12
2		45		10
3		120		5
4		300		2
5		180		12

INFORME DE COMPROMISO
ID: 1 | Clasificación: Alto
ID: 2 | Clasificación: Bajo
ID: 3 | Clasificación: Medio
ID: 4 | Clasificación: Bajo
ID: 5 | Clasificación: Medio
```

### Opción 2: ingreso manual

Primero pregunta cuántas sesiones se van a registrar. El mínimo es 5; si se escribe un número menor, lo vuelve a pedir. Después, para cada sesión, pide el ID del cliente, la duración en segundos y el número de clics:

```
--- Sesión 1 de 5 ---
  ID del cliente: C001
  Duración en segundos: 200
  Número de clics: 9
```

El ID puede ser cualquier texto. La duración, los clics y la cantidad de sesiones tienen que ser números enteros. Si se escribe un decimal como `200.5`, una palabra, un número negativo o se deja vacío, aparece este aviso y se vuelve a pedir el mismo dato:

```
  Valor no válido. Ingrese un número entero sin decimales ni letras.
```

Cuando termina de recibir los datos, muestra la matriz y el informe igual que en la opción 1.

### Repetir la prueba

Al final de cada informe el programa pregunta:

```
¿Desea hacer una nueva prueba? (s/n):
```

Con `s` vuelve al menú y con `n` termina mostrando "Programa finalizado". Solo acepta `s` o `n` en minúscula; cualquier otra respuesta la vuelve a pedir.

## Cómo está organizado el código

El archivo empieza con dos funciones:

- `clasificar_compromiso(duracion, clics)` aplica las reglas de arriba con `if / elif / else`, guarda el resultado en la variable `nivel` y la retorna una sola vez al final.
- `leer_numero_entero(mensaje)` pide un dato con `input` y lo repite mientras el texto no esté formado solo por dígitos. Para eso usa el método `isdecimal()`. Cuando el dato es válido, lo convierte con `int` y lo retorna. Así evité que el programa se detenga con un error al convertir un texto como `"abc"` o `"9.5"`.

Después viene un ciclo `while` que se repite mientras la variable `nueva_prueba` valga `"s"`. Dentro de ese ciclo están el menú, la carga de la matriz, la impresión de la matriz y el informe. El informe recorre la matriz con un contador `i` que empieza en 0 y aumenta de uno en uno, que es el mismo recorrido que dibujé en el diagrama de flujo. En cada vuelta toma `sesiones[i][0]`, `sesiones[i][1]` y `sesiones[i][2]` y llama a `clasificar_compromiso`.

## Limitaciones conocidas

- Si un ID tiene 8 caracteres o más, esa fila de la tabla de la matriz se corre hacia la derecha, porque las columnas se separan con tabuladores.
- Un número escrito con espacios antes o después, como `" 12"`, se toma como inválido.
- El ID del cliente no se valida, así que se puede dejar vacío.
