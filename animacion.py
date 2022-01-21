import pygame , sys, time
from pygame.locals import *

#Configurar pygame.
pygame.init()

#Configurar la Ventana.
superficieventana = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Animacion")

#Establece la Ventana
AnchoVentana = 500
AltoVentana = 500
superficieventana = pygame.display.set_mode((AnchoVentana,AltoVentana),0,32)

#Establecer variables de direcciones
AbajoIzquierda = 1
AbajoDerecha = 3
ArribaIzquierda= 7
ArribaDerecha = 9

VelocidadMovimiento = 4

#establecer los Colores
Negro= (0,0,0)
Rojo = (255,0,0)
Verde= (0,255,0)
Azul = (0,0,255)

#Establece los datos de los Bloques.
b1={'rect':pygame.Rect(300,80,50,100),'color':Rojo,'dir':ArribaDerecha}
b2={'rect':pygame.Rect(200,200,20,20),'color':Verde,'dir':ArribaIzquierda}
b3={'rect':pygame.Rect(300,80,50,100),'color':Azul,'dir':AbajoIzquierda}
bloques = [b1,b2,b3]

#Corre el Ciclo de Juego.
while True:
	#Busca el Evento quit para que salga el programa.
	for event in pygame.event.get():
		if event.type == 'QUIT':
			pygame.quit()
			sys.exit()
			
	#Dibuja el Fondo Negro sobre la superficie
	superficieventana.fill(Negro)
	
	for b in bloques:
		#mueva la estructura de datos de bloques
		if b['dir'] == AbajoIzquierda:
			b['rect'].left -= VelocidadMovimiento
			b['rect'].top += VelocidadMovimiento
		if b['dir'] == AbajoDerecha:
			b['rect'].left += VelocidadMovimiento
			b['rect'].top += VelocidadMovimiento
		if b['dir'] == ArribaIzquierda:
			b['rect'].left -= VelocidadMovimiento
			b['rect'].top -= VelocidadMovimiento
		if b['dir'] == ArribaDerecha:
			b['rect'].left += VelocidadMovimiento
			b['rect'].top -= VelocidadMovimiento
		#Verifica si el Bloque se movio fuera de la ventana.
		if b['rect'].top < 0:
			#El Bloque se Movio por debajo de la ventana.
			if b['dir'] == ArribaIzquierda:
				b['dir'] = AbajoIzquierda
			if b['dir'] == ArribaDerecha:
				b['dir'] = AbajoDerecha
		if b['rect'].left < 0:
			#El Bloque se Movio por la Izquierda de la Ventana.
			if b ['dir'] == AbajoIzquierda:
				b ['dir'] = AbajoDerecha
			if b['dir'] == ArribaIzquierda:
				b['dir'] = ArribaDerecha
		
		if b['rect'].bottom > AltoVentana:
			#el bloque se movio por debajo de la ventana.
			if b['dir'] == AbajoIzquierda:
				b['dir'] = ArribaIzquierda
			if b['dir'] == AbajoDerecha:
				b['dir'] = ArribaDerecha		
		if b['rect'].left < 0:
			#El Bloque se Movio por la Izquierda de la Ventana.
			if b ['dir'] == AbajoIzquierda:
				b ['dir'] = AbajoDerecha	
			if b['dir'] == ArribaIzquierda:
				b['dir'] = ArribaDerecha
				
		if b['rect'].right > AnchoVentana:
			#El Bloque se Movio por el Ancho de la Ventana.
			if b['dir'] == AbajoDerecha:
				b['dir'] = AbajoIzquierda
			if b['dir'] == ArribaDerecha:
				b['dir'] = ArribaIzquierda
				
		#Dibuja el bloque en la superficie
		pygame.draw.rect(superficieventana,b['color'],b['rect'])
	
	#Dibuja la Ventana en la pantalla
	pygame.display.update()
	time.sleep(0.02)
