import pygame

#pygame setup
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1270, 720))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

game_over = False
while not game_over:

    #이벤트 (창의 모든 이벤트를 핸들링하다가 quit가 되면 game_over 변수 값 바꿈)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #화면(display), screen(화면에 그릴 정보를 갖고 있는 변수)
    screen.fill('red')

    pygame.draw.circle(screen, "white", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 10
    if keys[pygame.K_DOWN]:
        player_pos.y += 10
    if keys[pygame.K_LEFT]:
        player_pos.y -= 10
    if keys[pygame.K_RIGHT]:
        player_pos.y += 10
        
    pygame.display.flip()

    clock.tick(60) #tick = frequency per second -> 60 
