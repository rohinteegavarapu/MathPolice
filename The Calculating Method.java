

import java.util.*;
import java.io.*;

class Main
{
  public static void main (String[]args)
  {
    Scanner keyboard = new Scanner (System.in);

      System.out.println
      ("Enter the word you would like to calculate the word value for.");
    String g = keyboard.nextLine ();
	  g = g.toLowerCase();

    long wordVal = 0;

    for (int i = 0; i < g.length (); i++)
      {
	wordVal += (long) (g.charAt (i) - 96);
      }

    System.out.println ("The word value of " + g + " is " + wordVal);

  }
}
