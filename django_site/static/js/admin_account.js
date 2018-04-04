var max_len = 20;
var base_account_url = "../helpers/account/";

function open_account_detail(e){
    e.setAttribute("class", "detail_clicked");
    mywindow = window.open('account_detail.html','', 'width=500, height=600');
    mywindow.focus();
}

function add_account_td($tr, data){
    var $td = $("<td><a class= 'un_clicked' onclick='open_account_detail(this)'>" + data.id + "</a></td>");
    $tr.append($td);
    $td = $("<td>" + data.date + "</td>");
    $tr.append($td);
    $td = $("<td>" + data.money + "</td>");
    $tr.append($td);
    $td = $("<td>" + data.username + "</td>");
    $tr.append($td);
}


function add_account(data){
    $.each(data.results, function() {
        var $tr = $("<tr></tr>");
        var status_dict = {
            false : "danger",
            true : "success"
        };
        $tr.attr("class", "dynamic_tr_account " + status_dict[this.valid]);
        $("#account_table").append($tr);
        add_account_td($tr, this);
    });
}


function refresh_account(){
        var options = {
        currentPage: 1,
        totalPages: 10,
        size:"normal",
        bootstrapMajorVersion: 3,
        alignment:"right",
        numberOfPages:5,
        onPageClicked: function(e, originalEvent, type, page) {
            $.getJSON(base_account_url + "?page=" + page, function(data, status){
                if(status === "success"){
                    $("tr").remove(".dynamic_tr_account");
                    add_account(data);
                }
            });
        }
    };
    $.getJSON(base_account_url, function(data, status){
        if (status === "success") {
            options["totalPages"] = Math.ceil(data.count/max_len);
            if (options["totalPages"] <= 5) {
                options["numberOfPages"] = options["totalPages"];
            }
            add_account(data);
            $("#account_paginator").bootstrapPaginator(options);  //async must set after receive response
        }
    });
}