$(document).ready(function(){
    $('#regex').click(function(){ 
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
            data : {ques : $("#sender").val(), method: 'regex'},
            success : function(data){
                ans.innerHTML = data;
                $('.convo').append(ans);
            },
            cache : false
        })
    });
});

$(document).ready(function(){
    $('#kmp').click(function(){ 
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
            data : {ques : $("#sender").val(), method: 'kmp'},
            success : function(data){
                ans.innerHTML = data;
                $('.convo').append(ans);
            },
            cache : false
        })
    });
});

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
    });
});
