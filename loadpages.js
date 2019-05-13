var xhr = new XMLHttpRequest();
xhr.onload = function(){
    if(xhr.status===200){
        document.getElementById('content').innerHTML=xhr.responseText;
    }
};
xhr.open('GET','tag1.html',true);
xhr.send(null);

$('nav a').on('click',function(e){
    e.preventDefault();
    let url=this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');
    $('#container').remove();

    $('#content').load(url+' #content');
});