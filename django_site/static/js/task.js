var max_len = 3;

var base_task_url = "../tasks/";

function add_task_td(element_tr, show_data) {
    element_tr.append("<td hidden>" + show_data.id +"</td>");
    var $td=$("<td></td>");
    var $a=$("<a class='un_clicked'></a>");
    $a.attr("id", show_data.id);
    $a.text(show_data.name);
    $td.append($a);
    element_tr.append($td);
    element_tr.append("<td>" + show_data.finish_time +"</td>");
    element_tr.append("<td>" + show_data.level +"</td>");
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