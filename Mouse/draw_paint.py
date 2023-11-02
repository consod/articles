import mouse # pip install mouse
import time

text_size = 200
space_size = 50
duration = 0.5

time.sleep(3)

# Start drawing a C
mouse.drag(0, 0, -text_size, 0, absolute=False, duration=duration)  
mouse.drag(0, 0, 0, text_size*2, absolute=False, duration=duration)
mouse.drag(0, 0, text_size, 0, absolute=False, duration=duration) 

# Space
mouse.move(space_size, 0, absolute=False, duration=duration)

# Draw O
mouse.drag(0, 0, text_size, 0, absolute=False, duration=duration)  
mouse.drag(0, 0, 0, -text_size*2, absolute=False, duration=duration)
mouse.drag(0, 0, -text_size, 0, absolute=False, duration=duration)
mouse.drag(0, 0, 0, text_size*2, absolute=False, duration=duration)

# Space
mouse.move(space_size+text_size, 0, absolute=False, duration=duration)

# Draw N
mouse.drag(0, 0, 0, -text_size*2, absolute=False, duration=duration)  
mouse.drag(0, 0, text_size, text_size*2, absolute=False, duration=duration)
mouse.drag(0, 0, 0, -text_size*2, absolute=False, duration=duration)  

# Space
mouse.move(space_size, text_size*2, absolute=False, duration=duration)

# Draw N
mouse.drag(0, 0, 0, -text_size*2, absolute=False, duration=duration)  
mouse.drag(0, 0, text_size, text_size*2, absolute=False, duration=duration)
mouse.drag(0, 0, 0, -text_size*2, absolute=False, duration=duration) 

# Space
mouse.move(space_size, 0, absolute=False, duration=duration)

# Draw Y
mouse.drag(0, 0, text_size*0.5, text_size, absolute=False, duration=duration)
mouse.drag(0, 0, 0, text_size, absolute=False, duration=duration)
mouse.move(0, -text_size, absolute=False, duration=duration)
mouse.drag(0, 0, text_size*0.5, -text_size, absolute=False, duration=duration)