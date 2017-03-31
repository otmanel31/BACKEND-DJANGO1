angular.module('myApp').controller('PortionAlimentController',
    function($scope, Portionaliment, $stateParams, Aliment ){
        var oneId = parseInt($stateParams.portionId)
        $scope.portionaliment = Portionaliment.query({ aliment_id: oneId })
        $scope.aliment = Aliment.get({ id: oneId})
        console.log('all portion ', $scope.portionaliment)
        console.log("alim", $scope.aliment)
    }
)