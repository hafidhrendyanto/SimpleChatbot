$(document).ready(function(){
    $('#bm').click(function(){ 
        var ans = document.createElement('P');
        ans.setAttribute('class','reply');
        ans.innerHTML="";
        var mess = document.createElement('P');
        mess.setAttribute('class','message');
        mess.innerHTML = $("#sender").val();
        $('.convo').append(mess);
        $.ajax({
            type : "POST",
            url : "index.php",
            datatype : 'json',
            data : {ques : $("#sender").val(), method: 'bm'},
            success : function(data){
                ans.innerHTML = data;
                $('.convo').append(ans);
            },
            cache : false
        })


        /*
        var toSend = $('input[name=text]').val();
        
        $('.convo').append("<p class='message'>" + toSend + "</p>");
        
        var toReply = $('greeting').val();
        
        $('.convo').append("<p class='reply'>" + "balesan" + "</p>");
        
        var greeting = ["Im doing ","Hello","Hi!",];
        var adjectives = ["Great","Good","Awesome","Amazing","Fantastic"];
        */
    });
});