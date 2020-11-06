$(document).ready(function () {
    if (jQuery().flexslider) {
        //flexslider ticker
        $('.flexslider-ticker').each(function() {
          var tickerSettings =  {
            animation: "slide",
            animationLoop: false,
            selector: ".items > .item",
            move: 1,
            controlNav: false,
            slideshow: true,
            direction: 'vertical'
          };
          $(this).flexslider(tickerSettings);
        });
        // flexsliders
        $('.flexslider').each(function() {
          var sliderSettings =  {
            animation: $(this).attr('data-transition'),
            selector: ".slides > .slide",
            controlNav: false,
            smoothHeight: true,
            prevText: "",
            nextText: "",
            sync: $(this).data('slidernav') || '',
            start: function(slider) {
              if (slider.find('[data-slide-bg-stretch=true]').length > 0) {
                slider.find('[data-slide-bg-stretch=true]').each(function() {
                  if ($(this).data('slide-bg')) {
                    $(this).backstretch($(this).data('slide-bg'));
                    // $(this).data('slide-bg');
                  }
                });
              }
            }
          };
          
          $('html').addClass('has-flexslider');
          $(this).flexslider(sliderSettings);
        });
        $(window).delay(1000).trigger('resize'); //make sure height is right load assets loaded
    }})