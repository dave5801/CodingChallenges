import java.util.Arrays; 

public class MatrixClass{

    static int[][] getArray(int[] s, int n){

        int[][] m = new int[s.length][n];
        for(int i=0;i<s.length;i++){            
            for(int j = 0; j < n; j++ ){
                m[i][j]=1;
               
            }
        }


        return m;
    }

    public static void main(String args[]){
        int[] arr = {1,2,5,6};
        int n = 10;

        int[][] matrix = getArray(arr,n);
        System.out.println(Arrays.deepToString(matrix));
    }
}