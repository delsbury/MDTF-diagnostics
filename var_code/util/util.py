# This file is part of the util module of the MDTF code package (see mdtf/MDTF_v2.0/LICENSE.txt)



def setenv(varname,varvalue,env_dict,verbose=0,overwrite=True):
   import os
   # env_dict: a dictionary to be dumped once file is created
   # This is a wrapper to os.environ so any new env vars 
   # automatically get written to the file
   
   if (not overwrite) and ('varname' in env_dict): 
      if (verbose > 0): print "Not overwriting ENV ",varname," = ",env_dict[varname]
   else:
      if ('varname' in env_dict) and (env_dict[varname] != varvalue) and (verbose > 0): 
         print "WARNING: setenv ",varname," = ",varvalue," overriding previous setting ",env_dict[varname]
      env_dict[varname] = varvalue

      # environment variables must be strings
      if type(varvalue) is bool:
         if varvalue == True:
            varvalue = '1'
         else:
            varvalue = '0'
      elif type(varvalue) is not str:
         varvalue = str(varvalue)
      os.environ[varname] = varvalue

      if (verbose > 0): print "ENV ",varname," = ",env_dict[varname]
   if ( verbose > 2) : print "Check ",varname," ",env_dict[varname]



def check_required_dirs(verbose=3, already_exist =[], create_if_nec = []):
   # arguments can be envvar name or just the paths

   import os
   filestr = __file__+":check_required_dirs: "
   errstr = "ERROR "+filestr
   if verbose > 1: filestr +" starting"
   for dir_in in already_exist + create_if_nec : 
      if verbose > 1: "\t looking at "+dir_in

      if dir_in in os.environ:  
         dir = os.environ[dir_in]
      else:
         if verbose>2: print(" envvar "+dir_in+" not defined")    
         dir = dir_in

      if not os.path.exists(dir):
         if not dir_in in create_if_nec:
            if (verbose>0): 
                print(errstr+dir_in+" = "+dir+" directory does not exist")
                print("         and not create_if_nec list: ",create_if_nec)
            exit()
         else:
            print(dir_in+" = "+dir+" created")
            os.makedirs(dir)
      else:
         print("Found "+dir)
