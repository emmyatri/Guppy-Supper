while True:
  key = pygame.key.get_pressed()
  for event in pygame.event.get:
    pass # handle all the event 
    if event.type == event.QUIT:
        pygame.quit()
        sys.exit(0)
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_escape:
        pygame.quit()
        sys.exit(0)
   # press R to reset  the player position.
    elif event.type == pygame.K_r:
      player_rect.(position of the player ex: center,left, up, down) = (display size // 2)
      print("[EVENT] KEYDOWN: USER PRESSED BUTTON R -> RESETTING PLAYER POSITION")
    # All the keys that USE TO move the player.
  keys = pygame.key.get_pressed()
  
  # to move the player up press (w)
    if key[K_w]: # check w is being pressed.
      if player.rect.top > 0:
        player_rect = player.rect.move (0,-5) # move the player 
        print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> MOVING PLAYER UP")
      else:
        print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
     
         # to move the player down.
      if keys[K_s] # check if s is pressed
        if player.rect.bottom > (display size): 
          player_rect = player.rect.move (0,5) # move the player
          print(""[EVENT] KEY STATE: S KEY IS BEING PRESSED -> MOVING PLAYER down ")
        else:
          print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
       
          # to move the player left.
      if keys[K_a] # check a is being pressed
        if player.rect.left > 0:
          player_rect =  player.rect.move (-5,0)
          print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> MOVING PLAYER left")
        else:
          print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
      
        # To move the player right. 
      if keys[K_d]:
        if player.rect.right < (display size):
           player_rect = player.rect.move (5,0)
           print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> MOVING PLAYER right")
        else:
           print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")


        
       
        
      
      
        
          
          

        
      
        
        
      
      
      
    


