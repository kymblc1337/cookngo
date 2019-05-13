let xhr1 = new XMLHttpRequest();
xhr1.open('GET','tag1.html',true);
xhr1.send(null);
xhr.onload = function() { alert( this.responseText ); };
xhr.onerror = function() { alert( 'Ошибка ' + this.status ); };
xhr.send();

let xhr2 = new XMLHttpRequest();
xhr2.open('GET','tag2.html',true);
xhr2.send(null);
xhr.onload = function() { alert( this.responseText ); };
xhr.onerror = function() { alert( 'Ошибка ' + this.status ); };
xhr.send();

let xhr3 = new XMLHttpRequest();
xhr3.open('GET','tag3.html',true);
xhr3.send(null);
xhr.onload = function() { alert( this.responseText ); };
xhr.onerror = function() { alert( 'Ошибка ' + this.status ); };
xhr.send();

$('nav a').on('click',null, null,function(e){
    e.preventDefault();
    var url=this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');
    $('#container').remove();

    $('#content').load(url);
});