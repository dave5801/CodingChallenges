import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

//how many years of experience with Java or C++
public class YearsOfExperience{

    static String returnMyActualYearsOfExperience() {
        Calendar cal = Calendar.getInstance();
        Date today = cal.getTime();
        cal.add(Calendar.YEAR, - 7); 
        Date roughlywhenIstartedCoding = cal.getTime();    
        
        return "This timeStamp: " + today + " minus this other timestamp, approximately: " + roughlywhenIstartedCoding;

    }

    public static void main(String[] args){


        String thatsAGoodQuestion = returnMyActualYearsOfExperience();
        System.out.println(thatsAGoodQuestion);
        System.out.println();
        System.out.println("I don't remember the exact moment when I started coding me some Java");
    }
}
