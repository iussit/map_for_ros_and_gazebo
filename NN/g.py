from PIL import Image,ImageOps


count=1
while(count<=16):
   string="sample/wall/"+str(count)+".png"
   print(string)
   img = Image.open(string)
   mirror_img = ImageOps.mirror(img)
   name=count+16
   mirror_img.save(str(name)+'.png')
   count+=1
