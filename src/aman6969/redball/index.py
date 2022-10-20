import pygame, random
pygame.init()

# To initialized the sound
pygame.mixer.init()
pygame.mixer.music.load('redballsong.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()


def paddle_animation():
    paddle1.top = paddle1.top - paddle_speed
    paddle2.top = paddle2.top - paddle_speed
    paddle3.top = paddle3.top - paddle_speed
    paddle4.top = paddle4.top - paddle_speed

    # for rendering the new paddle when it reaches the top
    if paddle1.top <= 0:
        paddle1.center = (random.randint(70, width - 140), 550)
    if paddle2.top <= 0:
        paddle2.center = (random.randint(70, width - 140), 550)
    if paddle3.top <= 0:
        paddle3.center = (random.randint(70, width - 140), 550)
    if paddle4.top <= 0:
        paddle4.center = (random.randint(70, width - 140), 550)



def ball_animation():
    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    if ball.right >= width:
        ball.right = width
    if ball.left <= 0:
        ball.left = 0

    # Collision between ball and paddle
    if ball.colliderect(paddle1) and ball_speed_y > 0:
        if abs(ball.bottom - paddle1.top) < 10:
            ball.bottom = paddle1.top

    if ball.colliderect(paddle2) and ball_speed_y > 0:
        if abs(ball.bottom - paddle2.top) < 10:
            ball.bottom = paddle2.top

    if ball.colliderect(paddle3) and ball_speed_y > 0:
        if abs(ball.bottom - paddle3.top) < 10:
            ball.bottom = paddle3.top

    if ball.colliderect(paddle4) and ball_speed_y > 0:
        if abs(ball.bottom - paddle4.top) < 10:
            ball.bottom = paddle4.top


def screen_drawing():
    '''Rendering all the useful stuffs'''

    pygame.draw.rect(screen, BLUE, paddle1)
    pygame.draw.rect(screen, BLUE, paddle2)
    pygame.draw.rect(screen, BLUE, paddle3)
    pygame.draw.rect(screen, BLUE, paddle4)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.rect(screen, WHITE, border)
    score_img = font.render(str(score), True, WHITE)
    screen.blit(score_img, (10, 560))
    pygame.draw.rect(screen, BACKGROUND, spike)
    # polygon function creates a triangle when 3 points is given
    pygame.draw.polygon(screen, RED, [(0, 0), (25, spike_y), (50, 0)])
    pygame.draw.polygon(screen, RED, [(50, 0), (75, spike_y), (100, 0)])
    pygame.draw.polygon(screen, RED, [(100, 0), (125, spike_y), (150, 0)])
    pygame.draw.polygon(screen, RED, [(150, 0), (175, spike_y), (200, 0)])
    pygame.draw.polygon(screen, RED, [(200, 0), (225, spike_y), (250, 0)])
    pygame.draw.polygon(screen, RED, [(250, 0), (275, spike_y), (300, 0)])
    pygame.draw.polygon(screen, RED, [(300, 0), (325, spike_y), (350, 0)])
    pygame.draw.polygon(screen, RED, [(350, 0), (375, spike_y), (400, 0)])
    pygame.draw.polygon(screen, RED, [(400, 0), (425, spike_y), (450, 0)])
    pygame.draw.polygon(screen, RED, [(450, 0), (475, spike_y), (500, 0)])
    pygame.draw.polygon(screen, RED, [(500, 0), (525, spike_y), (550, 0)])
    pygame.draw.polygon(screen, RED, [(550, 0), (575, spike_y), (600, 0)])


# Game specific variables
width = 600
height = 600
FPS = 60
exit_game = False
game_over = False

# Color
WHITE = (255, 255, 255)
RED = 'firebrick2'
BLUE = 'dodgerblue4'
BACKGROUND = 'dodgerblue2'

# Paddle1
paddle1_x = 100
paddle1_y = 100
paddle_width = 100
paddle_height = 10
paddle_speed = 2

# Paddle2
paddle2_x = 400
paddle2_y = 300

# Paddle3
paddle3_x = 100
paddle3_y = 400

# Paddle4
paddle4_x = 400
paddle4_y = 500

# Ball
ball_x = 400
ball_y = 300
ball_width = 40
ball_height = 40
ball_speed_x = 0
ball_speed_y = 3

# Bottom border
border_x = 0
border_y = 550
border_width = width
border_height = 1

# Spikes
spike_x = 0
spike_y = 50
spike_width = width
spike_height = 1

# Score
score = 0
font = pygame.font.SysFont('Arial', 26)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Red Ball Game')

paddle1 = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)
paddle2 = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)
paddle3 = pygame.Rect(paddle3_x, paddle3_y, paddle_width, paddle_height)
paddle4 = pygame.Rect(paddle4_x, paddle4_y, paddle_width, paddle_height)
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
border = pygame.Rect(border_x, border_y, border_width, border_height)
spike = pygame.Rect(spike_x, spike_y, spike_width, spike_height)

with open('RedballScore.txt', 'r') as f:
    highscore = f.read()


def gameloop():
    global exit_game, game_over, score, highscore, ball_speed_x, paddle_speed

    while not exit_game:

        if game_over:
            if score > int(highscore):
                highscore = score

            # overrides the new highscore
            with open('RedballScore.txt','w') as f:
                f.write(str(highscore))

            screen.fill(BACKGROUND)
            score_img = font.render('Score: ' + str(score), True, WHITE)
            screen.blit(score_img, (width//2-40, height//2-40))
            high_score_img = font.render('High Score: ' + str(highscore), True, WHITE)
            screen.blit(high_score_img, (width // 2-70, height // 2+10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:

                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ball_speed_x = ball_speed_x + 4
                    if event.key == pygame.K_LEFT:
                        ball_speed_x = ball_speed_x - 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        ball_speed_x = ball_speed_x - 4
                    if event.key == pygame.K_LEFT:
                        ball_speed_x = ball_speed_x + 4

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        ball_speed_x = ball_speed_x + 4
                    if event.key == pygame.K_a:
                        ball_speed_x = ball_speed_x - 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        ball_speed_x = ball_speed_x - 4
                    if event.key == pygame.K_a:
                        ball_speed_x = ball_speed_x + 4

            paddle_animation()
            ball_animation()

            score = score + 1
            if ball.colliderect(border) and ball_speed_y > 0:
                if abs(ball.bottom - border.top) < 10:
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
                    game_over = True

            # increasing the ball speed
            if score > 1500:
                paddle_speed = 3
            if score > 3000:
                paddle_speed = 4
            if score > 4500:
                paddle_speed = 5

            if ball.colliderect(spike) and ball_speed_y > 0:
                if abs(ball.top - spike.bottom) < 10:
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
                    game_over = True

            screen.fill(BACKGROUND)
            screen_drawing()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

gameloop()