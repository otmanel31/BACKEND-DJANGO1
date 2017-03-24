angular.module('myApp').factory('Portionaliment',
   function($resource) {
      return $resource('/api/portionaliments/:id', { id: '@id' }, {});
   }
);