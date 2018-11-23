import java.io.*;

/* StartPy.java
 * @Author: Andreas
 * 
 * Just looking at how would one really pass the info from a Java Program to a Python Script.
 * 
 * Will any information have to be passed back to the Listener.java program?  
 * Probably better if Listener.java is called anew each time it's...
 */

//mock Listener code, for testing on ubuntu for now
public class StartPy {
	public static void main(String[] args) throws java.io.IOException {
		System.out.println("Hi, I am a Java Program");
		
		String rc1 = "python3 nextPythonScript.py ";		//The space at the end is important!
		String rc2 = "OneWordString";		
		
		String rc = rc1+rc2;
		System.out.println(rc);
		
		try {
			//Process p = Runtime.getRuntime().exec("python3 nextPythonScript.py");					//which is better?  this			
			Runtime.getRuntime().exec(rc);						//or this?						
		}
		catch (IOException e) {
			e.printStackTrace();
		}		
	}
}
//(Problem 2of2): I can pass a String from the Java program to the Python Script, but only if the string doesn't have any spaces in it.

//Idea: Maybe we can pass an array of Strings?
