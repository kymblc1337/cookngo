$('.slider').each(function(){    // если слайдеров несколько
    let $this = $(this);
    let $group = $this.find('.slide-group');
    let $slides = $this.find('.slide');
    let currentIndex = 0;
    let timeout;

    function moveSlides(index) {
        let flipSlide = '100%';  // для текущего слайда
        let moveGroup = '-100%';  // для группы слайдов
        advance();

        if($group.is('.animated') || currentIndex === index){
            return;
        }

        $slides.eq(index).css({left: flipSlide, display: 'block'});
        $group.animate({left: moveGroup}, function(){
            $slides.eq(currentIndex).css({display: 'none'});
            $slides.eq(index).css({left: 0});
            $group.css({left: 0});
            currentIndex = index;
        });
    };

    function advance(){
        clearTimeout(timeout);
        timeout = setTimeout(function(){
            if (currentIndex < ($slides.length - 1)){
                moveSlides(currentIndex + 1);
            }else{
                moveSlides(0);
            }
        }, 3000);
    }

    advance();
});
