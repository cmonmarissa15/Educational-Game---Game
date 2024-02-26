#Bison Information page
import pygame
import SpeciesMenu
import Bison.identification     as Identification
import Bison.traits             as Traits
import Bison.diet               as Diet
import Bison.habitat            as Habitat
import Bison.threats            as Threats
import Bison.ecosystem          as Ecosystem
import Bison.conservation       as Conservation
import Bison.wolfpark           as WolfPark
import Bison.protect            as Protect

def information(): 
    
    print("Bison Testing menu is running")
    
    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    res = (1500, 1000) 
  
    # opens up a window 
    screen = pygame.display.set_mode(res)  
  
    # stores the width and height of the screen into variables 
    width = screen.get_width() 
    height = screen.get_height() 

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 

            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  20 <= mouse[0] <= width / 5 + 20 and height/4 <= mouse[1] <= height/2 + 50:                     Identification.bison_id()
                if  width/5 + 20 <= mouse[0] <= 2*width/5 + 10 and height/4 <= mouse[1] <= height/2 + 50:           Traits.bison_traits()
                if  2*width/5+10 <= mouse[0] <= 3*width/5 and height/4 <= mouse[1] <= height/2 + 50:                Diet.bison_diet()
                if  3*width/5 <= mouse[0] <= 4*width/5 - 10 and height/4 <= mouse[1] <= height/2 + 50:              Habitat.bison_habitat()
                if  4*width/5 -10 <= mouse[0] <= width - 20 and height/4 <= mouse[1] <= height/2 + 50:              Threats.bison_threats()
                if  20 <= mouse[0] <= width / 5 + 20 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100:             Ecosystem.bison_ecosystem()
                if  width/5 + 20 <= mouse[0] <= 2*width/5 + 10 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100:   Conservation.bison_conservation()
                if  2*width/5+10 <= mouse[0] <= 3*width/5 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100:        WolfPark.bison_wolfpark()
                if  3*width/5 <= mouse[0] <= 4*width/5 - 10 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100:      Protect.bison_protect()
                if  4*width/5 - 10 <= mouse[0] <= width - 20 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100:     quit()
                if  2*width/5 - 25 <= mouse[0] <= 3*width/5 + 55 and height - 105 <= mouse[1] <= height - 25:       SpeciesMenu.mainmenu_species()

        # Sets the Bison Species Page as the BACKGROUND 
        bison_Image = pygame.image.load('./Assets/Bison/SpeciesPage-BisonSized.png')
        screen.blit(bison_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over first button (Identification) it adds a box around it
        if  20 <= mouse[0] <= width / 5 + 20 and height/4 <= mouse[1] <= height/2 + 50:      
            s = pygame.Surface((width/5, height/4 + 50), pygame.SRCALPHA)       # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (20,height/4))                                       # blit the rectangle to the screen
        
        # if mouse is hovered over second button (Unique traits, behaviors and abilities) it changes to lighter shade 
        if  width/5 + 20 <= mouse[0] <= 2*width/5 + 10 and height/4 <= mouse[1] <= height/2 + 50: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (width/5 + 20, height/4))                            # blit the rectangle to the screen
        
        # if mouse is hovered over third button (Diet) it changes to lighter shade 
        if  2*width/5+10 <= mouse[0] <= 3*width/5 and height/4 <= mouse[1] <= height/2 + 50: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (2*width/5+10, height/4))                            # blit the rectangle to the screen
        
        # if mouse is hovered over fourth button (Habitat) it changes to lighter shade 
        if  3*width/5 <= mouse[0] <= 4*width/5 - 10 and height/4 <= mouse[1] <= height/2 + 50: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (3*width/5, height/4))                               # blit the rectangle to the screen
        
        # if mouse is hovered over fifth button (Threats) it changes to lighter shade 
        if  4*width/5 -10 <= mouse[0] <= width - 20 and height/4 <= mouse[1] <= height/2 + 50: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (4*width/5-10, height/4))                            # blit the rectangle to the screen
        
        # if mouse is hovered over sixth button (Role in Ecosystem) it changes to lighter shade 
        if  20 <= mouse[0] <= width / 5 + 20 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100: 
            s = pygame.Surface((width/5, height/4 + 50), pygame.SRCALPHA)       # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (20,height/2+50))                                    # blit the rectangle to the screen
        
        # if mouse is hovered over seventh button (Conservation Status) it changes to lighter shade 
        if  width/5 + 20 <= mouse[0] <= 2*width/5 + 10 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (width/5 + 20, height/2 + 50))                       # blit the rectangle to the screen
        
        # if mouse is hovered over eighth button (Bison at Wolf Park) it changes to lighter shade 
        if  2*width/5+10 <= mouse[0] <= 3*width/5 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (2*width/5+10, height/2 + 50))                       # blit the rectangle to the screen
        
        # if mouse is hovered over ninth button (How can people protect Bison?) it changes to lighter shade 
        if  3*width/5 <= mouse[0] <= 4*width/5 - 10 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (3*width/5, height/2 + 50))                          # blit the rectangle to the screen

        # if mouse is hovered over tenth button (Take a Quiz) it changes to lighter shade 
        if  4*width/5 - 10 <= mouse[0] <= width - 20 and height/2 + 50 <= mouse[1] <= 3*height/4 + 100: 
            s = pygame.Surface((width/5-10, height/4 + 50), pygame.SRCALPHA)    # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (4*width/5-10, height/2 + 50))                       # blit the rectangle to the screen
    
        # if mouse is hovered over main menu button (Return to Main Menu) it changes to lighter shade 
        if  2*width/5 - 25 <= mouse[0] <= 3*width/5 + 55 and height - 105 <= mouse[1] <= height - 25: 
            s = pygame.Surface((width/5 + 80, 80), pygame.SRCALPHA)             # per-pixel alpha
            s.fill((170,170,170,128))                                           # notice the alpha value in the color
            screen.blit(s, (2*width/5 - 25, height - 105))                      # blit the rectangle to the screen
        ### -------------------------------------------------------------------- ###
        
        # updates the frames of the game 
        pygame.display.update() 
