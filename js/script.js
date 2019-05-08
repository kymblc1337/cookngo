/* SLIDER MAIN PAGE */

$('section.awSlider .carousel').carousel({
	pause: "hover",
  interval: 4000
});

$('section.awSlider .carousel').on('slid.bs.carousel', function () {
 var bscn = $(this).find('.item.active > img').attr('src');
	$('section.awSlider > img').attr('src',bscn);
});

// Choosing ingredients

$(document).ready(function() {	
  // Добавляем значения
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
	  	['[name="choose_category"]', ["<a href='javascript:void(0);'><span class='open'>Категория</span><span class='value'></span></a>"],{"first": "1", "second": "2", "third": "3"}],
	  	['[name="choose_dish"]', ["<a href='javascript:void(0);'><span class='open'>Блюдо</span><span class='value'></span></a>"],{"first": "1", "second": "2", "third": "3"}]
	];

	for (var i = 0; i < ingredients_menu.length; i++) {
		var input = $(ingredients_menu[i][0]);
  
	  	var val_cont = document.createElement('div');
	  	$(val_cont).addClass("dropdown_cousine");
	  	$(val_cont).addClass(i + "s");

	  	$(val_cont).append(ingredients_menu[i][1]);

	  	var ul = document.createElement('ul');
	  	$(ul).addClass("choose_cousine_menu");
	  	for (elem in ingredients_menu[i][2]) {
	    	$(ul).append("<li><input type='checkbox' value='" + elem + "' id='" + elem + "'><label for='" + elem + "'>" + val_data[elem] + "</label></li>");
	  	}
	  	$(ul).appendTo(val_cont);

	  	$(input).after(val_cont);
	  	$(ul).hide();
	}

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





  	$('.dropdown_cousine ul input[type="checkbox"]').on('click', function() {

    var title_val = $(this).closest('.dropdown_cousine ul').find('input[type="checkbox"]').val(),
      title = $(this).val() + ", ";

    if ($(this).is(':checked')) {
      var html = '<span data-atr="' + title + '">' + title + '</span>';
      $('.value').append(html);
      $(".open").hide();
    } else {
      $('span[data-atr="' + title + '"]').remove();
    }
    
    if ($('.value').text() == "") {
      $(".open").show();
      $(input).val("");
    } else {
      $(input).val($('.value').text());
    }

  });

});