$('section.awSlider .carousel').carousel({
	pause: "hover",
  interval: 4000
});

$('section.awSlider .carousel').on('slid.bs.carousel', function () {
 var bscn = $(this).find('.item.active > img').attr('src');
	$('section.awSlider > img').attr('src',bscn);
});

$(document).ready(function() {
	$(".description").hide();

  	var val_data = {
	    "val1": "Значение 1",
	    "val2": "Значение 2",
	    "val3": "Значение 3",
	    "val4": "Значение 4",
	    "val5": "Значение 5"
  	};

  	var ingredients_menu = [
	  	['[name="choose_cousine"]', ["<a href='javascript:void(0);'><span class='open'>Кухня</span><span class='value'></span></a>"],{"first": "1", "second": "2", "third": "3"}],
	  	['[name="choose_menu"]', ["<a href='javascript:void(0);'><span class='open'>Меню</span><span class='value'></span></a>"],{"first": "1", "second": "2", "third": "3"}],
	  	['[name="choose_category"]', ["<a href='javascript:void(0);'><span class='open'>Категория</span><span class='value'></a>"],{"first": "1", "second": "2", "third": "3"}],
	  	['[name="choose_dish"]', ["<a href='javascript:void(0);'><span class='open'>Блюдо</span><span class='value'></span></a>"],{"first": "1", "second": "2", "third": "3"}]
	];


  	$(".1s a").on('click', function() {
    	$(".1s ul").slideToggle('medium');
  	});

  	$(".0s a").on('click', function() {
    	$(".0s ul").slideToggle('medium');
    	$(".0s a").toggleClass("white-bg");
  	});

  	$(".2s a").on('click', function() {
    	$(".2s ul").slideToggle('medium');
    	$(".2s a").toggleClass("white-bg");
  	});

  	$(".3s a").on('click', function() {
    	$(".3s ul").slideToggle('medium');
    	$(".3s a").toggleClass("white-bg");
  	});

  	$(".2n ul").hide();

  	$(".1n").hover( function() {
    	$(".1n ul").slideToggle('medium');
  	} , function() {
  		$(".1n ul").slideToggle("medium", function() {
  			$(".1n ul").hide();
  		});
  	});

  	$(".2n").hover( function() {
    	$(".2n ul").slideToggle('medium');
  	} , function() {
  		$(".2n ul").slideToggle("medium", function() {
  			$(".2n ul").hide();
  		});
  	});

  	$(".3n").hover( function() {
    	$(".3n ul").slideToggle('medium');
  	} , function() {
  		$(".3n ul").slideToggle("medium", function() {
  			$(".3n ul").hide();
  		});
  	});

  	$(".recipe_block").hover( function() {
  		$(".recipe_block p").addClass("active1");
    	$(".active1").slideToggle('medium');
  	});


});

document.addEventListener("DOMContentLoaded", function() {
	//The first argument are the elements to which the plugin shall be initialized
	//The second argument has to be at least a empty object or a object with your desired options
	OverlayScrollbars(document.querySelectorAll("body"), { });
});
