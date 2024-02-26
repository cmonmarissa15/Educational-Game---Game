#Gray Wolf Diet

def graywolf_diet(): 
    import pygame
    import SpeciesMenu
    import Species_GrayWolf
    
    print("Gray Wolf diet is running")
    
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
    GrayWolf_Image = pygame.image.load('./Assets/GrayWolf/Diet.png')

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  width/2 - 95 <= mouse[0] <= 3*width/4 - 75 and height - 100 <= mouse[1] <= height: 
                    Species_GrayWolf.information()
                
                #if the mouse is clicked on the home button (Go back to main menu)
                if  3*width/4 - 35 <= mouse[0] <= width - 15 and height - 100 <= mouse[1] <= height: 
                    SpeciesMenu.mainmenu_species()
                  
        # Sets the Gray Wolf Page as the BACKGROUND 
        screen.blit(GrayWolf_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over the back button (Go back to Gray Wolf page) it changes to lighter shade 
        if  width/2 - 95 <= mouse[0] <= 3*width/4 - 75 and height - 100 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (width/2 - 95, height - 100))                            # blit the rectangle to the screen
        
        # if mouse is hovered over tenth button (Return to Main Menu) it changes to lighter shade 
        if  3*width/4 - 35 <= mouse[0] <= width - 15 and height - 100 <= mouse[1] <= height: 
            s = pygame.Surface((width/4 + 20, 90), pygame.SRCALPHA)                 # per-pixel alpha
            s.fill((170,170,170,128))                                               # notice the alpha value in the color
            screen.blit(s, (3*width/4 - 35, height - 100))                          # blit the rectangle to the screen
        ### -------------------------------------------------------------------- ###
        
        # updates the frames of the game 
        pygame.display.update() 
