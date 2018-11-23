import java.io.*;
/*
Taken verbatim from:
https://bytes.com/topic/python/answers/554425-passing-data-between-python-java-solved
 
On the question of: what would happen if information needs to be sent back from the Python Program to the Java Program

*/
 
class SomeJavaProgram {
	
	public static void main(String a[]) throws IOException {
		
		Process process = Runtime.getRuntime().exec("python SomePythonProgram.py hello");
		BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
		System.out.println(reader.readLine());
		reader.close();
	} 
}
