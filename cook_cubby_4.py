#material 수정

import pygame
import random
import time

#화면 기본 설정
pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("요리왕 커비")
#game_font = pygame.font.Font(None, 40)
game_font = pygame.font.SysFont("arial", 30, True, True)

background = pygame.image.load(r"C:\Python\project\\background_2.jpg")
#background_scale = pygame.transform.scale(background, (1920, 1080))
#pygame.image.save(background, 'background.png')
#background = pygame.image.load(r"C:\Python\project\\background.png")
#background_scale = pygame.transform.scale(background, (5000, 5000))

#캐릭터 설정
character = pygame.image.load(r"C:\Python\project\cubby_1_(1_1).png")
character_scale = pygame.transform.scale(character, (100, 100))
pygame.image.save(character_scale, 'cubby_1_(3).png')
character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = 800
character_speed = 0.3   #캐릭터의 속도
character_x = 0         #캐릭터가 이동할 x좌표
character_eat_count = 0

eat = pygame.image.load(r"C:\Python\project\cubby_2.png")
eat_scale = pygame.transform.scale(eat, (100, 100))
pygame.image.save(eat_scale, 'cubby_2_(1).png')
eat_sound = pygame.mixer.Sound("C:\Python\project\pop_cat.mp3")

# 낙하물 설정


    
tteok = pygame.image.load(r'C:\Python\project\\tteok.png')
tteok_scale = pygame.transform.scale(tteok, (100, 100))
pygame.image.save(tteok_scale, 'tteok_(1).png')
tteok = pygame.image.load(r'C:\Python\project\\tteok_(1).png')
tteok_size = tteok.get_rect().size
tteok_width = tteok_size[0]
tteok_height = tteok_size[1]
tteok_x_pos = random.randint(150, 1650)
tteok_y_pos = 0
tteok_speed = 20
tteok_time=0
tteok_able=True
tteok_material = 0
tteok_count = 0

green_onion = pygame.image.load(r'C:\Python\project\green_onion.png')
green_onion_scale = pygame.transform.scale(green_onion, (100, 100))
pygame.image.save(green_onion_scale, 'green_onion(1).png')
green_onion = pygame.image.load(r'C:\Python\project\green_onion(1).png')
green_onion_size = green_onion.get_rect().size
green_onion_width = green_onion_size[0]
green_onion_height = green_onion_size[1]
green_onion_x_pos = random.randint(150, 1650)
green_onion_y_pos = 0
green_onion_speed = 20
green_onion_time=0
green_onion_able=True
green_onion_material = 0
green_onion_count = 0

fish_cake = pygame.image.load(r'C:\Python\project\fish_cake.png')
fish_cake_scale = pygame.transform.scale(fish_cake, (100, 100))
pygame.image.save(fish_cake_scale, 'fish_cake(1).png')
fish_cake = pygame.image.load(r'C:\Python\project\fish_cake(1).png')
fish_cake_size = fish_cake.get_rect().size
fish_cake_width = fish_cake_size[0]
fish_cake_height = fish_cake_size[1]
fish_cake_x_pos = random.randint(150, 1650)
fish_cake_y_pos = 0
fish_cake_speed = 20
fish_cake_time=0
fish_cake_able=True
fish_cake_material = 0
fish_cake_count = 0

red_pepper_paste = pygame.image.load(r'C:\Python\project\red_pepper_paste.png')
red_pepper_paste_scale = pygame.transform.scale(red_pepper_paste, (100, 100))
pygame.image.save(red_pepper_paste_scale, 'red_pepper_paste(1).png')
red_pepper_paste = pygame.image.load(r'C:\Python\project\red_pepper_paste(1).png')
red_pepper_paste_size = red_pepper_paste.get_rect().size
red_pepper_paste_width = red_pepper_paste_size[0]
red_pepper_paste_height = red_pepper_paste_size[1]
red_pepper_paste_x_pos = random.randint(150, 1650)
red_pepper_paste_y_pos = 0
red_pepper_paste_speed = 20
red_pepper_paste_time=0
red_pepper_paste_able=True
red_pepper_paste_material = 0
red_pepper_paste_count = 0

trash = pygame.image.load(r'C:\Python\project\\trash.png')
trash_scale = pygame.transform.scale(trash, (100, 100))
pygame.image.save(trash_scale, 'trash_(1).png')
trash = pygame.image.load(r'C:\Python\project\\trash_(1).png')
trash_size = trash.get_rect().size
trash_width = trash_size[0]
trash_height = trash_size[1]
trash_x_pos = random.randint(150, 1650)
trash_y_pos = 0
trash_speed = 20
trash_time=0
trash_able=True
trash_material = " "
trash_count = 0
trash_cnt = 0



