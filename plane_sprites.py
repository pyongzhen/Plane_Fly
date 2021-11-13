'''
pygame.sprite.Sprite
package.module.class
if not extends object :
		override superclass __init__()
		ensure superclass implements __init__() code canexcute successfully
		Game Sprite
		------------
		image --> get_rect()
		rect
		speed
		import module 
		1.local
		2. three field
		3. self module
		'''
import random
import pygame 
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_FLUSH_RATE = 60
# create enemy event

CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_BOTTOM_POSITION = 100

HERO_FIRE_EVENT = pygame.USEREVENT + 1;
class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_name,speed=1):
# apply the superclass measures
							super().__init__()

# define object properties
							self.image = pygame.image.load(image_name) 
							self.rect = self.image.get_rect() 
							self.speed = speed 
	def update(self):
				self.rect.y += self.speed


class Background(GameSprite):
	def __init__(self,is_alt=False):
	
		super().__init__("./images/background.png")
		if is_alt:
				self.rect.y = -self.rect.height

	def update(self):
#visit superclass method
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
					self.rect.y = -self.rect.height
		'''
		create the atmosphere rollbacking the screen which usually use some running game to implement the special circumstance
		'''

class Enemy(GameSprite):
# initialised enemy sprites
				def __init__(self):
# create enemy sprites
						super().__init__("./images/enemy1.png")
# ensure the primary random speed 1-3
						self.speed = random.randint(1,3)
# ensure the primary random position
						self.rect.bottom = 0 # equals - self.rect.height
						max_x = SCREEN_RECT.width - self.rect.width

						self.rect.x = random.randint(0,max_x)

				def update(self):

# visit superclass
					super().update()

	# if fly screen kill enemy sprites 
					if self.rect.y >= SCREEN_RECT.height: 
	#print("enemy fly out which will fall")
 						self.kill() 
				def __del__(self):
					pass 
#print("kill %s" % self.rect) 


class Hero(GameSprite): 
	def __init__(self):
#images & speed
		super().__init__("./images/me1.png",0)
#centerx centery
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - HERO_BOTTOM_POSITION
# initialised the position
		self.bullets = pygame.sprite.Group()
	def update(self):
# not extends superclass only vertical running
				self.rect.x += self.speed
# control the position border
				if self.rect.x < 0:     #left
						self.rect.x = 0
				elif self.rect.right > SCREEN_RECT.right:
						self.rect.right = SCREEN_RECT.right

						pass
	def fire(self):
			for i in (0,1,2):
				bullet = Bullet()
				bullet.rect.bottom = self.rect.y - i*20
				bullet.rect.centerx = self.rect.centerx # remain bullet up the hero
				self.bullets.add(bullet)

class Bullet(GameSprite):
	def __init__(self):
			super().__init__("./images/bullet2.png",-2) 
# speed negative from vertical
	def update(self):
			super().update()
			
			if self.rect.bottom < 0:
								self.kill()
	def __del__(self):
				pass
			#print("Free")
