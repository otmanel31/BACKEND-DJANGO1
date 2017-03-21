var app = angular.module('myApp', []);

app.controller('CartController',
   function($scope) {

      $scope.items = [];

      $scope.remove = function(index) {
         $scope.items.splice(index, 1);
      };

      $scope.add = function() {
         $scope.items.push({title: 'Stuff', quantity: 1, price: 1.0});
          
      };
       
    $scope.total = function() {
        let total = 0
        $scope.items.forEach((item) =>{
            total += item.price * item.quantity
        })
        return total
    }
   }
);
