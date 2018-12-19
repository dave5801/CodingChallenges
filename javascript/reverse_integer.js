var reverse = function(x) {

    x = reduce_number(x);
    var digits = (""+x).split("");
    var ret = []
    if(digits[0] == '-'){
        tmp = reverse_helper(digits.slice(1))
        return tmp-tmp-tmp;
    }else{
        return reverse_helper(digits);
    }
   
};

var reduce_number = function(x){
     while(x!=0){

        if(x%10 == 0){
            x = x/10;
        }else if(x%10 != 0){
            break;
        }
    }

    return x;
}

function reverse_helper(digits){
    if(digits.length == 2){
        var tmp = digits[0];
        digits[0] = digits[1];
        digits[1] = tmp;
    }else{
        for(var i = 0; i < digits.length/2-1; i++){
        var tmp = digits[i];
        digits[i] = digits[digits.length-1-i];
        digits[digits.length-1-i] = tmp;
    }
    }

  return parseInt(digits.join(''));

}

console.log(reverse(1534236469));