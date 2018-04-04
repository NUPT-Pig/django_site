

$("#account-submit").click(function(){
    var money = $("#account_money").val();
    var money1 = money
    var option = "存入";
    if (money <= 0) {alert('金额不合法'); return 0;}
    if ($("#account_option").find("option:selected").val() === '0') {money = -money; option = "支出";}
    var json_data = {"money": money, "comment": $("#account_comment").val(), "date": $("#account_date").val()};
    var result = confirm(option + " : " + money1);
    if (result === false) {return 0;}

    var formData = new FormData();
    var img_file = document.getElementById("img_file");
    var fileobj = img_file.files[0];

    formData.append("img", fileobj);
    formData.append("account_detail", JSON.stringify(json_data));

    $.ajax({
        url: "../helpers/add_account/",
        // url: "../helpers/test/",
        type: "post",
        // contentType: "application/json",
        contentType: false,
        async: false,
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        // dataType: "json",
        // data: JSON.stringify(json_data),
        data: formData,
        processData: false,
        success: function(result, status){},
        statusCode: {
            201: function(){
                alert('提交成功');
            }
        }
    });
});