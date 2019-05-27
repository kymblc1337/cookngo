$('a.endless_more').on('click',null,null,function(e){
    e.preventDefault();
    var url=this.href;

    $('#container').remove();

    $('#content').load(url+' #content').hide().fadeIn('slow');
});