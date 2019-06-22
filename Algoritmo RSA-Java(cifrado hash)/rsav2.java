package RSA;

import java.io.*;
import java.math.*;
import java.util.*;
import java.security.SecureRandom;
import java.nio.*;
import java.nio.charset.Charset;
public class RSA{

private BigInteger p,q,a,b,n,phinN;

public static void main(String[] args) throws IOException{
      RSA tmp = new RSA();
      tmp.texto(args);
   }

   public void texto(String[] args) throws IOException {
      generarclave();
      if (args[0].equals("-help")){
   System.out.println("ALGORITMO RSA\n"+"Estudiantes: Jose luis Rodriguez campos, Jonathan Rivas Cerrud\n"+"Profesor:Siler Amador Donado\nUNIVERSIDAD AUTONOMA DE OCCIDENTE [CALI,CO]\n----------------------------------------------------------------------------------------------\nSintaxis para ejecutar todo el codigo\n #java rsav2.java -r archivohash.txt archivocifrado.txt \n Donde archivocifrado = el nombre que tendra su arhcivo con el mensaje cifrado \n................................................................................. \nSintaxis para cifrar con el codigo\n # java rsav2.java -c archivohash.txt archivocifrado.txt \n Donde archivocifrado = el nombre que tendra su arhcivo con el mensaje cifrado\n............................................................................................\nSintaxis para descifrar con el codigo\n #java rsav2.java -d archivocifrado.txt archivodescifrado.txt \n Donde archivodescifrado = el nombre que tendra su arhcivo con el mensaje descifrado \n...............................................................................\nRecuerde que los archivos txt generados como el mensaje cifrado, la clave 'n' y 'e', se encuentra en la carpeta de Descargas; Si desea conocer como  cambiar las rutas ejecute\n #java rsav2.java -g \n ........................................................................");
      }
     

 

	      
if (args[0].equals("-g")){

      
      System.out.println("tenga en cuenta que este algoritmo RSA fue construido  para cifrar numeros o 'HASH de texto'\n "
              + "Si desea cambiar el hash de texto predeterminado por el programa continue con el siguiente ejempelo:\n "
              + "1- Primero en la consola de linux debe obtener el hash del texto que desea cifrar,\n # md5sum 'archivo.txt' > 'archivodehash.txt'\n2- Seguido de esto debe conocer la ruta donde se guardara dicho hash\n"
              + "3- luego en la consola de linux debe modificar el script de rsa de la siguiente manera\n"
              + " # vi rsa.java\n"
              + "4- en la linea numero '45'y '89' debe modificar la ruta de su archivo hash y guardar el script,\n"
              + " # String textocodificado  = textoorig( '/root/Downloads/)';\n"
             
              + "5- siguiente a esto debe guardar la configuracion y ejecutar de nuevo el porgrama  digitando 'run'\n"
	      +"6- Recuerde que el mensaje cifrado puede ser encontrado como archivo de texto en la siguiente ruta '/root/Downloads/'; si el programa se ejecuta desde otra parte debe modificar dicha ruta en el script en la lineas '70' y '111', la ruta de archivos de clave publica 'n' y 'e' estan en las lineas '74, 114, 78,118', por ultimo debe modificar la ruta del archivo a descifrar en las lineas '132' y '141'\n"
	      + "7- Para salir del programa oprima las teclas 'CONTROL' + 'C' , de lo contrario digite 'run'" );
  } if (args[0].equals("-r")){
      
      String archivo = args[1] ;
      String cifradot = args[2]; 
      String textocodificado = textoorig("/root/Downloads/"+archivo);
		      
      textocodificado = textocodificado.substring(0, textocodificado.length()-3);
      String textotxt = codificar(textocodificado);
      
      String textoCifrado = cifrar(procesarEntrada(textocodificado));
      String textoDecifrado = decifrar(procesarEntrada(textoCifrado));
      String caracteresDecifradoas = codificar(textoDecifrado);
    
     
      
      System.out.println("Mensaje del archivo : "+ textotxt);
      System.out.println("Mensaje Codificado: "+textocodificado);
      System.out.println("numero primo p : "+ p);
      System.out.println("numero primo q : "+ q);
      System.out.println("modulo n  : "+ n);
      System.out.println("clave privada  : "+ b);
      System.out.println("clave publica  : "+ a);
      System.out.println("valor phin  : "+ phinN);
      
      System.out.println("Mensaje cifrado: "+textoCifrado);
      System.out.println("Mensaje decifrado: "+textoDecifrado);
      System.out.println("Mensaje Decodificado: "+caracteresDecifradoas);
  
    FileWriter fichero = new FileWriter ("/root/Downloads/"+cifradot);
    fichero.write(textoCifrado);
    fichero.close();

   FileWriter ficheron = new FileWriter ("/root/Downloads/valorn.txt");
    String valorn = String.valueOf(n);
    ficheron.write(valorn);
    ficheron.close();
    FileWriter ficheroa = new FileWriter ("/root/Downloads/valore.txt");
    String valora = String.valueOf(a);
    ficheroa.write(valora);
    ficheroa.close();

  }
  //7/////////////////////////////////////////////////////////////
  if (args[0].equals("-c")){
 

      String archivo = args[1] ;
      String cifradot = args[2];
      String textocodificado = textoorig("/root/Downloads/"+archivo);
      textocodificado = textocodificado.substring(0, textocodificado.length()-4)
;//3
      String textotxt = codificar(textocodificado);

      String textoCifrado = cifrar(procesarEntrada(textocodificado));
     
      
;

      System.out.println("Mensaje del archivo : "+ textotxt);
      System.out.println("Mensaje Codificado: "+textocodificado);
      System.out.println("numero primo p : "+ p);
      System.out.println("numero primo q : "+ q);
      System.out.println("modulo n  : "+ n);
      System.out.println("clave privada  : "+ b);
      System.out.println("clave publica  : "+ a);
      System.out.println("valor phin  : "+ phinN);

      System.out.println("Mensaje cifrado: "+textoCifrado);

    FileWriter fichero = new FileWriter ("/root/Downloads/"+cifradot);
    fichero.write(textoCifrado);
    fichero.close();
    FileWriter ficheron = new FileWriter ("/root/Downloads/valorn.txt");
    String valorn = String.valueOf(n);
    ficheron.write(valorn);
    ficheron.close();
    FileWriter ficheroa = new FileWriter ("/root/Downloads/valore.txt");
    String valora = String.valueOf(a);
    ficheroa.write(valora);
    ficheroa.close();


  }

  /////////////////////////////////////////////////////////////////7
 if (args[0].equals("-d")){
 

      String archivocif = args[1] ;
      String descifradot = args[2];
      String textocodificad = textdecifrar("/root/Downloads/"+archivocif);
      textocodificad = textocodificad.substring(0, textocodificad.length()-0);
      String textoDecifrado = solodecif(procesarEntrada(textocodificad));
      String caracteresDecifradoas = codificar(textoDecifrado);
   

      System.out.println("Mensaje Cifrado: "+textocodificad);
     System.out.println("Mensaje Descifrado: "+textoDecifrado);
      System.out.println("Mensaje Decodificado: "+caracteresDecifradoas);
       
   FileWriter ficherod = new FileWriter ("/root/Downloads/"+descifradot);
    ficherod.write(caracteresDecifradoas);
    ficherod.write("\n");
    ficherod.close();
  }

//////////////////////////////////////////////////////////////////////////   
     
   } 
 //--------------------------------------------------------------------------------------------------------  
// metodo creado para separar el archivo 
   public LinkedList<BigInteger> procesarEntrada(String input){
      StringTokenizer tokens = new StringTokenizer(input,", ");
      LinkedList<BigInteger> ret = new LinkedList<BigInteger>();
      while( tokens.hasMoreTokens() ){
         ret.add(new BigInteger(tokens.nextToken()));
      }
      return ret;
   }
//--------------------------------------------------------------------------------------------------------
  // metodo creado para  leer el archivo enrrutado
    public String textoorig (String direccion ) throws FileNotFoundException{
       String texto ="";
       
       try{
         
	 FileInputStream valor = new FileInputStream (new File (direccion));
         String temp="";
         int  caracter;
         while ((caracter = valor.read()) != -1){
         
	      temp += caracter + " ";
         }
         texto = temp;
       } catch (FileNotFoundException ex){
       ex.printStackTrace();
       }  catch (Exception e){
       System.err.println("error");
       }
       
       return texto;
   }
//////////////////////////////////////////////////////////////7

//metodo para tomar mensaje cifrado 
    public String textdecifrar (String direccion ){
       String texto ="";
      
       
       try{
          BufferedReader bf = new BufferedReader (new FileReader( direccion));
         String temp="";
         String bfRead;
         while ((bfRead = bf.readLine()) !=null){
             temp = temp +  bfRead;
         }
         texto = temp;
       } catch (Exception e){
       System.err.println("error");
       }
       
       return texto;
   }

/////////////////////////////////////////////
 
