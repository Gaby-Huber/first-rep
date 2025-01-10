import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Verde")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Reloj para controlar los FPS
clock = pygame.time.Clock()
FPS = 60

# Estado del juego
blur_level = 0  # Nivel de desenfoque de la "cámara"
ping_pong_balls = []
score = 0

def pixelate_surface(surface, pixel_size):
    """Aplica un efecto de pixelación a la superficie."""
    if pixel_size <= 1:
        return surface
    small = pygame.transform.scale(surface, (WIDTH // pixel_size, HEIGHT // pixel_size))
    return pygame.transform.scale(small, (WIDTH, HEIGHT))

# Clase para las pelotas de ping pong
class PingPongBall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, -2)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx = -self.vx
        if self.y - self.radius < 0:
            self.vy = -self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

# Clase para los vasos
class Cup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# Crear vasos
cups = [Cup(100 + i * 100, HEIGHT - 100) for i in range(5)]

# Funciones del juego
def make_and_smoke():
    """Simula hacer y fumar cigarrillos verdes."""
    print("Estás haciendo y fumando un cigarrillo verde...")

def drink_juice():
    """Simula beber un vaso de jugo."""
    global blur_level
    print("Tomaste un vaso de jugo...")
    blur_level += 2  # Incrementa el nivel de desenfoque

def throw_ball():
    """Lanza una pelota de ping pong."""
    print("Lanzaste una pelota de ping pong...")
    ping_pong_balls.append(PingPongBall(WIDTH // 2, HEIGHT - 50))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # Hacer y fumar
                make_and_smoke()
            elif event.key == pygame.K_d:  # Beber jugo
                drink_juice()
            elif event.key == pygame.K_t:  # Lanzar pelota
                throw_ball()

    # Actualizar
    for ball in ping_pong_balls:
        ball.update()

    # Detección de colisiones
    for ball in ping_pong_balls:
        for cup in cups:
            if cup.x < ball.x < cup.x + cup.width and cup.y < ball.y < cup.y + cup.height:
                cups.remove(cup)
                ping_pong_balls.remove(ball)
                score += 1
                break

    # Dibujar
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill(BLACK)

    # Dibujar elementos del juego
    for cup in cups:
        cup.draw(surface)
    for ball in ping_pong_balls:
        ball.draw(surface)

    # Aplicar pixelación
    surface = pixelate_surface(surface, blur_level)

    # Mostrar en pantalla
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    # Controlar FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()