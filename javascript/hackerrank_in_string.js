function hackerrankInString(s) {

    let h = getDictionary("hackerrank");
    let len = Object.keys(h).length;
    let S = getDictionary(s);

    let count = 0;

    for(var key in h){
       
        if((key in S) && (h[key] <= S[key])){
             count++;
        }
    }

    if(count == len){
        return "YES"
    }
    
    return "NO";
}


function getDictionary(str){
    let dictionary = {}
    let count = 0;
    for(let i = 0; i < str.length; i++){    
        if (!([str[i]] in dictionary)){
            dictionary[str[i]] = 1;
        }else{
            dictionary[str[i]] = dictionary[str[i]] + 1;
        }
    }
    return dictionary;
};

console.log(hackerrankInString("hereiamstackerrank"));