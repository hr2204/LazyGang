describe('testContrller Test Spec', function() {
    var $rootScope, $scope, controller;

    beforeEach(function() {
        module.apply(this, Dessert.Dependencies);

        inject(function($injector) {
            $rootScope = $injector.get('$rootScope');
            $scope = $rootScope.$new();
            controller = $injector.get("$controller")("testController", { $scope: $scope })
        });
    });

    describe('Action Handlers ', function() { //describe your app name

        describe("getFullName", function() {
            it("Should get correct full name", function() {
                $scope.firstName = "lazy";
                $scope.lastName = "gang";


                $scope.getFullName();

                expect($scope.fullName).toEqual("lazy gang");
            });
        });
    });
});