from moviepy.editor import ImageSequenceClip
images = []
for i in range(1, 11):
    images.append(f'C:\Users\harsh\OneDrive\Pictures\kali.jpg')
clip = ImageSequenceClip(images, fps=1)
clip.write_gif('demo.gif')
clip.close()
print("GIF created successfully! Check 'demo.gif'")