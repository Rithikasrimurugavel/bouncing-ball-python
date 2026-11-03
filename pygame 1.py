import pygame 
  
pygame.init()    
win = pygame.display.set_mode((1000, 700)) 
pygame.display.set_caption("blssom blast")
image = pygame.image.load(r"C:\rithika\pygame install\stars.png")
width=int(image.get_width()*0.1)
height=int(image.get_height()*0.1)
image=pygame.transform.scale(image,(width,height))


x = 600
y = 600
width,height = image.get_size()
vel = 10
run = True
while run: 
    pygame.time.delay(10)    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:  
            run = False 
    keys = pygame.key.get_pressed() 
         
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<990-width: 
          
        # increment in x co-ordinate 
        x += vel 
         
              
    # completely fill the surface object   
    # with black colour   
    win.fill((0, 0, 0))
    win.blit(image, (x, y))
       
    # it refreshes the window 
    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() 
