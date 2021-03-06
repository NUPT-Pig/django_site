/**
 * Created by anshun on 17-12-21.
 */

var max_len = 10;

var base_teacher_url = "../teachers/";
var delete_task_url = base_task_url + "delete/";

var de_dict = new Array();
de_dict["UN"] = "未录入";
de_dict["CS"] = "计算机";
de_dict["PHY"] = "物理";

var po_dict = new Array();
po_dict["UN"] = "未录入";
po_dict["TE"] = "教师";

function detail_click_teacher(e) {
    var id_clicked = "#" + e.id;
    $(id_clicked).attr("class", "detail_clicked");
    window.open('teacher_detail.html');
}

function add_teacher_td(element_tr, show_data) {
    element_tr.append("<td hidden>" + show_data.id +"</td>");
    element_tr.append("<td><a onclick='detail_click_teacher(this)' class='un_clicked' id=" + show_data.id + ">" + show_data.employee_id +"</a></td>");
    element_tr.append("<td>" + show_data.username +"</td>");
    element_tr.append("<td>" + de_dict[show_data.department] +"</td>");
    element_tr.append("<td>" + po_dict[show_data.position] +"</td>");
}

function add_teachers(element_table, response_data) {
    $.each(response_data.results, function(){
                var tr_id = "teacher_tr_" + this.id;
                element_table.append("<tr class='dynamic_tr_teacher'" + "id=" + tr_id +"></tr>");
                add_teacher_td($("#"+tr_id), this);
            });
}


function teammate_paginator(element_paginator, element_table) {
    var options = {
        currentPage: 1,
        totalPages: 10,
        size:"normal",
        bootstrapMajorVersion: 3,
        alignment:"right",
        numberOfPages:5,
        //pageUrl: function (type, page, current) {
        //    return "../" + "teachers/" + "?page=" + page
        //},
        onPageClicked: function(e, originalEvent, type, page) {
            $.getJSON(base_teacher_url + "?page=" + page, function(data, status){
                if(status == "success"){
                    $("tr").remove(".dynamic_tr_teacher");
                    add_teachers(element_table, data);
                }
            });
        }
    };
    $.getJSON(base_teacher_url, function(data, status){
        if (status == "success") {
            options["totalPages"] = Math.ceil(data.count/max_len);
            if (options["totalPages"] <= 5) {
                options["numberOfPages"] = options["totalPages"];
            }
            add_teachers(element_table, data);
            element_paginator.bootstrapPaginator(options);  //async must set after receive response
        }
    });
}

