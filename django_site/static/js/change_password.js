var change_password_url = 'management/change_password/';

$("#submit_new_password").click(function(){
    var new_password = $("#new_password").val();
    var confirm_password = $("#confirm_password").val();
    if (new_password === confirm_password)
    {
        $.ajax({
            url: change_password_url,
            type: "post",
            contentType: "application/json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
            dataType: "json",
            data: JSON.stringify({"new_password" : new_password}),
            success: function(result, status){},
            statusCode: {
                200: function(){
                    alert('密码重置成功');
                }
            }
        });
    }

});