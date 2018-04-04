
var base_account_detail_url = "../helpers/account_detail/";

function load_account(){
    var account_id = $(".detail_clicked", window.opener.document).text();
    $(".detail_clicked", window.opener.document).attr("class", "un_clicked");
    base_account_detail_url = base_account_detail_url + account_id + "/";
    $.getJSON(base_account_detail_url, function(data, status) {
        if(status === "success"){
            $("#account_id").val(data.id);
            $("#account_date").val(data.date);
            $("#account_comment").val(data.comment);
            $("#account_username").val(data.username);
            $("#account_money").val(data.money);
            $("#account_file").attr("src", data.file);
            $("#account_file_href").attr("href", data.file);
            if (data.valid) {
                $("#account_check").hide();
            }
        }
    });
}

$("#account_delete").click(function(){
    var result = confirm("确定删除此记录吗？");
    if (result === false) {return 0;}
    $.ajax({
            url: base_account_detail_url,
            type: "delete",
            contentType: "application/json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
            dataType: "json",
            success: function(result, status){},
            statusCode: {
                204: function(){
                    alert('删除成功');
                    window.close();
                }
            }
        });
});

$("#account_check").click(function(){
    var result = confirm("确定通过审核吗？");
    if (result === false) {return 0;}
    $.ajax({
            url: base_account_detail_url,
            type: "patch",
            contentType: "application/json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
            dataType: "json",
            data: JSON.stringify({"valid": true}),
            success: function(result, status){},
            statusCode: {
                200: function(){
                    alert('审核成功');
                }
            }
        });
});