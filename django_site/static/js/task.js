var max_len = 10;

var base_task_url = "../tasks/";
var detail_task_url = base_task_url + 'detail/';
var delete_task_url = base_task_url + 'delete/';
var base_teacher_url = "../teachers/";

function task_detail(e) {
    var taskId = e.id;
    $.getJSON(detail_task_url + taskId + '/', function(data, status){
        if (status == 'success') {
            $("#task_id").val(taskId);
            $(".to_server").remove();
            $("#task_name_id").val(data.name);
            $("#select_level").val(data.level);
            $("#select_status").val(data.status);
            $("#finish_time_id").val(data.finish_time);
            $("#comment_id").val(data.comment);
            $("#begin_time_id").val(data.begin_time);
            $.each(data.manager_names, function(){
                var $btn = $("<button></button>");
                $btn.text(this.name);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $btn.dblclick(function(){$(this).remove()});
                $("#manager_list").append($btn);
            });
            $.each(data.executor_names, function(){
                var $btn = $("<button></button>");
                $btn.text(this.name);
                $btn.attr('id', this.id);
                $btn.attr('class', 'to_server btn-success');
                $btn.dblclick(function(){$(this).remove()});
                $("#executor_list").append($btn);
            });
        }
    });
}

function add_task_td(element_tr, show_data) {
    var status_dict = {
        0 : "执行",
        1 : "审核",
        2 : "完成",
    };
    element_tr.append("<td hidden>" + show_data.id +"</td>");
    var $td=$("<td></td>");
    var $a=$("<a onclick='task_detail(this)'></a>");
    $a.attr("id", show_data.id);
    $a.text(show_data.name);
    $td.append($a);
    element_tr.append($td);
    element_tr.append("<td>" + show_data.finish_time +"</td>");
    element_tr.append("<td>" + status_dict[show_data.status] +"</td>");
    var $input = $("<input type='checkbox' value='' class='for_task_delete'>");
    $input.attr("id", show_data.id);
    var $div = $("<table></table>");
    $div.append($input);
    $td = $("<td align='center'></td>");
    $td.append($div);
    element_tr.append($td);
    //element_tr.append("<td align='right'><table class='checkbox'>jjjjjj<input type='checkbox' value='' aria-label='...'></table></td>");
}

function add_tasks(element_table, response_data) {
    $.each(response_data.results, function() {
        var tr_id = "task_tr_" + this.id;
        var $tr = $("<tr></tr>");
        var level_dict = {
            0 : "info",
            1 : "warning",
            2 : "danger"
        };
        $tr.attr("id", tr_id);
        $tr.attr("class", "dynamic_tr_task " + level_dict[this.level]);
        element_table.append($tr);
        add_task_td($tr, this);
    });
}

function task_paginator(element_paginator, element_table) {
    var options = {
        currentPage: 1,
        totalPages: 10,
        size:"normal",
        bootstrapMajorVersion: 3,
        alignment:"right",
        numberOfPages:5,
        onPageClicked: function(e, originalEvent, type, page) {
            $.getJSON(base_task_url + "?page=" + page, function(data, status){
                if (status == "success") {
                    $("tr").remove(".dynamic_tr_task");
                    add_tasks(element_table, data);
                }
            });
        }
    };
    $.getJSON(base_task_url, function(data, status){
        if (status == "success") {
            options["totalPages"] = Math.ceil(data.count/max_len);
            if (options["totalPages"] <= 5) {
                options["numberOfPages"] = options["totalPages"];
            }
            add_tasks(element_table, data);
            element_paginator.bootstrapPaginator(options);  //async must set after receive response
        }
    });
}

function add_task(){
    window.open('add_task.html');
}

function delete_task(){
    var task_ids = [];
    $.each($(".for_task_delete"), function(){
        if (this.checked){
            task_ids.push(Number(this.id));
        }
    });
    var json_data = {
        "task_ids" : task_ids
    };
    $.ajax({
            url: delete_task_url,
            type: "delete",
            contentType: "application/json",
            headers: {"X-CSRFToken": Cookies.get('csrftoken')},
            dataType: "json",
            data: JSON.stringify(json_data),
            success: function(result, status){},
            statusCode: {
                204: function(){
                    alert('删除成功');
                }
            }
        });
}