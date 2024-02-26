#Gray Wolf Habitat

def graywolf_habitat(): 
    import pygame
    import SpeciesMenu
    import Species_GrayWolf
    
    print("Gray Wolf habitats is running")
    
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
    GrayWolf_Image = pygame.image.load('./Assets/GrayWolf/Habitat.png')
    habitat_popout1 = pygame.image.load('./Assets/GrayWolf/Habitat-Popout1.png')
    habitat_popout2 = pygame.image.load('./Assets/GrayWolf/Habitat-Popout2.png')
    habitat_popout3 = pygame.image.load('./Assets/GrayWolf/Habitat-Popout3.png')
    habitat_popout4 = pygame.image.load('./Assets/GrayWolf/Habitat-Popout4.png')
    habitat_popout5 = pygame.image.load('./Assets/GrayWolf/Habitat-Popout5.png')

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  20 <= mouse[0] <= width/4 + 40 and height - 90 <= mouse[1] <= height: 
                    Species_GrayWolf.information()
                
                #if the mouse is clicked on the home button (Go back to main menu)
                if  width/4 + 75 <= mouse[0] <= width/2 + 95 and height - 90 <= mouse[1] <= height: 
                    SpeciesMenu.mainmenu_species()
                  
        # Sets the Gray Wolf Page as the BACKGROUND 
        screen.blit(GrayWolf_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over a bullet point - associated information popout appears 
        if  40 <= mouse[0] <= 150 and 3 * height / 4 + 20 <= mouse[1] <= 3 * height / 4 + 140:       screen.blit(habitat_popout1, (80, 3 * height / 4 + 20))
        if  210 <= mouse[0] <= 320 and 3 * height / 4 + 20 <= mouse[1] <= 3 * height / 4 + 140:       screen.blit(habitat_popout2, (250, 3 * height / 4 + 20))
        if  380 <= mouse[0] <= 490 and 3 * height / 4 + 20 <= mouse[1] <= 3 * height / 4 + 140:       screen.blit(habitat_popout3, (420, 3 * height / 4 + 20))
        if  550 <= mouse[0] <= 660 and 3 * height / 4 + 20 <= mouse[1] <= 3 * height / 4 + 140:       screen.blit(habitat_popout4, (590, 3 * height / 4 + 20))
        if  720 <= mouse[0] <= 830 and 3 * height / 4 + 20 <= mouse[1] <= 3 * height / 4 + 140:       screen.blit(habitat_popout5, (760, 3 * height / 4 + 20))

        # if mouse is hovered over the back button (Go back to Gray Wolf page) it changes to lighter shade 
        if  20 <= mouse[0] <= width/4 + 40 and height - 90 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (20, height - 90))                                       # blit the rectangle to the screen
        
        # if mouse is hovered over tenth button (Return to Main Menu) it changes to lighter shade 
        if  width/4 + 75 <= mouse[0] <= width/2 + 95 and height - 90 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (width/4 + 75, height - 90))                             # blit the rectangle to the screen
        ### -------------------------------------------------------------------- ###
        
        # updates the frames of the game 
        pygame.display.update() 