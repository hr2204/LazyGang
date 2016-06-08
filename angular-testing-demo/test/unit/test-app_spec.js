describe('testContrller Test Spec', function() {
    var $rootScope, $scope, controller;

    beforeEach(module('testApp'));
    var $controller;

    beforeEach(inject(function(_$controller_){
    // The injector unwraps the underscores (_) from around the parameter names when matching
        $controller = _$controller_;
    }));

    describe('Action Handlers ', function() { //describe your app name

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