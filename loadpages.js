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
    var $content = $('#content');

    $('nav a.current').removeClass('current');
    $(this).addClass('current');
    $('#container').remove();

    $.ajax({
        type:"POST",
        url:url,
        timeout:2000,
        beforeSend: function(){
            $content.append('<div id="load">Loading</div>');
        },
        complete:function(){
            $('#loading').remove();
        },
        success: function(data){
            $content.html($(data).find('#container')).hide().fadeIn(400);
        },
        fail:function(){
            $('#panel').html('<div class="loading">Please try again soon.</div>');
        }
    });
});