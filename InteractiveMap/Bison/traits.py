#Bison Unique traits, behaviors and abilities sub-page

def bison_traits(): 
    import pygame
    import SpeciesMenu
    import Species_Bison
    
    print("Bison unique traits is running")
    
    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    res = (1500, 1000) 
  
    # opens up a window 
    screen = pygame.display.set_mode(res)
  
    # stores the width and height of the screen into variables 
    width = screen.get_width() 
    height = screen.get_height() 
  
    #Load all images
    bison_Image = pygame.image.load('./Assets/Bison/Traits.png')
    traits_popout1 = pygame.image.load('./Assets/Bison/Traits-Popout1.png')
    traits_popout2 = pygame.image.load('./Assets/Bison/Traits-Popout2.png')
    traits_popout3 = pygame.image.load('./Assets/Bison/Traits-Popout3.png')
    traits_popout4 = pygame.image.load('./Assets/Bison/Traits-Popout4.png')
    traits_popout5 = pygame.image.load('./Assets/Bison/Traits-Popout5.png')
    traits_popout6 = pygame.image.load('./Assets/Bison/Traits-Popout6.png')

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  width/4-40 <= mouse[0] <= width/2 - 20 and height - 90 <= mouse[1] <= height: 
                    Species_Bison.information()
                
                #if the mouse is clicked on the home button (Go back to main menu)
                if width/2 + 20 <= mouse[0] <= 3*width/4 + 40 and height - 90 <= mouse[1] <= height: 
                    SpeciesMenu.mainmenu_species()
                  
        # Sets the Bison Species Page as the BACKGROUND 
        screen.blit(bison_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over a bullet point - associated information popout appears 
        if  width/2 + 60 <= mouse[0] <= 3*width/4 + 80 and height/4-20 <= mouse[1] <= height/4 + 50:            screen.blit(traits_popout1, (width/2 + 60, height/4-20))
        if  3*width/4-80 <= mouse[0] <= 3*width/4 + 300 and height/4 + 90 <= mouse[1] <= height/4 + 160:        screen.blit(traits_popout2, (3*width/4-80, height/4+90))
        if  width/2 + 60 <= mouse[0] <= 3*width/4 + 80 and height/2 - 40 <= mouse[1] <= height/2 + 40:          screen.blit(traits_popout3, (width/2 + 60, height/2-40))
        if  3*width/4-80 <= mouse[0] <= 3*width/4 + 300 and height/2 + 70 <= mouse[1] <= height/2 + 140:        screen.blit(traits_popout4, (3*width/4-80, height/2+70))
        if  width/2 + 60 <= mouse[0] <= 3*width/4 + 80 and 3*height/4 - 70 <= mouse[1] <= 3*height/4:           screen.blit(traits_popout5, (width/2 + 60, 3*height/4-70))
        if  3*width/4-80 <= mouse[0] <= 3*width/4 + 300 and 3*height/4 + 40 <= mouse[1] <= 3*height/4 + 110:    screen.blit(traits_popout6, (3*width/4-80, 3*height/4+40))

        # if mouse is hovered over the back button (Go back to Bison page) it changes to lighter shade 
        if  width/4-40 <= mouse[0] <= width/2 - 20 and height - 90 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (width/4 - 40, height - 90))                             # blit the rectangle to the screen
        
        # if mouse is hovered over tenth button (Return to Main Menu) it changes to lighter shade 
        if  width/2 + 20 <= mouse[0] <= 3*width/4 + 40 and height - 90 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (width/2 + 20, height - 90))                             # blit the rectangle to the screen
        ### -------------------------------------------------------------------- ###

        # updates the frames of the game 
        pygame.display.update() 
