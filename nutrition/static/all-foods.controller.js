angular.module('myApp').controller('AllFoodsController', function($scope, Aliment) {
      $scope.mySearch = ''
      $scope.client_search = ''
      $scope.aliments = Aliment.query({});

      $scope.doSearch = function() {
            $scope.aliments = Aliment.query({search: $scope.mySearch})
      }

      $scope.sortBy = function(name){
            $scope.reverse = ($scope.name === name) ? !$scope.reverse : false;
            $scope.name = name;
      }
   }
);