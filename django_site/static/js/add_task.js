/**
 * Created by anshun on 17-12-28.
 */

var base_teacher_url = "../teachers/";
var base_task_url = "../tasks/";
var create_task_url = base_task_url + "create/";
var detail_task_url = base_task_url + "detail/";
var check_teacher_url = base_teacher_url + 'check/';


$("#check_manager_bt").click(function(){
    var url = check_teacher_url + "?teacher_name=" + $("#check_manager_id").val();
    $.getJSON(url, function(data, status){
        if(status == "success"){
            $.each(data.results, function(){
                var $btn = $("<button></button>");
                $btn.text(this.username);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $btn.dblclick(function(){$(this).remove()});
                $("#manager_list").append($btn);
            });
        }
    });
});

$("#check_executor_bt").click(function(){
    var url = check_teacher_url + "?teacher_name=" + $("#check_executor_id").val();
    $.getJSON(url, function(data, status){
        if(status == "success"){
            $.each(data.results, function () {
                var $btn = $("<button></button>");
                $btn.text(this.username);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $btn.dblclick(function(){$(this).remove()});
                $("#executor_list").append($btn);
            })
        }
    });
});

$("#submit_add_task").click(function(){
    var manager_ids = [];
    $.each($("#manager_list").children(".to_server"), function(){
        manager_ids.push(Number(this.id));
    });
    var executor_ids = [];
    $.each($("#executor_list").children(".to_server"), function(){
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
            url: create_task_url,
            type: "post",
            contentType: "application/json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
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

$("#submit-modify-task").click(function(){
    var manager_ids = [];
    $.each($("#manager_list").children(".to_server"), function(){
        manager_ids.push(Number(this.id));
    });
    var executor_ids = [];
    $.each($("#executor_list").children(".to_server"), function(){
        executor_ids.push(Number(this.id));
    });
    json_data = {
        "name" : $("#task_name_id").val(),
        "managers" : manager_ids,
        "executors" : executor_ids,
        "level" : $("#add_level").find("option:selected").val(),
        "begin_time" : $("#begin_time_id").val(),
        "finish_time" : $("#finish_time_id").val(),
        "comment" : $("#comment_id").val(),
        "status" : $("#add_status").find("option:selected").val(),
    };
    //$.ajaxSetup({headers: {"X-CSRFToken": Cookies.get('csrftoken')}});
    $.ajax({
            url: detail_task_url + $("#task_id").val() +"/",
            type: "put",
            contentType: "application/json",
            dataType: "json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
            data: JSON.stringify(json_data),
            success: function(result, status){},
            statusCode: {
                200: function(){
                    alert('修改成功');
                }
            }
        });
});