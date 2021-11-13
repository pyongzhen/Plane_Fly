import pygame as py
from plane_sprites import *

class PlaneGame(object):
		def __init__(self):
			print("Init Pygame")
			self.screen = py.display.set_mode(SCREEN_RECT.size)

			self.clock = py.time.Clock()

			self.__create_sprites()

			py.init()

			py.time.set_timer(CREATE_ENEMY_EVENT,1000)  # one sec
			py.time.set_timer(HERO_FIRE_EVENT,500) 		# one point five sec


		def __create_sprites(self):

			bg1 = Background()
			bg2 = Background(True)
# bg2.rect.y = -bg2.rect.height
			self.back_group = py.sprite.Group(bg1,bg2)
			self.enemy_group = py.sprite.Group()

			self.hero = Hero()
			self.hero_group = py.sprite.Group(self.hero)

		def start_game(self):

			print("Beginning of game")
			while True:

				self.clock.tick(FRAME_FLUSH_RATE)
				self.__event_handler()
				self.__check_collide()
				self.__update_sprites()
				py.display.update()

		def __event_handler(self):
				for event in py.event.get():

						if event.type == py.QUIT:
							PlaneGame.__game_over()
						elif event.type == CREATE_ENEMY_EVENT:
# print("Enemy exits")
# create enemy sprite
							enemy = Enemy()
							self.enemy_group.add(enemy)
#1.event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT 
# but this method seem keyup and keydown as a event touch
#2.pygame.key.get_pressed() --> all event Tuple
# Through const parameter judge the keydown if or not.
# elif event.type == py.KEYDOWN and event.key == py.K_RIGHT:
# print("Right")		
						elif event.type == HERO_FIRE_EVENT:
								self.hero.fire()
				keys_pressed = py.key.get_pressed()
				if keys_pressed[py.K_RIGHT]:    # keep listener 
							self.hero.speed = 2
				elif keys_pressed[py.K_LEFT]:
							self.hero.speed = -2
				else:
					self.hero.speed = 0

# keyup --> end 
# keydown -->  begin

		def __check_collide(self):
							py.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
							enemies = py.sprite.spritecollide(self.hero,self.enemy_group,True)
							if len(enemies) > 0:
									self.hero.kill()
									PlaneGame.__game_over()
		def __update_sprites(self):
				self.back_group.update()
				self.back_group.draw(self.screen)

				self.enemy_group.update()
				self.enemy_group.draw(self.screen)

				self.hero_group.update()
				self.hero_group.draw(self.screen)
				
				self.hero.bullets.update()
				self.hero.bullets.draw(self.screen)

		@staticmethod
		def __game_over():
			print("Game Over")
			py.quit()
			exit()

		''' 
		settimer(eventid,millisecs) --> None
		event.get 
		'''
if __name__ == '__main__':

		game = PlaneGame()
		game.start_game()

