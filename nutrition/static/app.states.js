appModule.config(function ($urlRouterProvider, $stateProvider) {

      $urlRouterProvider.otherwise('/foods');

      $stateProvider

         .state('foods', {
            url: '/foods',
            templateUrl: 'foods.view.html',
            controller: 'FoodsController',
         })

         .state('foods.food', {
            url: '/food/{foodId}',
            templateUrl: 'food-details.view.html',
            controller: 'FoodDetailsController',
            resolve: {
               food: function ($stateParams, Aliment) {
                  var foodId = parseInt($stateParams.foodId, 10);
                  return Aliment.get({ id: foodId });
               },
            },
         });
      /*.state('meal', {
               url: '/meal',
               templateUrl: 'meal.view.html',
               controller: 'MealController', 
         });
*/
      

});