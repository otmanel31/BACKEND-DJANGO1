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
         })
         .state('portions',{
               url: '/portions/{portionId}',
               templateUrl: 'portionaliment.view.html',
               controller: 'PortionAlimentController',
                resolve: {
                     portion : function($stateParams, Portionaliment){
                        var portionId = parseInt($stateParams.portionId, 10)
                        console.log('id p ', portionId)
                        console.log('toto', Portionaliment.get({aliment_id: portionId}))
                        return Portionaliment.get({aliment_id: portionId})
                        
                      }
               },
         });
         /*.state('portions.portion', {
               url: '/portion/{portionId}',
               templateUrl: 'portionaliment.view.html',
               controller: 'portionDetailController',
               resolve: {
                     portion : function($stateParams, Portionaliment){
                        let portionId = parseInt($stateParams.portionId, 10)
                        console.log('id p ', portionId)
                        return Portionaliment.get({aliment_id: portionId})
                        
                      }
               },
         });*/

});