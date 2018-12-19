import java.util.regex.Matcher;
import java.util.regex.Pattern;

//solution to: https://www.hackerrank.com/challenges/strong-password/problem
public class StrongPassword{

    static int minimumNumber(int n, String password){

        //variable to be returned
        int min = 0;

        //Regexes
        String numbers = "[1-9]";
        String lower_case = "[a-z]";
        String upper_case = "[A-Z]";
        String special_chars = "[!@#$%^&*()+-]";

        //Patterns
        Pattern p_numbers = Pattern.compile(numbers);
        Pattern p_lower_case = Pattern.compile(lower_case);
        Pattern p_upper_case = Pattern.compile(upper_case);
        Pattern p_special_chars = Pattern.compile(special_chars);

        //Matchers
        Matcher m_numbers = p_numbers.matcher(password);
        Matcher m_lower_case = p_lower_case.matcher(password);
        Matcher m_upper_case = p_upper_case.matcher(password);
        Matcher m_special_chars = p_special_chars.matcher(password);

        //Conditionals
        if(!m_numbers.find()){
            System.out.println("no numbers");
            min++;
        }

        if(!m_lower_case.find()){
            min++;
        }

        if(!m_upper_case.find()){
            min++;
        }

        if(!m_special_chars.find()){
            System.out.println("no special chars");
            min++;
        }

        if(n < 6){
            min = 6 - n;
        }

        return min;

    }

    public static void main(String args[]){
        //3, "&+6"
        int x = minimumNumber(3, "&+6");
        System.out.println(x);
    }

}