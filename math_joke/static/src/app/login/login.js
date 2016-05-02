angular.module('onlineLearningApp.login', [
    'ui.router',
    'ui.bootstrap',
    'ngIdle',
    'mathCommonModel'
]);

angular.module('onlineLearningApp.login').controller('LoginController',
    function LoginCtrl($scope, $rootScope, $cookieStore, $location, $q, $mdDialog, 
    UserModelFactory, $state, MathModelFactory, Idle, Keepalive, mjConstant, AppUtils, $window) {

        // <---- Session Timeout
        $rootScope.idle_started = false;

        $rootScope.$on('IdleStart', function() {
            console.log("$scope.started - ", $rootScope.idle_started);
            if (!$rootScope.idle_started) {
                $rootScope.idle_started = true;
                $mdDialog.show({
                    controller: 'LoginTimeoutController',
                    templateUrl: 'static/src/app/login/login-timeout.tpl.html'
                });
            }
            console.log("On IdleStart");
        });

        $rootScope.$on('IdleEnd', function() {
            console.log("On IdleEnd");
        });

        $rootScope.$on('IdleTimeout', function() {
            $rootScope.idle_started = false;
            $mdDialog.hide();
            Idle.unwatch();
            $rootScope.$emit(mjConstant.logout_user_session);
            console.log("On IdleTimeout");
        });

        $scope.start = function() {
            Idle.watch();
        };

        $scope.stop = function() {
            Idle.unwatch();
        };


        // ----->
        $scope.startPlacementtest = function() {

            item = {};

            $mdDialog.show({
                controller: 'StartPlacementTestController',
                templateUrl: 'static/src/app/placementtest/startPlacementTest.tmpl.html',
                //  resolve: {
                item: item
                //  }

            });
            //    .then(
            //    function(answer) {
            //        // $scope.alert = 'You said the information was "' + answer + '".';
            //
            //        if(answer=='YES'){
            //
            //
            //            console.log("  start placement test YES:");
            //          //  $rootScope.$broadcast(mjConstant.popupAfficiencySession_DialogEvent,$scope.item);
            //            // $state.go('homeafficiencyexercise', {'grade': $scope.grade});
            //        }
            //
            //        else if (answer=='NO'){
            //            console.log("go back to home ");
            //        }
            //
            //
            //    },
            //    function() {
            //        $scope.alert = 'You cancelled the dialog.';
            //    }
            //);
        };


        $scope.getAppConfig = function() {
            console.log("In appConfig() function");
            $q.all(
                [
                    MathModelFactory.getAppConfig()
                ]).then(function(response) {
                    $scope.app_config = response[0].data;
                    $window.sessionStorage.user_task_assignment_home = $scope.app_config[0].user_task_assignment_home;
                    $rootScope.$broadcast(mjConstant.math_contest_config, $scope.app_config[0].mathContestConfig);
                },
                function(error) {
                    console.log("Error in getting app_Config data on login.");
                });

            console.log('$window.sessionStorage.user_task_assignment_home: ', $window.sessionStorage.user_task_assignment_home);
        };

        $scope.init = function() {

            $scope.userPassword = '';
            $scope.userEmail = '';
            $scope.user = '';
            $scope.validUser = true;


            $scope.getAppConfig();

            console.log("in initititit");
            $("#loginbutton").keypress(function(e) {

                if ("$scope.userEmail".length == 0 || $scope.userPassword.length == 0) {
                    console.log("empty username and password");
                    return;

                }

                if (e.keyCode == 13) {
                    //   sendMessage();
                    $scope.authenticateUser($scope.userEmail, $scope.userPassword);
                    e.preventDefault();
                    return false;
                }
            });
        };


        $scope.authenticateUser = function(username, password) {
            var params = { 'username': $scope.userEmail, 'password': $scope.userPassword, 'ip': document.userip };
            $q.all([UserModelFactory.getUser(params)]).then(function(response) {
                $scope.user = response[0].data;


                console.log("  !!!!!!  get user from service", $scope.user);

                if ($scope.user === 'null') {
                    $rootScope.currentUser = {};
                    $cookieStore.remove('currentUser');
                    $scope.validUser = false;
                    $state.go('login');
                } else if (typeof $scope.user["user_expired"] != "undefined" && $scope.user["user_expired"] == true) {

                    $rootScope.currentUser = {};
                    //$cookieStore.remove('currentUser');
                    $scope.validUser = true;
                    $scope.userExpired = true;
                    var expdate = String($scope.user["expiration_date"]);
                    $scope.userExpirationDate = expdate.substring(0, expdate.indexOf("T"));
                    $state.go('login');
                } else {

                    //setup client user ip:
                    console.log("   !!!login client user ip: ", document.userip, $scope.user);
                    // $scope.user.ip=document.userip;

                    $rootScope.currentUser = $scope.user;


                    $cookieStore.put('currentUser', $rootScope.currentUser);
                    $scope.validUser = true;
                    $scope.userExpired = false;
                    $scope.$parent.isUserLogin = true;

                    $scope.start();

                    if ($scope.app_config[0].user_task_assignment_home) {
                        $state.go('home');
                    } else {
                        $state.go('homeprofile');
                    }

                    // if ($scope.app_config[0].mathContestConfig.enableMathContest) {
                    //     $rootScope.enableMathContest = $scope.app_config[0].mathContestConfig.enableMathContest;
                    //
                    //     //todo : Ling Lin, add math contest timer init here
                    //     AppUtils.initMathContestTimerRoot();
                    //
                    // }

                }

            }, function(err) {
                $state.go('login');
            });
        };
        $scope.getUser = function() {

        };
        $scope.goHome = function() {
            $state.go('home');
        };


        $scope.init();

    });