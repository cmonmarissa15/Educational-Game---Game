#Bison Identification sub-page

def bison_id(): 
    import pygame
    import SpeciesMenu
    import Species_Bison
    
    print("Bison identification is running")
    
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
    bison_Image = pygame.image.load('./Assets/Bison/Identification.png')
    identification_popout1 = pygame.image.load('./Assets/Bison/Identification-Popout1.png')
    identification_popout2 = pygame.image.load('./Assets/Bison/Identification-Popout2.png')
    identification_popout3 = pygame.image.load('./Assets/Bison/Identification-Popout3.png')
    identification_popout4 = pygame.image.load('./Assets/Bison/Identification-Popout4.png')
    identification_popout5 = pygame.image.load('./Assets/Bison/Identification-Popout5.png')

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
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 90 <= mouse[1] <= height / 2 + 130:        screen.blit(identification_popout1, (80, height / 2 + 30))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 150 <= mouse[1] <= height / 2 + 190:       screen.blit(identification_popout2, (80, height / 2 + 90))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 220 <= mouse[1] <= height / 2 + 260:       screen.blit(identification_popout3, (80, height / 2 + 150))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 280 <= mouse[1] <= height / 2 + 320:       screen.blit(identification_popout4, (80, height / 2 + 220))
        if  20 <= mouse[0] <= width/4 - 40 and height / 2 + 350 <= mouse[1] <= height / 2 + 390:       screen.blit(identification_popout5, (80, height / 2 + 280))
        
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
