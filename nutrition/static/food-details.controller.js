angular.module('myApp').controller('FoodDetailsController',
   function($scope, food) {
      $scope.food = food;
   }
);