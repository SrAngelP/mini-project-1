<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# ¡Simulador Pokemon!

## Content
- [Descripción del juego](#Descripción-del-juego)
- [Mecánica del juego](#Mecánica-del-juego)
- [Estadísticas](#Estadísticas)
- [Ataques](#Ataques)
- [Mejoras futuras](#Mejoras-futuras)
- [Links](#Links)

## Descripción del juego

El juego fusiona dos formas de juego. La clásica rutina de batalla de las versionas para *gameboy*/*gameboy advance*/*etc* y la aleatoriedad de los juegos *gatcha*. En concreto el usuario puede elegir si jugar solo (contra la maquina) o contra un compañero (*PvP*). Se efectua la batalla y el ganador aparece en la pantalla.



## Mecánica del juego

Entrando en el juego el usuario selecciona el tipo de modalidad, posteriormente se le asignará un pokemon aleatorio de los que contiene el juego (por el momento 3) con estadísticas aleatorias según el rango máximo que puede alcanzar, se le enseña al usuario dichas estadísticas que puede analizar, ya que estas serán importantes después. Al iniciar la batalla el pokemon con la velocidad más elevada es el que ataca primero. Durante la lucha el usuario tiene la oportunidad de elegir uno de los dos ataques predeterminados. Ambos luchadores siguen atacando hasta que los *Hit Point* (HP) del oponente queden en 0 lo que dará por terminada la batalla y definirá al ganador.


### Estadísticas

Las estadísticas (*Stats*) de los pokemon están basados en las oficiales según los juegos. **NO SON LAS ESTADÍSTICAS BASE (***BASE STATS***)** . Las estadísticas son las tomadas del ragno que puede tener un pokemon cuando se encuentra en el nivel 100, se decidió de esta manera para que no hubiera una diferencia tan abismal entre los competidores.

### Ataques

Los ataques fueron elegidos con la idea de que cada pokemon tenga un ataque *físico* y uno tipo *especial* por lo que el usuario tendrá que poner atención cuál ataque le conviene más según las características de su pokemon (*ataque especial* y *ataque*). De la misma manera deberá estar atento a qué ataques le hacen más daño según sus niveles de defensa.

El daño que produce cada ataque está calculado según una forma simplificada de la fórmula del daño en la primera generación. La ecuación original es la siguiente:


<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Blank_image.jpg" width="1000" height="1000" class="under" />
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4445736b8e1e8be597cf7901e4ad0be60b54d1ab" alt="1000" width="1000" class="over" />

De la ecuación anterior no se tomaron em cuenta los *boosters* de *type 1*, *typ2*, *STAB* y *random* así que se igualaron a uno, y el nivel se asumió como el 100 (el máximo en la primera generación). Esto se calculo teniendo en cuenta que *A* y *D* son el ataque y defensa de los correspondientes pokemons y *power* es el poder de cada ataque individual.


## Mejoras futuras

Durante la programación del juego se encontró con la dificultad de la creación de cada pokemon individual (hecho con objetos de python) pero en el proceso se descrubrió una manera de usar las bases de datos ya existentes para poder ampliar el catálogo de pokemones y ataques. Se espera que en un futuro se implementen dichos cambios.
Del mismo modo se especúla una mejora en la dificultad de la computadora la cual hasta el momento elegía los ataques al azar, aumentando así el nivel de dificultad. 
Ya por último se baraja la idea de aumentar la cantidad de datos de cada pokemon, como la mejora de la interfaz gráfica para que sea más a interactica con el usuario.



## Links

https://pokemondb.net/

https://bulbapedia.bulbagarden.net/wiki/Damage
