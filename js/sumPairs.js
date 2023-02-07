exports.sumPairs = function(arr, num) {
  let result = [];
  let total = 0;
  // Check for input type
  if (!(arr instanceof Array)) {
    return "Not a list"
  } else if (!(typeof num === 'number')) {
    return "Not a number"
  }
  let options = {}
  for (let i=0; i<arr.length; i++) {
    if ((num - arr[i]) in options) {
      result.push([num-arr[i], arr[i]])
    }
    arr[i] in options ? options[arr[i]] += 1 : options[arr[i]] = 1
    
  }
  if (result.length == 0) {
    return "Unable to find pairs"
  }
  return result
};
