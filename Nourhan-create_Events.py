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
        
def move (player,keys):
  # to move the player up press (w)
    if key[K_w]: # check w is being pressed.
      if player.rect.top > 0:
        player_rect = player.rect.move (0,-12) # move the player 
       
     
         # to move the player down.
      if keys[K_s] # check if s is pressed
        if player.rect.bottom > (800): 
          player_rect = player.rect.move (0,12) # move the player
         
          # to move the player left.
      if keys[K_a] # check a is being pressed
        if player.rect.left > 0:
          player_rect =  player.rect.move (-12,0)
         
        # To move the player right. 
      if keys[K_d]:
        if player.rect.right < (800):
           player_rect = player.rect.move (12,0)
          
          
           
        
       
        
      
      
        
          
          

        
      
        
        
      
      
      
    


