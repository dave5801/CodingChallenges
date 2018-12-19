function getRansom(magazine, ransom){
    let m = getDictionary(magazine);
   
    let r = getDictionary(ransom);
    
    for (var key in r) {

        if(r[key] > m[key]){
            return "No";
        }
    }
        return "Yes";
}

function getDictionary(magazine){
    let dictionary = {}
    let count = 0;
    for(let i = 0; i < magazine.length; i++){    
        if (!([magazine[i]] in dictionary)){
            dictionary[magazine[i]] = 1;
        }else{
            dictionary[magazine[i]] = dictionary[magazine[i]] + 1
        }
    }
    return dictionary;
};

s1 = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".split(" ");
s2 = "elo lxkvg bg mwz clm w".split(" ");


console.log(getRansom(s1,s2));