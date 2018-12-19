import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
//solution to: https://www.hackerrank.com/challenges/mars-exploration/problem
public class Mars{

    static int marsExploration(String s) {
        // Complete this function

        int count = 0;

        for(int i = 0; i < s.length(); i+=3){
          //  String tmp = s.charAt(i) + s.charAt(i+1) + s.charAt(i+2);
            StringBuffer tmp = new StringBuffer("");
            tmp.append(s.charAt(i));
            tmp.append(s.charAt(i+1));
            tmp.append(s.charAt(i+2));

            if(!tmp.toString().equals("SOS")){
                if(tmp.charAt(0) != 'S'){
                    count++;
                }

                if(tmp.charAt(1) != 'O'){
                    count++;
                }

                if(tmp.charAt(2) != 'S'){
                    count++;
                }
            }
        }
       
        return count;
    }

    public static void main(String[] args){
        int x = marsExploration("OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS");
        System.out.println("final count " +x);

    }
}