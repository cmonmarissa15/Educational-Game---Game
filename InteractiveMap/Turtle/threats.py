#Turtle Threats

def turtle_threats(): 
    import pygame
    import SpeciesMenu
    import Species_Turtle
    
    print("Turtle threats is running")
    
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
    Turtle_Image = pygame.image.load('./Assets/Turtles/Threats.png')

    while True: 
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if  width/4-40 <= mouse[0] <= width/2 - 20 and height - 90 <= mouse[1] <= height: 
                    Species_Turtle.information()
                
                #if the mouse is clicked on the home button (Go back to main menu)
                if width/2 + 20 <= mouse[0] <= 3*width/4 + 40 and height - 90 <= mouse[1] <= height: 
                    SpeciesMenu.mainmenu_species()
                  
        # Sets the Turtle Page as the BACKGROUND 
        screen.blit(Turtle_Image, (0, 0))
      
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()

        ### -----------------------------------------------------------------------### 
        # if mouse is hovered over the back button (Go back to Turtle page) it changes to lighter shade 
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