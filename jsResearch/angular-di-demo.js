/*
    This demo show you how the Angular gets inject arguments from a function.

    references :
        Tero Parviainen: Build Your Own AngularJS [11:00] (https://vimeo.com/96444762)
 */

var STRIP_COMMENTS = /((\/\/.*$)|(\/\*[\s\S]*?\*\/))/mg;
var FN_ARGS = /^function\s*[^\(]*\(([^\)]*)\)/m;

//  The controller or function will be injected
function lazyGangController(/*this is scope*/  $scope,
                            /*this is root scope*/  $rootScope, $lazyGangModule) {
    // this is a controller
    console.log("This is lazy gang controller");

    /* Some comments...*/
    console.log("We are lazy gang");
}

var funString = lazyGangController.toString();
console.log("> Function string------\n", funString);

// get rid of all comments
var funString = funString.replace(STRIP_COMMENTS, '');
console.log("> Function code without comments------\n", funString);

var argStringMatch = funString.match(FN_ARGS);
console.log("> Arguments string regex match -----\n", argStringMatch);

for (var i = 0; i < argStringMatch.length; i++) {
    console.log("   > Regex match group" + i + " -----\n", argStringMatch[i]);
}

var argString = funString.match(FN_ARGS)[1];
console.log("> Arguments string-----\n", argString);

var argsTobeInject = argString.split(',').map(function (arg) {
    // remove all space
    return arg.replace(/\s*/g, '');
});

console.log("> Arguments to be injected ----\n", argsTobeInject);
