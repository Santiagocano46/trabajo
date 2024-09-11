Este proyecto consiste en la creación de una aplicación para encriptar y desencriptar mensajes utilizando el algoritmo de cifrado simétrico AES (Advanced Encryption Standard). La encriptación simétrica es un método en el que el mismo algoritmo y clave se utilizan tanto para encriptar como para desencriptar la información.

Objetivos del proyecto:
Encriptación: Convertir un mensaje de texto claro (escrito por el usuario) en un mensaje cifrado (ilegible) utilizando una clave.
Desencriptación: Convertir un mensaje cifrado de vuelta a su forma original (mensaje en texto claro) utilizando la misma clave utilizada para encriptar.
¿Cómo funciona el proyecto?
Encriptación:

El usuario ingresa un mensaje y una clave de longitud válida (16, 24 o 32 bytes).
El mensaje se procesa utilizando el algoritmo AES con el modo CBC (Cipher Block Chaining), que divide el mensaje en bloques y los cifra uno a uno, encadenando los resultados.
El mensaje cifrado se devuelve como una secuencia de bytes que luego se puede mostrar en formato hexadecimal para facilitar su almacenamiento o transmisión.
Desencriptación:

El usuario ingresa el mensaje encriptado en formato hexadecimal y la misma clave que utilizó para encriptarlo.
El sistema descifra el mensaje, devolviéndolo a su estado original (texto legible), siempre y cuando la clave y el mensaje cifrado sean correctos.
¿Para qué sirve este proyecto?
Este proyecto puede ser útil para garantizar la seguridad y confidencialidad de la información. Al cifrar un mensaje, solo las personas que posean la clave correcta podrán descifrar y leer el contenido. Es una técnica común en la comunicación segura, como correos electrónicos cifrados, almacenamiento de contraseñas, y proteger datos sensibles durante su transmisión por la red.

Aplicaciones prácticas:
Proteger la privacidad en mensajes.
Asegurar la transmisión de datos entre dos puntos.
Mantener la integridad de información sensible en sistemas informáticos.
Este proyecto ofrece una introducción a la criptografía aplicada en sistemas reales, con un enfoque en el cifrado simétrico y la seguridad de la información.
