var main = function(callback) {

    var para = "Lazy Gang";

    //callback.apply(this, para);
    callback(para);
}

var myCallback = function(parameter) {
    console.log("Hello", parameter);
}

var yourCallback = function(parameter) {
    console.log("Good bye", parameter);
}

// call the fn with callback as parameter
main(myCallback);

main(yourCallback);