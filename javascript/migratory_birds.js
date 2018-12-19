function migratoryBirds(n, ar) {
    let birds = getDictionary(ar);
    return Object.keys(birds).reduce(function(a, b){ return birds[a] > birds[b] ? a : b });
}

function getDictionary(ar){
    let dictionary = {}
    let count = 0;
    for(let i = 0; i < ar.length; i++){    
        if (!([ar[i]] in dictionary)){
            dictionary[ar[i]] = 1;
        }else{
            dictionary[ar[i]] = dictionary[ar[i]] + 1;
        }
    }
    return dictionary;
};



console.log(migratoryBirds(6,[1, 4, 4, 4, 5, 3]))