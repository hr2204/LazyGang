var app = angular.module('testApp', []);
app.controller('testController', function($scope) {
    $scope.firstName = "";
    $scope.lastName = "";
    $scope.fullName = "";
    
    
    $scope.getFullName = function()
    {
        $scope.fullName = $scope.firstName + " " + $scope.lastName;
    }
});