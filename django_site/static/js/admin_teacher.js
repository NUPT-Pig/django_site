/**
 * Created by anshun on 18-1-2.
 */
var base_teacher_url = "../teachers/";
var max_len=20;

function add_teachers_admin(data) {
    $.each(data.results, function(){
        var $tr = $("<tr></tr>");
        $tr.attr("id", this.id);
        $tr.attr("class", "dynamic_tr_content");
        $tr.append("<td><a class='teacher_unclicked_admin'>" + this.id + "</a></td>");
        $tr.append("<td>" + this.employee_id + "</td>");
        $tr.append("<td>" + this.username + "</td>");
        var $td = $("<td></td>");
        if (this.gender) {$td.text("女")} else {$td.text("男")}
        $tr.append($td);
        $tr.append("<td>" + this.department + "</td>");
        $tr.append("<td>" + this.position + "</td>");
        $("#teacher_table").append($tr);
    });
    
    $(".teacher_unclicked_admin").click(function () {
        $(this).attr("class", "teacher_clicked_admin");
        window.open("teacher_detail.html", '', 'width=500, height=600');
    });
}

function refresh_teachers(){
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
                    $("tr").remove(".dynamic_tr_content");
                    add_teachers_admin(data);
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
            add_teachers_admin(data);
            $("#teacher_paginator_admin").bootstrapPaginator(options);  //async must set after receive response
        }
    });
}