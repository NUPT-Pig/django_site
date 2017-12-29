/**
 * Created by anshun on 17-12-28.
 */

var base_teacher_url = "../teachers/";
var base_task_url = "../tasks/create/";
$("#check_manager_bt").click(function(){
    var url = base_teacher_url + "?teacher_name=" + $("#check_manager_id").val();
    $.getJSON(url, function(data, status){
        if(status == "success"){
            $.each(data.results, function(){
                var $btn = $("<button></button>");
                $btn.text(this.username);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $("#add_manager").append($btn);
            });
        }
    });
});

$("#check_executor_bt").click(function(){
    var url = base_teacher_url + "?teacher_name=" + $("#check_executor_id").val();
    $.getJSON(url, function(data, status){
        if(status == "success"){
            $.each(data.results, function () {
                var $btn = $("<button></button>");
                $btn.text(this.username);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $("#add_executor").append($btn);
            })
        }
    });
});

$("#submit_add_task").click(function(){
    var manager_ids = [];
    $.each($("#add_manager").children(".to_server"), function(){
        manager_ids.push(Number(this.id));
    });
    var executor_ids = [];
    $.each($("#add_executor").children(".to_server"), function(){
        executor_ids.push(Number(this.id));
    });
    json_data = {
        "name" : $("#task_name_id").val(),
        "managers" : manager_ids,
        "executors" : executor_ids,
        "level" : $("#add_level").find("option:selected").val(),
        "finish_time" : $("#finish_time_id").val()
    };
    $.ajax({
            url: base_task_url,
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(json_data),
            success: function(result, status){},
            statusCode: {
                201: function(){
                    alert('提交成功');
                }
            }
        });
});