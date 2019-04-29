$('.slider').each(function(){    // если слайдеров несколько
    let $this = $(this);
    let $group = $this.find('.slide-group');
    let $slides = $this.find('.slide');
    let currentIndex = 0;
    let timeout;
    let backButton = $this.find('#backward');
    let forButton = $this.find('#forward');
    let flipSlide = '100%';  // для текущего слайда
    let moveGroup = '-100%';  // для группы слайдов

    function moveSlides(index) {
        advance();

        if($group.is(':animated') || currentIndex === index){
            return;
        }

        $slides.eq(index).css({left: flipSlide, display: 'block'});
        $group.animate({left: moveGroup},600, function(){
            $slides.eq(currentIndex).css({display: 'none'});
            $slides.eq(index).css({left: 0});
            $group.css({left: 0});
            currentIndex = index;
        });
    }

    function advance(){
        clearTimeout(timeout);
        timeout = setTimeout(function(){
            if (currentIndex < ($slides.length - 1)){
                moveSlides(currentIndex + 1);
            }else{
                moveSlides(0);
            }
        }, 2600);
    }

    backButton.on('click',function(){
        flipSlide = '-100%';
        moveGroup = '100%';
        if (currentIndex === 0){
            moveSlides($slides.length - 1)
        }else{
            moveSlides(currentIndex - 1)
        }
        flipSlide = '100%';
        moveGroup = '-100%';
    });

    forButton.on('click',function(){
        if (currentIndex === $slides.length - 1){
            moveSlides(0)
        }else{
            moveSlides(currentIndex + 1)
        }
    });

    advance();
});
