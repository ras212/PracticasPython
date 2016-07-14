import os
def rename_files ():
    # 1) Vamos a obtener el nombre de los archivos
   file_list = os.listdir ("D:\prank")
   print (file_list)
    saved_path = os.getcwd ()
    
   
   print ("El directorio activo es " +saved_path)
   os.chdir("D:\prank")
  
    # 2) Hacemos un bucle que los renombrará uno a uno:
   for file_name in file_list :
      os.rename (file_name, file_name.translate (None, "0123456789"))
      os.chdir(saved_path)
       rename_files()
    
