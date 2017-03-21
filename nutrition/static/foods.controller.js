angular.module('myApp').controller('FoodsController',
   function($scope, Aliment) {

      $scope.aliments = Aliment.query({ });

   }
);