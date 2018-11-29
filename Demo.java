// create a class (the class has a name)
// create a main method (the main method is standardized in Java)
// within the main method some code is executed

public class Demo {
	public static void main(String[] args) {
		
		// the classic print statement
		System.out.println("Hello World!");
		
		// declare and initialize an Integer
		int range = 100;
		
		// a simple for loop 
		for (int i = 0; i < range; i++) {
			System.out.println(i);
		}
		
		// a simple while loop
		int j = 10;
		while (j > 1) {
			System.out.println(j);
			j++;
		}
		
		int x=0;	//needed so that the code could compile...
		// our if/else if/else Statement (several recordings of this exist already)		
		if (x > 0) {
			System.out.println("positive");
		}	
		else if (x == 0) {
			System.out.println(" x = 0 ");
		}
		else {
			System.out.print("negative");
		}		
	}
}




/*

// From: https://www.cs.utexas.edu/~scottm/cs307/codingSamples.htm
// Geoni's unneccessary overly ambitious easter egg:
public static void bubblesort(int[] list) {

	assert list != null : "failed precondition";

	int temp;
	boolean changed = true;
	for (int i = 0; i < list.length && changed; i++) {
		changed = false;
		for (int j = 0; j < list.length - i - 1; j++) {
			assert (j > 0) && (j + 1 < list.length) : "loop counter j " + j + "is out of bounds.";
			if (list[j] > list[j+1]) {
				changed = true;
				temp = list[j + 1];
				list[j + 1] = list[j];
				list[j] = temp;
			}
		}
	}
	assert isAscending( list );
}

*/
