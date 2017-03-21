angular.module('myApp').factory('Aliment',
   function($resource) {
      return $resource('/api/aliments/:id', { id: '@id' }, {});
   }
);