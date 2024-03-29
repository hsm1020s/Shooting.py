import pygame

class Ship:
    """우주선을 관리하는 클래스"""

    def __init__(self,ai_game):
        """우주선을 초기화하고 시작 위치를 설정합니다"""
        self.screen = ai_game.screen #
        self.settings = ai_game.settings #
        self.screen_rect = ai_game.screen.get_rect() #

        # 우주선 이미지를 불러오고 사각형을 가져옵니다
        self.image = pygame.image.load(r'C:\renew\Shooting.py\alien_invasion\images\ship.bmp') #
        self.rect = self.image.get_rect()

        # 우주선의 초기 위치는 화면 하단 중앙입니다
        self.rect.midbottom = self.screen_rect.midbottom #

        # 우주선의 정확한 가로 위치 설정을 위해 부동소수점 숫자를 저장
        self.x = float(self.rect.x) #

        # 움직임 플래그는 정지 상태로 시작합니다
        self.moving_right = False # 오른쪽 
        self.moving_left = False # 왼쪽
#-------------------------------------------------------------------------------------------------------------
        self.image_mhs = pygame.image.load(r'C:\renew\Shooting.py\alien_invasion\images\mhs.bmp')
        self.rect2 = self.image_mhs.get_rect()

        # self.image_mhs를 화면 중앙에 그립니다
        #self.rect2.center = self.screen_rect.center  이미지 임시로 제거
#-------------------------------------------------------------------------------------------------------------        
    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치를 업데이트합니다"""

        #rect가 아니라 우주선의 x 의 값을 업데이트한다.
        if self.moving_right and self.rect.right < self.screen_rect.right: # 여기 문제있어보인다 self.screen_rect
            self.x += self.settings.ship_speed #
            print("Screen rect right:", self.screen_rect.right)
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed #
        
        #self.x를 통해 rect 객체를 업데이트합니다
            self.rect.x = self.x # 

    def blitme(self): #
        """우주선을 현재 위치에 그립니다"""
        self.screen.blit(self.image, self.rect)

        #self.screen.blit(self.image_mhs, self.rect2)  이미지 임시로 제거


    