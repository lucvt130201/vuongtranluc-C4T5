import pygame

#1 initallize
pygame.init()
pygame.display.set_caption("Pong game")

#2 set up game window

SIZE = (600, 600)
BG_COLOR = (70, 96, 70)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")  #load ảnh
ball_image = pygame.image.load("assets/ball.png")    #load ảnh

#tọa độ paddle 1
x1 = 0
y1 = 100

#tọa độ paddle 2
x2 = 570
y2 = 250

# x3 = 300
# y3 = 0

ball_x = 300
ball_y = 0
ball_v_x = 2
ball_v_y = 0

w_pressed = False
s_pressed = False

i_pressed = False
k_pressed = False

# UP_pressed = False
# DOWN_pressed = False
loop = True



while loop:

    # pooling: kĩ thuật check event
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT: # sau chấm nhớ viết hoa
            loop =  False
        elif e.type == pygame.KEYDOWN:   #hành động người dùng nhấn phím

            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True

            elif e.key == pygame.K_i:
                i_pressed = True
            elif e.key == pygame.K_k:
                k_pressed = True

            # elif e.key == pygame.K_u:
            #     UP_pressed = True
            # elif e.key == pygame.K_j:
            #     DOWN_pressed = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False

            elif e.key == pygame.K_i:
                i_pressed = False
            elif e.key == pygame.K_k:
                k_pressed = False

            # elif e.key == pygame.K_u:
            #     UP_pressed = False
            # elif e.key == pygame.K_j:
            #     DOWN_pressed = False

    if w_pressed:
        y1 -= 5
    elif s_pressed:
        y1 += 5

    elif i_pressed:
        y2 -= 5
    elif k_pressed:
        y2 += 5

    # elif UP_pressed:
    #     y3 -= 5
    # elif DOWN_pressed:
    #     y3 += 5
    ball_x += ball_v_x
    ball_y += ball_v_y
    if ball_x >= 570 or ball_x <= 0:
        ball_v_x = - ball_v_x


    canvas.fill(BG_COLOR)    # đổ màu
    canvas.blit(paddle_image, (x1, y1))     # vẽ ảnh
    canvas.blit(paddle_image, (x2, y2))
    canvas.blit(ball_image, (ball_x, ball_y))
    clock.tick(60)
    pygame.display.flip()

    #1  x += 2 ; y += 0
    #2  x += -2; y += 0
    #3  y += 2
    #4  y += -2
    #5  x += -2; y += -2
    #6  x += 2; y += 2
    #7  x +=2; y += -2
    #8  x +=-2; y +=2

