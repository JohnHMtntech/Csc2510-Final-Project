import pygame
#import random
from game import Game
from button import Button
#from card import Card

class Graphics:
    CARD_SCALE = .4
    CARD_SIZE = (500*CARD_SCALE,726*CARD_SCALE)
    CARD_BACK_IMAGE = pygame.image.load("assets\\cards\\card_back.png")

    def __init__(self):
        #Initalize pygame
        pygame.init()
        pygame.font.init()

        #Create window
        pygame.display.set_caption("Blackjack")
        pygame.display.set_icon(pygame.image.load("assets\\cards\\card_back.png"))
        self.screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.round_ended = False
        self.main_game = Game()
        self.main_game.fill_deck()
        self.main_game.shuffle_deck()
        self.main_game.start_hand()

    def end_round(self):
        if len(self.main_game.second_player_hand) == 0:
            self.round_ended = True
            self.main_game.run_dealers_turn()
            if self.main_game.get_winner() == "dealer":
                self.main_game.chips-=self.main_game.current_bet
            elif self.main_game.get_winner() == "player":
                self.main_game.chips+=self.main_game.current_bet
        elif self.main_game.first_hand_total != 0:
            self.round_ended = True
            self.main_game.run_dealers_turn()
            if self.main_game.get_winner() == "dealer":
                self.main_game.chips-=self.main_game.current_bet
            elif self.main_game.get_winner() == "player":
                self.main_game.chips+=self.main_game.current_bet
        else:
            self.main_game.first_hand_total = self.main_game.get_player_point_total()
            self.main_game.current_player_hand = self.main_game.second_player_hand
            
    def run_game(self):
        mouse_pos = (0,0)
        getting_bet = True
        bet = "0"
        invalid_value = "1"

        hit_button = Button("assets\\hit.png", (160,90), (1100,600))
        stand_button = Button("assets\\stand.png", (160,90), (1100,500))
        double_down_button = Button("assets\\double_down.png", (160,90), (1100,400))
        split_button = Button("assets\\split.png", (160,90), (1100,300))

        while self.running:
            #Refill deck
            if len(self.main_game.deck) == 0:
                self.main_game.fill_deck()
                self.main_game.shuffle_deck()

            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Button Handling
                    if not self.round_ended and not getting_bet:
                        if hit_button.is_touching_mouse(mouse_pos):
                            self.main_game.current_player_hand.append(self.main_game.draw_card())
                            self.main_game.is_turn_one = False
                            if self.main_game.get_player_point_total() >= 21:
                                self.end_round()
                        elif stand_button.is_touching_mouse(mouse_pos):
                            self.end_round()
                        elif double_down_button.is_touching_mouse(mouse_pos):
                            self.main_game.is_turn_one = False
                            self.end_round()
                        elif split_button.is_touching_mouse(mouse_pos):
                            self.main_game.is_turn_one = False
                            self.main_game.second_player_hand.append(self.main_game.current_player_hand.pop(1))

            #Apply background
            self.screen.blit(pygame.transform.scale(pygame.image.load("assets\\wood_texture.jpg"), self.screen.get_size()), (0,0))

            #Key handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_F11]:
                pygame.display.toggle_fullscreen()
            if self.round_ended and not getting_bet and keys[pygame.K_TAB]:
                getting_bet = True
                self.round_ended = False
                bet = "0"
            
            #Bet handling
            if getting_bet:
                #Variables
                chip_surface = pygame.font.SysFont('Comic Sans MS', 50).render(f"Chips: {self.main_game.chips}", False, (0, 0, 0))
                bet_surface = pygame.font.SysFont('Comic Sans MS', 30).render(f"{bet} chips", False, (0, 0, 0))
                bet_too_much_surface = pygame.font.SysFont('Comic Sans MS', 30).render(f"{invalid_value} is more chips than you have", False, (0, 0, 0))
                bet_too_little_surface = pygame.font.SysFont('Comic Sans MS', 30).render("You need to bet atleast 1 chip", False, (0, 0, 0))
                bet_not_int = pygame.font.SysFont('Comic Sans MS', 30).render("Bet is not an integer", False, (0, 0, 0))

                #Draw text
                self.screen.blit(chip_surface, (self.screen.get_width()/2-chip_surface.get_width()/2,100))
                self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render("Type in your bet. Press enter to continue", False, (0, 0, 0)), (400,160))
                self.screen.blit(bet_surface, (self.screen.get_width()/2-bet_surface.get_width()/2,200))
                
                if invalid_value == "not_int":
                    self.screen.blit(bet_not_int, (self.screen.get_width()/2-bet_too_much_surface.get_width()/2,250))
                elif int(invalid_value) > self.main_game.chips:
                    self.screen.blit(bet_too_much_surface, (self.screen.get_width()/2-bet_too_much_surface.get_width()/2,250))
                elif int(invalid_value) < 1:
                    self.screen.blit(bet_too_little_surface, (self.screen.get_width()/2-bet_too_little_surface.get_width()/2,250))

                if keys[pygame.K_RETURN]:
                    try:
                        if int(bet) > self.main_game.chips or int(bet) < 1:
                            raise TypeError
                        getting_bet = False
                        self.main_game.current_bet = int(bet)
                        self.main_game.start_hand()
                        if self.main_game.get_dealer_point_total() == 21:
                            self.round_ended = True
                            self.main_game.dealer_blackjack = True
                        if self.main_game.get_player_point_total() == 21:
                            self.round_ended = True
                            self.main_game.player_blackjack = True
                    except TypeError:
                        invalid_value = bet
                        bet = "0"
                    except ValueError:
                        invalid_value = "not_int"
                        bet = "0"
                if keys[pygame.K_0]:
                    if bet != "0":
                        bet+="0"
                if keys[pygame.K_1]:
                    if bet != "0":
                        bet+="1"
                    else:
                        bet = "1"
                if keys[pygame.K_2]:
                    if bet != "0":
                        bet+="2"
                    else:
                        bet = "2"
                if keys[pygame.K_3]:
                    if bet != "0":
                        bet+="3"
                    else:
                        bet = "3"
                if keys[pygame.K_4]:
                    if bet != "0":
                        bet+="4"
                    else:
                        bet = "4"
                if keys[pygame.K_5]:
                    if bet != "0":
                        bet+="5"
                    else:
                        bet = "5"
                if keys[pygame.K_6]:
                    if bet != "0":
                        bet+="6"
                    else:
                        bet = "6"
                if keys[pygame.K_7]:
                    if bet != "0":
                        bet+="7"
                    else:
                        bet = "7"
                if keys[pygame.K_8]:
                    if bet != "0":
                        bet+="8"
                    else:
                        bet = "8"
                if keys[pygame.K_9]:
                    if bet != "0":
                        bet+="9"
                    else:
                        bet = "9"
                if keys[pygame.K_BACKSPACE]:
                    if len(bet) == 1:
                        bet = "0"
                    else:
                        bet = bet[:len(bet)-2]
            #Draw buttons
            if not getting_bet:        
                hit_button.render(self.screen)        
                stand_button.render(self.screen)
                if self.main_game.is_turn_one:
                    double_down_button.render(self.screen)
                    if self.main_game.current_player_hand[0].rank == self.main_game.current_player_hand[1].rank:
                        split_button.render(self.screen)
                    else:
                        split_button.unrender()
                else:
                    double_down_button.unrender()
                    split_button.unrender()

                #Draw text
                if self.round_ended:
                    self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(self.main_game.get_dealer_point_total()), False, (0, 0, 0)), (250,140))
                    self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render("Press Tab to continue", False, (0, 0, 0)), (800,10))
                else:
                    self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(self.main_game.get_card_point_value(self.main_game.dealer_hand[0])), False, (0, 0, 0)), (250,140))
                self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(self.main_game.get_player_point_total()), False, (0, 0, 0)), (250,540))
                self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(len(self.main_game.deck)), False, (0, 0, 0)), (10,680))
                self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(f"Chips: {self.main_game.chips}", False, (0, 0, 0)), (10,10))
                self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(f"Current Bet: {self.main_game.current_bet}", False, (0, 0, 0)), (10,50))

                #Draw Pile
                self.screen.blit(pygame.transform.scale(Graphics.CARD_BACK_IMAGE, Graphics.CARD_SIZE), (10, self.screen.get_height()-Graphics.CARD_SIZE[1]-50))
            
            
                #Dealer's hand
                if self.round_ended:
                    for i in range(len(self.main_game.dealer_hand)):
                        self.screen.blit(pygame.transform.scale(pygame.image.load("assets\\cards\\"+self.main_game.dealer_hand[i].texture), Graphics.CARD_SIZE), (300+50*i,10))
                else:
                    self.screen.blit(pygame.transform.scale(pygame.image.load("assets\\cards\\"+self.main_game.dealer_hand[0].texture), Graphics.CARD_SIZE), (300,10))
                    for i in range(len(self.main_game.dealer_hand)-1):
                        self.screen.blit(pygame.transform.scale(Graphics.CARD_BACK_IMAGE, Graphics.CARD_SIZE), (350+50*i,10))
                
                #Player's cards
                for i in range(len(self.main_game.current_player_hand)):
                    self.screen.blit(pygame.transform.scale(pygame.image.load("assets\\cards\\"+self.main_game.current_player_hand[i].texture), Graphics.CARD_SIZE), (300+50*i,400))
            
            pygame.display.flip()

            self.dt = self.clock.tick(120) / 1000
        pygame.quit()

if __name__ == "__main__":
    game = Graphics()
    game.run_game()