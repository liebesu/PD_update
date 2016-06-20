# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import random

from lib.common.colors import color, yellow


def logo():
    """Cuckoo asciiarts.
    @return: asciiarts array.
    """
    logos = []

    
    logos.append("""
                                                              
                }$$$$$$$$$$$$$$$$$$$$$$$$$$^                
            $$$$$,$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$            
            $$$    $$$$$$$$$$$$$$$$$$$$$$    $$$            
                   $$$$$$$$$$$$$$$$$$$$$$                   
         $$$   B$   $$$$$$$$$$$$$$$$$$$$   $$   $$$         
      $$$$$$*$$$$    $$$$$$$ $$ $$$$$$$   ;$$$$$$$$$$$      
     $$$$   -$$$$$   $$$$$$  $$  $$$$$#   $$$$$$   $$$$     
    $$$     . ]$$$$   $$$$   $$   $$$$   $$$$  $     $$$    
   $$$     $     u$$   $$    $@    $$   $$'     $     $$$   
  $$$    $$$ $         _     Ql               $ $$$    $$$  
  $$   $$$$   $$$            '             $$$ $ $$$$   $$  
 $$   $$.        $$                     .$$         $$   $$ 
  $  $$   $$ $     $$$   $        $   $$$     $ $$   $$  $  
  $ <$$ $$$  $$$      $  $$$!  B$$$  $      $$$$ $$$ $$. $  
    $$  $$$  $$$          $$$  $$$          $$$$ $$$  $$    
   $$$   ;$$.$   $$$$$                $$$$$   $$$$    $$$   
   $$      $  $$  X$$$$$(          $$$$$$   $$  $      $$   
    $       $  $$   $$$$$$  $$$$  $$$$$$   $$  $       $    
     $      $$   $$$$$$$$$$$$$$$$$$$$$$$$$$   $       $     
      $     .$$$     $$$$$$$$$$$$$$$$$$     $$$      $      
       '     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     k       
             *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$              
              $$$$$$ $  $$$$$$$$$$$$$$$$$$$$v               
               $$$$$ $$%$  $        $ $ $$$$$               
                $$$$ $$ $ $$$   $$$   $ $$$$                
                 $$$mmmm$mm$mm$mmmmm$$mm$$$                 
                  $$%$$%$%%$%%%%%%$%%%$%$$                  
                   $$$$$$$$$$$$$$$$$$$$.                    
                    $$$$$$$$$$$$$$$$$$$                     
                      $$$$$$$$$$$$$$$$                      
                        $$$$$$$$$$$$                        
                          $$$$$$ $                          
                                                                
    """)
    
    logos.append("""
                          $$r[[a "X[# ($                        
                   $Z[[[[[I    &    q[&                     
                 $[[[[[[[[   (f  h"  [[[%                   
               $t[[[[[[[[[      h    -Ou[a                  
               [[[[[[[|#  }    h kZhf    a$                 
             $[[[[[[1 >     pp" b  ZW  #>    $              
             [[[[[[(       >hn  nZZm>                       
            $[[[[[z               (                         
            [[[[[C                    I      $              
           $[[[[[    wZZZZdo#8n            h$               
           $[[[[r   nZm##wZZZZZZZZZbo&WW&d                  
           $[[[[a   -ZZZZZZZZZZZZZZZZZZZZO                  
           $[[[[p    ZZZZZZZZZZZZZZZZZZZa  O                
            Z[[[Z    CaOOOOOOmoZZZZZZZZ*                    
            $[[[[     %OOOOOOOOOkZZZZZh   $                 
             Q[[[#     "OOOOOOOOOZZZq    O                  
             $1[[[-      %OOOOOOO%Zh                        
               [[[[        "MOOOoI     8                    
                Z[[[h  IO&dZf   >Zw&%ZZM                    
                 %rkZZZoaQrz     IbMb&$z                    
                 $q#b[[[[[["      zzCzM $                   
                  $[[[[[[[[&     pzzbw  $                   
                   [[[[[[[[#-C nn  -->  p                   
                   [[[[uU[O n           n$     $            
                   |[[[[[[  h           (                   
                   a[[[[[[-  n         h        $           
               $ow$$[[[[[[X   n"     h -                    
               oZZZ$[[[[[[[Q          q                     
               $kZ@$[[[[[[[[[#     -q[[        $            
                   X[[[[[[[[[[[[[[[[[[[h      $             
                 $([[[[[[[[[[[[[[%$     $-  $               
                   X[[[[[[[[[X$                             
                $   q[[[[[u$                                
                p    a[[[$                                  
                $        $                                  
                 "       (                                  
                  $     ($                                  
    
    """)
    logos.append("""
                                                                                                                            
   $$$$$$$$$         $$$$$$$$$$                                                                                         
   $$      $$;       $$       >$$                                                                                       
   $$      $$        $$        ;$$                                            $                    ;                    
   $$$$$$$$$         $$         $$           f$    $       $ $$$$        $$$$ $       $$$$$      $$$$$        $$$$      
   $$                $$        $$$           f$    $       $    $$      $,    $           $$       $        $> $$ $     
   $$                $$       $$;            f$    $       $    $$      $     $      $$   $$       $        $+          
   $$                $$$$$$$$                 $$$$ $       $ $$$$        $$$$ $       $$$$$$       $$$       $$$$$$     
                                                           $                                                            
    """)

    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" PD_update")
    print(" From liebesu")
    print(" https://github.com/liebesu/PD_update")
    print(" www.polydata.com.cn")
    print(" Copyright (c) 2010-2015")
    print
    sys.stdout.flush()
