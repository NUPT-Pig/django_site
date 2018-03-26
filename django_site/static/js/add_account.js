

$("#account-submit").click(function(){
    var json_data = {"phone_number": $("#phone_number").val()}
    $.ajax({
        url: "../teachers/MyDetail/",
        type: "put",
        contentType: "application/json",
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        dataType: "json",
        data: JSON.stringify(json_data),
        success: function(result, status){},
        statusCode: {
            200: function(){
                alert('提交成功');
            }
        }
    });
});