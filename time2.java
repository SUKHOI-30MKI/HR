import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class time2 {

    static String timeConversion(String s) {
        // Complete this function
	String add = "00";
	if(s.contains("PM")){
			String a  = s.substring(0,2);
			String can = s.substring(2,8);
			int b  = Integer.parseInt(a);
			
			//System.out.println(b);
			int ans = b+12;
			String b1 = Integer.toString(ans);
			String nw = b1.concat(can);
			return nw;
			}
else{
	if(s.contains("12")){
				String can1 = s.substring(2,8);
				String rep = add.concat(can1);
				return rep;
				}

		else{
			String can2 = s.substring(0,8);
			return can2;
		}
}
	
	    }
	public static void main(String[] args) {
        	Scanner in = new Scanner(System.in);
        	String s = in.next();
        	String result = timeConversion(s);
        	System.out.println(result);
    }
}

