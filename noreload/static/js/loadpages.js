$('nav a').on('click',null,null,function(e){
    e.preventDefault();
    var url=this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');
    $('#container-1').remove();

    $('#content').load(url+' #content').hide().fadeIn('slow');
});