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
        
def move (Snake,keys):
   if key[K_w]: 
      if Snake.rect.top > 0:
       Snake_rect = Snake.rect.move (0,-12) 
    if keys[K_s] 
        if Snake.rect.bottom > (800): 
        Snake_rect = Snake.rect.move (0,12) 
    if keys[K_a] 
        if Snake.rect.left > 0:
        Snake_rect =  Snake.rect.move (-12,0)
    if keys[K_d]:
        if Snake.rect.right < (800):
        Snake_rect = Snake.rect.move (12,0)
          
          
           
        
       
        
      
      
        
          
          

        
      
        
        
      
      
      
    


