$(function(){
  var $filterSelect = $('#FilterSelect'),
      $sortSelect = $('#SortSelect'),
      $container = $('#Container');
  
  $container.mixItUp();
  
  $filterSelect.on('change', function(){
    $container.mixItUp('filter', this.value);
  });
  
  $sortSelect.on('change', function(){
    $container.mixItUp('sort', this.value);
  });
});