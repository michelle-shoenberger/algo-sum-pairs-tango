var sp = require("./sumPairs");

var shallowEqual = require('shallow-equal');

console.log(sp.sumPairs([1,2,3,4,5], 7))
console.log(sp.sumPairs([1,2,3,4,5], 9))
console.log(sp.sumPairs([3, 1, 5, 8, 2], 27))

console.log(shallowEqual.shallowEqualArrays(sp.sumPairs([1,2,3,4,5], 7),[[2,5], [3,4]]));
