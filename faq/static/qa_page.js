$("button").click(function(){
   
    $(this).parent().parent().children('div').children('p').slideToggle();

  });
  (function () {
    $('.circle').on('click', function() {
      $('.bar').toggleClass('animate');
    });
    $('.plus-button').on('click', function() {
      $(this).toggleClass('animate');
    })
  })();