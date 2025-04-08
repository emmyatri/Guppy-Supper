while True:
  key = pygame.key.get_pressed()
  for event in pygame.event.get:
    pass # handle all the event 
    if event.type == event.QUIT:
        pygame.quit()
        sys.exit(0)
    if event.type


