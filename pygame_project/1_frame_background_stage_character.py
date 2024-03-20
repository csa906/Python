import pygame
import os

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()
fps = 60

# 1. 사용자 게임 초기화
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 폴더 주소 가져오기
dir = os.getcwd()

# 배경 이미지 불러오기

# 캐릭터(스프라이트) 불러오기

# 이동할 좌표

# 적 캐릭터

# 폰트 정의 
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(fps) # 프레임 수 설정
    print("fps : {0}".format(clock.get_fps()))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # 창 닫히는 이벤트
            running = False


    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))

    pygame.display.update()


# pygame 종료
pygame.quit()