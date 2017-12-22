/**
 * Created by anshun on 17-12-22.
 */

var id = Cookies.get("id");

$("#phone_number_modify").click(function(){
    $("#phone_number").removeAttr("readonly");
});

$("#email_modify").click(function(){
    $("#email").removeAttr("readonly");
});

$("#phone_number_submit").click(function(){
    var json_data = {"phone_number": $("#phone_number").val()}
    $.ajax({
        url: "../teachers/detail/" + id + "/",
        type: "put",
        contentType: "application/json",
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

$("#email_submit").click(function(){
    var json_data = {"email": $("#email").val()}
    $.ajax({
        url: "../teachers/detail/" + id + "/",
        type: "put",
        contentType: "application/json",
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