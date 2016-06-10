describe('testContrller Test Spec', function() {
    var $rootScope, $scope, controller;

    beforeEach(module('testApp'));
    var $controller;

    beforeEach(inject(function(_$controller_){
    // The injector unwraps the underscores (_) from around the parameter names when matching
        $controller = _$controller_;
    }));

    describe('Action Handlers ', function() { //describe your app name

        describe("check correct answer", function() {
            it("Should get correct full name", function() {
                var $scope = {};
                var controller = $controller('testController', { $scope: $scope });
                $scope.firstName = getCorrectAnswerFromAnswerGenerator();
                $scope.lastName = getCorrectAnswerFromAnswerGenerator();

                $scope.getFullName();

                expect($scope.fullName).toEqual(getCorrectResultFromAnswerGenerator());
            });
        });

         describe("check worong answer", function() {
            it("Should get correct full name", function() {
                var $scope = {};
                var controller = $controller('testController', { $scope: $scope });
                $scope.firstName = getCorrectAnswerFromAnswerGenerator()+"a";
                $scope.lastName = getCorrectAnswerFromAnswerGenerator()+"b";

                $scope.getFullName();

                expect($scope.fullName).toNotEqual(getCorrectResultFromAnswerGenerator());
            });
        });

        describe("check incomplete answer", function() {
            it("Should get correct full name", function() {
                var $scope = {};
                var controller = $controller('testController', { $scope: $scope });
                $scope.firstName = "";
                $scope.lastName = null;

                $scope.getFullName();

                expect($scope.fullName).toNotEqual(-1);
            });
        });

        describe("getFullName", function() {
            it("Should get correct full name", function() {
                var $scope = {};
                var controller = $controller('testController', { $scope: $scope });
                $scope.firstName = "lazy";
                $scope.lastName = "gang";

                $scope.getFullName();

                expect($scope.fullName).toEqual("lazy gang");
            });
        });
    });
});