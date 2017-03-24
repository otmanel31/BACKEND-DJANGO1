angular.module('myApp').controller('portionDetailController',
   function($scope, portionaliment) {
      $scope.portionaliment = portionaliment
        console.log(portionaliment)   ;
       /* $scope.portionaliment = Portionaliment.query({
        aliment_id: portionaliment
     })*/

   }
);