#time 부분
clock = pygame.time.Clock()
total_time = 100  #제한시간
start_time = pygame.time.get_ticks()
complete_able = 0
complete_count = 0
complete_time = 0
sick = True

#gauge 부분
gauge = pygame.image.load("C:\Python\project\gauge.png")
gauge_x_pos = 1650
gauge_y_pos = 100
score = 0   #점수 저장 변수
gauge_able = True
gauge_time = 0 
gauge_count = 0

def change_eat_size():
    character = pygame.image.load(r"C:\Python\project\cubby_1_(1_1).png")
    character_scale = pygame.transform.scale(character, (100+character_eat_count, 100+character_eat_count))
    pygame.image.save(character_scale, 'cubby_1_(3).png')
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
        
    character = pygame.image.load(r"C:\Python\project\cubby_2.png")
    character_scale = pygame.transform.scale(character, (100+character_eat_count, 100+character_eat_count))
    pygame.image.save(character_scale, 'cubby_2_(1).png')
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]


    


running = True

#게임시작
while running:
    dt = clock.tick(30)

    #이벤트 발생동안
    for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           time.sleep(10)
           running = False
   
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               character_x -= character_speed
           elif event.key == pygame.K_RIGHT:
               character_x += character_speed
    
               
    #플레이어 화면밖에 있다면
    if character_x_pos < 150:
        character_x_pos = 150
    elif character_x_pos > 1650:
        character_x_pos = 1650
     
    #캐릭터의 위치
    character_x_pos += character_x * dt
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    #떡 
    tteok_y_pos += tteok_speed
    
    #떡이 화면밖에 있다면
    if tteok_y_pos > screen_height:
        tteok_y_pos = 0
        tteok_x_pos = random.randint(150, 1650)

    #충돌 처리
    tteok_rect = tteok.get_rect()
    tteok_rect.left = tteok_x_pos
    tteok_rect.top = tteok_y_pos

    if sick and tteok_able and character_rect.colliderect(tteok_rect):   
        score +=5
        character_eat_count +=5
        #item_text = game_font.render("tteok", True, (255, 0, 0))
        #screen.blit(item_text, (1600, 200))
        tteok_time = time.time()
        eat_sound.play()
        change_eat_size()
        tteok_y_pos = 0
        tteok_x_pos = random.randint(150, 1650)
  #      if gauge_able == True:
   #         gauge_x_pos -= 100
   
    #타이머
    if (time.time() - tteok_time) < 0.5:
        tteok_able = False
        character = pygame.image.load(r"C:\Python\project\cubby_2_(1).png")
        tteok_material = 1
        tteok_count = 1
    else:
        tteok_able = True
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
      
        
      
        
        
    #파
    green_onion_y_pos += green_onion_speed
    #파가 화면밖에 있다면
    if green_onion_y_pos > screen_height:
        green_onion_y_pos = 0
        green_onion_x_pos = random.randint(150, 1650)
    
    green_onion_rect = green_onion.get_rect()
    green_onion_rect.left = green_onion_x_pos
    green_onion_rect.top = green_onion_y_pos
    
    if sick and green_onion_able and character_rect.colliderect(green_onion_rect):   
        score +=5
        character_eat_count +=5
        #item_text = game_font.render("tteok", True, (255, 0, 0))
        #screen.blit(item_text, (1600, 200))
        green_onion_time = time.time()
        eat_sound.play()
        change_eat_size()
        green_onion_y_pos = 0
        green_onion_x_pos = random.randint(150, 1650)
     #   if gauge_able == True:
      #      gauge_x_pos -= 100
        
    #타이머
    if (time.time() - green_onion_time) < 0.5:
        green_onion_able = False
        character = pygame.image.load(r"C:\Python\project\cubby_2_(1).png")
        green_onion_material = 1
        green_onion_count = 1
    else:
        green_onion_able = True
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
            
    
    #어묵
    fish_cake_y_pos += fish_cake_speed
    #어묵이 화면밖에 있다면
    if fish_cake_y_pos > screen_height:
        fish_cake_y_pos = 0
        fish_cake_x_pos = random.randint(150, 1650)
    
    fish_cake_rect = fish_cake.get_rect()
    fish_cake_rect.left = fish_cake_x_pos
    fish_cake_rect.top = fish_cake_y_pos
    
    if sick and fish_cake_able and character_rect.colliderect(fish_cake_rect):   
        score +=5
        character_eat_count +=5
        #item_text = game_font.render("tteok", True, (255, 0, 0))
        #screen.blit(item_text, (1600, 200))
        fish_cake_time = time.time()
        eat_sound.play()
        change_eat_size()
        fish_cake_y_pos = 0
        fish_cake_x_pos = random.randint(150, 1650)
      #  if gauge_able == True:
       #     gauge_x_pos -= 100
        
    #타이머
    if (time.time() - fish_cake_time) < 0.5:
        fish_cake_able = False
        character = pygame.image.load(r"C:\Python\project\cubby_2_(1).png")
        fish_cake_material = 1
        fish_cake_count = 1
    else:
        fish_cake_able = True
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
    
    
    
    #고추장
    red_pepper_paste_y_pos += red_pepper_paste_speed
    #고추장이 화면밖에 있다면
    if red_pepper_paste_y_pos > screen_height:
        red_pepper_paste_y_pos = 0
        red_pepper_paste_x_pos = random.randint(150, 1650)
    
    red_pepper_paste_rect = red_pepper_paste.get_rect()
    red_pepper_paste_rect.left = red_pepper_paste_x_pos
    red_pepper_paste_rect.top = red_pepper_paste_y_pos
    
    if sick and red_pepper_paste_able and character_rect.colliderect(red_pepper_paste_rect):   
        score +=5
        character_eat_count +=5
        #item_text = game_font.render("tteok", True, (255, 0, 0))
        #screen.blit(item_text, (1600, 200))
        red_pepper_paste_time = time.time()
        eat_sound.play()
        change_eat_size()
        red_pepper_paste_y_pos = 0
        red_pepper_paste_x_pos = random.randint(150, 1650)
        #if gauge_able == True:
         #   gauge_x_pos -= 100
        
    #타이머
    if (time.time() - red_pepper_paste_time) < 0.5:
        red_pepper_paste_able = False
        character = pygame.image.load(r"C:\Python\project\cubby_2_(1).png")
        red_pepper_paste_material = 1
        red_pepper_paste_count = 1
    else:
        red_pepper_paste_able = True
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")


    

    #민초(쓰레기)
    trash_y_pos += trash_speed
    
    #민초가 화면밖에 있다면
    if trash_y_pos > screen_height:
        trash_y_pos = 0
        trash_x_pos = random.randint(150, 1650)

    #충돌 처리
    trash_rect = trash.get_rect()
    trash_rect.left = trash_x_pos
    trash_rect.top = trash_y_pos
    
    
    if trash_able and character_rect.colliderect(trash_rect):   
        score -= 500
        trash_cnt +=1
        character_eat_count = 0
        #item_text = game_font.render("tteok", True, (255, 0, 0))
        #screen.blit(item_text, (1600, 200))
        trash_time = time.time()
        eat_sound.play()
        change_eat_size()
        trash_y_pos = 0
        trash_x_pos = random.randint(150, 1650)
        if gauge_able == True:
            gauge_x_pos += 50
        tteok_count = green_onion_count = fish_cake_count = red_pepper_paste_count = 0
        tteok_material = green_onion_material = fish_cake_material = red_pepper_paste_material = 0
        if gauge_x_pos > 1650:
            gauge_x_pos = 1650
        
    #타이머
    if (time.time() - trash_time) < 0.5:
        trash_able = False
        character = pygame.image.load(r"C:\Python\project\cry_cubby.jpg")
        trash_material = "trash"
        trash_count = 1
    else:
        trash_able = True

    if (time.time() - trash_time) < 10:
        sick = False
        character = pygame.image.load(r"C:\Python\project\cry_cubby.jpg")
    elif (time.time() - trash_time > 10) and trash_count == 1:
        sick = True
        trash_material = " "
        character_scale = pygame.transform.scale(character, (100, 100))
        pygame.image.save(character_scale, 'cubby_1_(3).png')
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
        trash_count = 0




        
        
    #게이지
    if gauge_able and gauge_x_pos < 1300:       #피버타임 발동조건
        gauge_time = time.time()
        gauge_count = 1
        gauge_x_pos = 1300
        
    if gauge_count==1 and time.time() - gauge_time < 10:   #피버타임 지속중이다
        gauge_able = False
        character = pygame.image.load(r"C:\Python\project\cubby_2_big.png")
        character_eat_count = 0
        character_y_pos = 500
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        trash_able = False
    elif (time.time() - gauge_time >10) and gauge_count == 1:
        gauge_count = 0
        gauge_x_pos = 1650
        gauge_able = True
       # character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
        trash_able = True
        character = pygame.image.load(r"C:\Python\project\cubby_1_(1_1).png")
        character_scale = pygame.transform.scale(character, (100, 100))
        pygame.image.save(character_scale, 'cubby_1_(3).png')
        character = pygame.image.load(r"C:\Python\project\cubby_1_(3).png")
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character_y_pos = 800
        eat = pygame.image.load(r"C:\Python\project\cubby_2.png")
        eat_scale = pygame.transform.scale(eat, (100, 100))
        pygame.image.save(eat_scale, 'cubby_2_(1).png')
        eat_size = eat.get_rect().size
        
        
    
        
    
    #요리 완성시
    if complete_able and (tteok_count * green_onion_count * fish_cake_count * red_pepper_paste_count == 1):
        score += 1000
        complete_count +=1
        tteok_count = green_onion_count = fish_cake_count = red_pepper_paste_count = 0
        tteok_material = green_onion_material = fish_cake_material = red_pepper_paste_material = 0
        complete_time = time.time()
        if gauge_able == True:
            gauge_x_pos -= 80
        
        
    if (time.time() - complete_time) < 0.5:
        red_pepper_paste_able = False
    else:
        complete_able = True   
    
    
    
        
    #화면에 출력하기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(tteok, (tteok_x_pos, tteok_y_pos))
    screen.blit(green_onion, (green_onion_x_pos, green_onion_y_pos))
    screen.blit(fish_cake, (fish_cake_x_pos, fish_cake_y_pos))
    screen.blit(red_pepper_paste, (red_pepper_paste_x_pos, red_pepper_paste_y_pos))
    screen.blit(trash, (trash_x_pos, trash_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = game_font.render("Time: " + str(int(total_time - elapsed_time)), True, (255, 0, 0))
    screen.blit(timer, (300, 200))
    
    score_text = game_font.render("Score: " + str(score), True, (0, 0, 255))
    screen.blit(score_text, (500, 200))
    
    if tteok_material == 0:
        tteok_text = game_font.render("tteok", True, (255, 0, 0))
    else:
        tteok_text = game_font.render("tteok", True, (1, 0, 0))
    screen.blit(tteok_text, (1500, 200))
    
    if green_onion_material==0:
        green_onion_text = game_font.render("green_onion", True, (255, 0, 0))
    else:
        green_onion_text = game_font.render("green_onion", True, (1, 0, 0))
    screen.blit(green_onion_text, (1500, 250))
    
    
    if fish_cake_material==0:
        fish_cake_text = game_font.render("fish_cake", True, (255, 0, 0))
    else:
        fish_cake_text = game_font.render("fish_cake", True, (1, 0, 0))
    screen.blit(fish_cake_text, (1500, 300))
    
    if red_pepper_paste_material==0:    
        red_pepper_paste_text = game_font.render("red_pepper_paste", True, (255, 0, 0))
    else:
        red_pepper_paste_text = game_font.render("red_pepper_paste", True, (1, 0, 0))
    screen.blit(red_pepper_paste_text, (1500, 350))
    
    trash_text = game_font.render("trash: " +str(trash_cnt), True, (0, 255, 0))
    #trash_text = game_font.render("trash: "+ str(trash_cnt), True, (0, 255, 0))
    screen.blit(trash_text, (1500, 400))
    
    #test = game_font.render("@@@@@@@@@@", True, (255, 0, 0))
    #screen.blit(test, (1500, 100))
    
    complete_text = game_font.render("Tteokbokki: "+str(complete_count), True, (0, 0, 255))
    screen.blit(complete_text, (1500, 450))
    
    
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        time.sleep(5)
        running = False
        
    
    #게이지바 제작
    screen.blit(gauge, (gauge_x_pos, gauge_y_pos))
    #x좌표: 1650~1300 
    #350이니깐.. 30씩 하면 되것다
        

    pygame.display.update()
    
    #pygame.quit()

    




















# https://velog.io/@wltn39/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B2%8C%EC%9E%84-1-%EB%98%A5%ED%94%BC%ED%95%98%EA%B8%B0
# https://blog.naver.com/PostView.nhn?blogId=topblade71&logNo=221507282811&parentCategoryNo=&categoryNo=13&viewDate=&isShowPopularPosts=true&from=search
