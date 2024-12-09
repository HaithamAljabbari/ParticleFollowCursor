import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Animation Following Cursor")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 2)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.life = random.randint(30, 50)  
        self.speed = random.uniform(2, 4) 
    
        self.angle = random.uniform(0, 2 * math.e)

    def move(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance != 0:
            dx, dy = dx / distance, dy / distance 

       
        self.x += dx * self.speed
        self.y += dy * self.speed
        
        self.life -= 1
        
    def draw(self, surface):
        if self.life > 0:
 
def main():
    particles = []  
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill(BLACK)
        
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        

        for _ in range(10): 
            particles.append(Particle(mouse_x, mouse_y))
        
        for particle in particles[:]:
            particle.move(mouse_x, mouse_y)
            particle.draw(screen)
            
            if particle.life <= 0:
                particles.remove(particle)
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

