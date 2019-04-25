var slides = document.getElementsByClassName("slide");
var n = 0;
forwardButton = document.getElementById("forward");
backwardButton = document.getElementById("backward");

var timerID = setInterval(moveSlides, 3000);
function moveSlides(){
    slides[n].className = "slide";
    n++;
    if (n >= (slides.length)){
        n = 0;
    }
    slides[n].className = "slide shown";
}
