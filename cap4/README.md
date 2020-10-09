# Capacitación 4: Visión 3D

Durante la capacitación 4 se mostraron los conceptos de geometría tanto en 2D como en 3D que se utilizan en la robótica móvil y visión computacional.

La misión para esta capacitación es programar un freno de emergencia que evite los accidentes en Duckietown. Para esto, deben utilizar el trabajo realizado anteriormente de detectar a los patitos y aplicar la aproximación vista en la capacitación que permite estimar la distancia entre el Duckiebot y los patos. Se agrega el archivo `emergency_stop.py`, el cual posee la estructura principal y funciones de utilidad con sus respectivos comentarios que servirán para poder completar la misión.

## Funciones útiles
Estas funciones serán de utilidad para resolver el desafío:

`dets = det_duckie(obs)`: Permite hacer la detección de los patos (deben agregar su detector). Lo importante es que en este caso deben retornar una lista de detecciones!

`obs = draw_dets(obs, dets)`: Esta función recibe la imagen `obs` en la cual dibuja las detecciones enlistadas en `dets`.

`img_out = red_alert(img_in)`: Agrega dramatismo al simulador.

## Mapa para calibración
Además, se adjunta mapa (archivo `free.yaml`) que debe copiarse en la carpeta de mapas de `gym-duckietown`. Este mapa contiene un pato de tamaño conocido (0.08 [m]) en el centro del mapa, cada _tile_ mide 1 [m] y se pueden mover libremente por todo el espacio.

El código se corre de la siguiente forma:

`python emergency_stop.py --map-name free`
