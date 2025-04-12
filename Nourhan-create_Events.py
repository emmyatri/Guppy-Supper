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
   if key[K_w]: 
      if player.rect.top > 0:
       player_rect = player.rect.move (0,-12) # move the player 
    if keys[K_s] 
        if player.rect.bottom > (800): 
        player_rect = player.rect.move (0,12) # move the player
    if keys[K_a] 
        if player.rect.left > 0:
        player_rect =  player.rect.move (-12,0)
    if keys[K_d]:
        if player.rect.right < (800):
        player_rect = player.rect.move (12,0)
          
          
           
        
       
        
      
      
        
          
          

        
      
        
        
      
      
      
    


