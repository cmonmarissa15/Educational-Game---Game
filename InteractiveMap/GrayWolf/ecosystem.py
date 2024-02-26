#Gray Wolf Role in the Ecosystem

def graywolf_ecosystem(): 
    import pygame
    import SpeciesMenu
    import Species_GrayWolf
    
    print("Gray Wolf role in the ecosystem is running")
    
    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    res = (1500, 1000) 
  
    # opens up a window 
    screen = pygame.display.set_mode(res) 
  
    # stores the width and height of the screen into variables 
    width = screen.get_width() 
    height = screen.get_height() 
  
    # Load all images
    GrayWolf_Image = pygame.image.load('./Assets/GrayWolf/Ecosystem.png')
    ecosystem_popout1 = pygame.image.load('./Assets/GrayWolf/Ecosystem-Popout1.png')
    ecosystem_popout2 = pygame.image.load('./Assets/GrayWolf/Ecosystem-Popout2.png')
    ecosystem_popout3 = pygame.image.load('./Assets/GrayWolf/Ecosystem-Popout3.png')
    ecosystem_popout4 = pygame.image.load('./Assets/GrayWolf/Ecosystem-Popout4.png')
    ecosystem_popout5 = pygame.image.load('./Assets/GrayWolf/Ecosystem-Popout5.png')

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  width/4-40 <= mouse[0] <= width/2 - 20 and height - 90 <= mouse[1] <= height: 
                    Species_GrayWolf.information()
                
                #if the mouse is clicked on the home button (Go back to main menu)
                if width/2 + 20 <= mouse[0] <= 3*width/4 + 40 and height - 90 <= mouse[1] <= height: 
                    SpeciesMenu.mainmenu_species()
                  
        # Sets the Gray Wolf Page as the BACKGROUND 
        screen.blit(GrayWolf_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over a bullet point - associated information popout appears 
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 - 200 <= mouse[1] <= height / 2 - 70:                 screen.blit(ecosystem_popout1, (20, height / 2 - 200))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 <= mouse[1] <= height / 2 + 130:                      screen.blit(ecosystem_popout2, (20, height / 2))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 200 <= mouse[1] <= height / 2 +330:                 screen.blit(ecosystem_popout3, (20, height / 2 + 200))
        if  3*width/4 - 40 <= mouse[0] <= width - 20 and height / 2 - 100 <= mouse[1] <= height / 2 + 30:       screen.blit(ecosystem_popout4, (3*width/4-40, height / 2 - 100))
        if  3*width/4 - 40 <= mouse[0] <= width - 20 and height / 2 + 100 <= mouse[1] <= height / 2 + 230:      screen.blit(ecosystem_popout5, (3*width/4-40, height / 2 + 100))

        # if mouse is hovered over the back button (Go back to Gray Wolf page) it changes to lighter shade 
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