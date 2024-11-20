# POO_Reto01_Manuel_T

1. algoritmo que define si una palabra es palíndromo: Para resolver el problema de verificar si una palabra es un palíndromo de manera eficiente, decidí comparar solo los caracteres desde el principio y el final de la palabra, recorriendo únicamente hasta la mitad. Esto se debe a que, en un palíndromo, los caracteres deben coincidir en simetría: el primero con el último, el segundo con el penúltimo, y así sucesivamente. Al reducir la cantidad de comparaciones a la mitad de la longitud de la palabra, se optimiza el proceso. Además, para asegurar que la comparación no dependa de mayúsculas o espacios, copilot me recomendo que transforme la palabra a minúsculas y elimine los espacios antes de realizar las comparaciones. Si en alguna comparación los caracteres no coincidian, la función retorna inmediatamente `False`, haciendo que el proceso sea más rápido. 

![image](https://github.com/user-attachments/assets/51ba9d06-c955-4217-ba1c-1d93e17f1750)


3. algoritmo para operaciones básicas: Para que el algoritmo pudiera realizar las operaciones básicas (suma, resta, multiplicación y división), primero tuve que declararlas. Luego se le pidió al usuario que digitara los dos números con los que quería trabajar e inmediatamente después se le mostraba un menú de operaciones, en el que se denotaban las convenciones con las cuales podría acceder a una de las operaciones.

4. Algortitmo que devuelve números primos: Para llegar a la solución del problema, comencé por entender que el objetivo era encontrar todos los números primos en la lista de numeros proporcionada por el usuario. Sabía que un número primo es aquel que solo tiene dos divisores: 1 y él mismo. Por lo tanto, la primera tarea fue crear una función que verificara si un número dado es primo. Para hacer esto de manera eficiente, utilicé el hecho de que no es necesario verificar todos los números hasta el número mismo, sino hasta su raíz cuadrada. Luego, creé otra función que recorría todos los números de la lista ingresada por el usuario y utilizaba la función anterior para verificar si cada número era primo. Finalmente, el programa mostraba todos los números primos encontrados.

5. algoritmo para definir anagramas: Para resolver el problema de verificar si dos palabras son anagramas, comencé por identificar que dos palabras son anagramas si tienen las mismas letras en la misma cantidad, sin importar el orden. Para lograrlo, por recomendación de copilot primero eliminé los espacios y convertí las letras a minúsculas, para hacer la comparación más flexible. Luego, utilicé la función `sorted()` para ordenar las letras de ambas palabras y comparé si las listas resultantes eran iguales. Si las listas ordenadas eran idénticas, entonces las palabras ingresadas son anagramas.

6. algoritmo para mayor suma de consecutivos: Para resolver el problema de encontrar la mayor suma de dos números consecutivos en una lista proporcionada por el usuario, comencé pidiendo al usuario que ingresara una lista de números. Luego, utilicé un bucle para recorrer la lista y sumé cada par de números consecutivos. Mientras recorría la lista, mantuve un registro de la mayor suma encontrada hasta ese momento. Para ello, comparé la suma de los dos números consecutivos con la suma máxima almacenada y actualicé el valor si encontraba una suma mayor. Finalmente, el resultado es la mayor suma de dos números consecutivos en la lista proporcionada.

    


