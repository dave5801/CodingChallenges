import java.util.Arrays; 
import java.lang.Math;

public class CoinChange{

    /*
    if coin < cur sum
        n = look back and add 1
        p = loop upwards 1 space
        take min of n,p

    if coin > cur sum
        look up 1 space

    if coin % curr sum ==0
        look back coin spaces, and add 1

    return last element in int[][] coins

    */

    static int getSumofCoins(int[] s, int n){

        int coin_to_get = 0; 
        int p = 0;

        int[][] coins = new int[s.length][n];
        for(int i=0;i<s.length;i++){         
            int coin = s[i];//current coin   
            for(int j = 0; j < n; j++ ){
                int current_sum = j;
                if (coin < current_sum){
                    coin_to_get = coins[i][j-coin];
                    p = coins[i-1][j];


                }
                coins[i][j]=1;

               
            }
        }

        return 0;
    }


    public static void main(String[] args){
        System.out.println("Coin Change problem");
        int[] s = {1,5,6,8};
        int n = 11;

        int x = getSumofCoins(s,n);
        System.out.println(x);


    }
}