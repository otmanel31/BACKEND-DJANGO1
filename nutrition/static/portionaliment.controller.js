angular.module('myApp').controller('PortionAlimentController',
    function($scope, Portionaliment){
        $scope.portionaliment = Portionaliment.query({ aliment_id: $routeParams.portionId})
        console.log('all portion ', $scope.portionaliment)
    }
)