 //-----------------------------------------------------------------------------------------------        
 // metodo para cifrar el mensaje codificado    
     
     public String cifrar(LinkedList<BigInteger> input){
      String ret = "";
      for(BigInteger aux : input){
         BigInteger cip = aux.modPow(b,n);
         ret += cip.toString()+", ";
      }
      return ret;
   }
 //---------------------------------------------------------------------------------------------------------    
  // metodo para descifrar el mensaje    
   public String decifrar(LinkedList<BigInteger> input){
      String ret = "";
      String ret2="";
      for(BigInteger aux : input){
         BigInteger dip = aux.modPow(a,n);
         ret += dip.toString()+ " ";
      }
      return ret;
      
   }
//..................................................................
// metodo para solo decifrar el hash
   public String solodecif(LinkedList<BigInteger> input){
       System.out.println("ingrese el valor de n");
Scanner entrada2=new Scanner(System.in);
BigInteger cadena2 =entrada2.nextBigInteger();
System.out.println("ingrese el valor de e");
Scanner entrada3=new Scanner(System.in);
BigInteger cadena3 =entrada3.nextBigInteger();

 
 
      String ret = "";
      String ret2="";
      for(BigInteger aux : input){
         BigInteger dip = aux.modPow(cadena3,cadena2);
         ret += dip.toString()+ " ";
      }
      return ret;
      
   }
//-------------------------------------------------------------------------------------------------------------  
 //metodo para codificar  codigo en caracteres
           
public String codificar(String descifrado){
   
       	String texto2 ="";
    int d = 0;
    char caracter=' '; 

    String [] text = descifrado.split(" ");
    for (int i=0; i < text.length; i++ ){
    d = Integer.parseInt(text[i]);  
    caracter = (char)(d);  
       texto2 += caracter ;
    }
  return texto2;      
}
  //-----------------------------------------------------------------------     
   
