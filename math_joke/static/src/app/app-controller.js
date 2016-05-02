angular.module('onlineLearningApp').controller('AppController',


    ['$scope', '$location', 'mjEvents', function ($scope, $location, mjEvents) {

        $scope.isUserLogin = false;
        $scope.selectedSkill = "";

        $scope.currentGrade;


        $scope.userState = '';
        $scope.states = ('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS ' +
        'MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI ' +
        'WY').split(' ').map(function (state) {
            return {abbrev: state};
        });


        //$scope.toggleKeypadOpening =  function($event){
        //    //Toggling KeyPad Locking state, second argument is Keypad ID
        //
        //
        //    var inputboxAnswerProp=$($event.target).attr("answer-obj");
        //
        //    console.log(" app level event received...", inputboxAnswerProp,JSON.parse(inputboxAnswerProp).id);
        //
        //    $scope.$emit(  mjEvents.Keypad_TOGGLE_OPENING, JSON.parse(inputboxAnswerProp).id);
        //};


        $scope.init = function () {
            $scope.isUserLogin = false;


            //MathJax.Hub.Insert(MathJax.InputJax.TeX.Definitions.macros,{
            //    cancel: ["Extension","cancel"],
            //    bcancel: ["Extension","cancel"],
            //    xcancel: ["Extension","cancel"],
            //    cancelto: ["Extension","cancel"]
            //});

            //initialize mathjax library
            //MathJax.Hub.Config({
            //    showProcessingMessages: false,
            //    extensions: ["tex2jax.js","longdiv.js"],
            //    jax: ["input/TeX","output/HTML-CSS"],//"output/SVG",
            //    tex2jax: {
            //        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            //        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            //        processEscapes: true
            //    },
            //    skipStartupTypeset: true,
            //    "HTML-CSS": {
            //        linebreaks: { automatic: true ,width: "container"},
            //        preferredFont: "STIX",
            //        showMathMenu: true,
            //        availableFonts: ["STIX","TeX"],
            //        extensions: ["handle-floats.js"],
            //        minScaleAdjust: 50,
            //        scale: 100,
            //        matchFontHeight: true,
            //        styles: {
            //
            //        }
            //    },
            //    TeX: {
            //        extensions: ["AMSmath.js","AMSsymbols.js","cancel.js","enclose.js"],
            //        noErrors: {
            //            style: {
            //                "font-size": "10px",
            //                "border": ""
            //            }
            //        },
            //        Macros: {
            //            xspace: '',
            //            ensuremath: ''
            //
            //        }
            //    },
            //    SVG: {
            //      //  linebreaks: { automatic: true },
            //        scale: 40,
            //        minScaleAdjust: 50,
            //        styles: {
            //            "font-size": "10px",
            //            "border": ""
            //        }
            //    }
            //
            //    // TeX: {extensions: ["xypic.js"]}//"AMSmath.js","AMSsymbols.js",
            //});
            //MathJax.Hub.Config({
            //    TeX: { extensions: ["autoload-all.js"] },
            //
            //    tex2jax: {
            //        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            //        processEscapes: true
            //    }
            //
            //});
            //MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
            //MathJax.Hub.Configured();


            (function ($) {
                $.fn.getCursorPosition = function () {
                    var input = this.get(0);
                    if (!input) return; // No (input) element found
                    if ('selectionStart' in input) {
                        // Standard-compliant browsers
                        return input.selectionStart;
                    } else if (document.selection) {
                        // IE
                        input.focus();
                        var sel = document.selection.createRange();
                        var selLen = document.selection.createRange().text.length;
                        sel.moveStart('character', -input.value.length);
                        return sel.text.length - selLen;
                    }
                }
            })(jQuery);


            (function ($) {
                // Behind the scenes method deals with browser
                // idiosyncrasies and such
                $.caretTo = function (el, index) {
                    if (el.createTextRange) {
                        var range = el.createTextRange();
                        range.move("character", index);
                        range.select();
                    } else if (el.selectionStart != null) {
                        el.focus();
                        el.setSelectionRange(index, index);
                    }
                };

                // The following methods are queued under fx for more
                // flexibility when combining with $.fn.delay() and
                // jQuery effects.

                // Set caret to a particular index
                $.fn.caretTo = function (index, offset) {
                    return this.queue(function (next) {
                        if (isNaN(index)) {
                            var i = $(this).val().indexOf(index);

                            if (offset === true) {
                                i += index.length;
                            } else if (offset) {
                                i += offset;
                            }

                            $.caretTo(this, i);
                        } else {
                            $.caretTo(this, index);
                        }

                        next();
                    });
                };

                // Set caret to beginning of an element
                $.fn.caretToStart = function () {
                    return this.caretTo(0);
                };

                // Set caret to the end of an element
                $.fn.caretToEnd = function () {
                    return this.queue(function (next) {
                        $.caretTo(this, $(this).val().length);
                        next();
                    });
                };
            }(jQuery));


        };

        $scope.test = function () {
            $scope.isUserLogin = true;
        };

        $scope.init();

        $scope.$on('$stateChangeSuccess', function (event, toState, toParams, fromState, fromParams) {
            if (angular.isDefined(toState.data.pageTitle)) {
                $scope.pageTitle = 'Afficient | ' + toState.data.pageTitle;
            }
        });




    }]).filter('slice', function () {
    return function (arr, start, end) {
        if (Array.isArray(arr)) {
            return arr.slice(start, end);
        }
    };
}).config(function ($provide) {
    $provide.decorator('$state', function ($delegate, $stateParams) {
        $delegate.forceReload = function () {


            console.log(" ========= forceReload was called.....");


            //return $delegate.go($delegate.current, $stateParams, {
            //    reload: true,
            //    inherit: false,
            //    notify: true
            //});
        };
        return $delegate;
    });

});
