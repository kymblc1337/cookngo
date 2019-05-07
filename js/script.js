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

  var input = $('[name="choose_cousine"]');
  
  // Создаем общий блок с классом
  var val_cont = document.createElement('div');
  $(val_cont).addClass("dropdown_cousine");

  // Создаем кнопку открытия списка и поле для записи значений
  $(val_cont).append("<a href='javascript:void(0);'><span class='open'>Кухня</span><span class='value'></span></a>");

  // Создаем выпдающий список и вкладываем в общий блок
  var ul = document.createElement('ul');
  $(ul).addClass("choose_cousine_menu");
  for (elem in val_data) {
    $(ul).append("<li><input type='checkbox' value='" + elem + "' id='" + elem + "'><label for='" + elem + "'>" + val_data[elem] + "</label></li>");
  }
  $(ul).appendTo(val_cont);
  $(ul).hide();

  // Размещаем общий блок после нужного input-а
  $(input).after(val_cont);

  // Скрываем/открываем выпадающий список
  $(".dropdown_cousine a").on('click', function() {
    $(".dropdown_cousine ul").slideToggle('fast');
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