 // METODOS DE PROCESOS MATEMACIOS  
//--------------------------------------------
// Metodo para generar primos en modo randon, calcular phi, calcular clave publica a y clave privada b



private void generarclave(){
      SecureRandom rand = new SecureRandom();
  
      BigInteger tmp = BigInteger.probablePrime(512, rand);  //512
      while( !primo(tmp) ){
         tmp = BigInteger.probablePrime(512, rand);  //512
      }
      
      
      p = tmp;
     
      tmp = BigInteger.probablePrime(512, rand);  //512
      while( !primo(tmp) ){
         tmp = BigInteger.probablePrime(512, rand); //512
      }
      q = tmp;
      n = q.multiply(p);
      tmp = new BigInteger(100,rand);   //100
      BigInteger phiN = p.subtract(BigInteger.ONE).multiply( q.subtract(BigInteger.ONE) );
      BigInteger inv  = inverModule(tmp, phiN);
      while( inv.compareTo(new BigInteger("-1")) == 0){
         tmp = new BigInteger(128, rand);
         inv = inverModule(tmp, phiN);
      }
      a = tmp;
      b = inv;
      phinN = phiN;
   }

   //---------------------------------------------------------------------------------------------
   
  //metodo comprobar si es primo el randon generado
   private boolean primo(BigInteger p) {
      return p.isProbablePrime(0); 
   }
//-------------------------------------------------------------------------------------------------------
   // metodo para realizar el modulo inverso
   
   private BigInteger inverModule(BigInteger a,BigInteger p){
      a = a.mod(p);
      BigInteger[] sol = euclides(a,p);
      if(sol[0].compareTo(BigInteger.ONE) != 0){
         return new BigInteger("-1");
      }
      return ( sol[1].compareTo(BigInteger.ZERO) < 0 )? p.add(sol[1]) : sol[1];
   }
//-----------------------------------------------------------------------------------------------------------
   
// metodo para algoritmo extendido de euclides
   private BigInteger[] euclides(BigInteger p, BigInteger q) {
      if (q.compareTo(BigInteger.ZERO) == 0){
         return new BigInteger[] { p, BigInteger.ONE, BigInteger.ZERO };
      }
      BigInteger[] vals = euclides(q, p.mod(q));
      BigInteger d = vals[0];
      BigInteger a = vals[2];
      BigInteger b = vals[1].subtract((p.divide(q)).multiply(vals[2]));
      return new BigInteger[] { d, a, b };
   }
//-------------------------------------------------------------------------------------------------------------------------

/*    private Object charAt(int i) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    } */
}

