document.addEventListener(
    "DOMContentLoaded",
    function() {
      var today = new Date(),
        year = today.getFullYear(),
        month = today.getMonth(),
        monthTag = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"
        ],
        day = today.getDate(),
        days = document.getElementsByTagName("td"),
        selectedDay,
        setDate,
        daysLen = days.length;
      // options should like '2014-01-01'
      function Calendar(selector, options) {
        this.options = options;
        this.draw();
      }
  
      Calendar.prototype.draw = function() {
        this.getCookie("selected_day");
        this.getOptions();
        this.drawDays();
        var that = this,
          reset = document.getElementById("reset"),
          pre = document.getElementsByClassName("pre-button"),
          next = document.getElementsByClassName("next-button");
  
        pre[0].addEventListener("click", function() {
          that.preMonth();
        });
        next[0].addEventListener("click", function() {
          that.nextMonth();
        });
        reset.addEventListener("click", function() {
          that.reset();
        });
        while (daysLen--) {
          days[daysLen].addEventListener("click", function() {
            that.clickDay(this);
          });
        }
      };
  
      Calendar.prototype.drawHeader = function(e) {
        var headDay = document.getElementsByClassName("head-day"),
          headMonth = document.getElementsByClassName("head-month");
  
        e ? (headDay[0].innerHTML = e) : (headDay[0].innerHTML = day);
        headMonth[0].innerHTML = monthTag[month] + " - " + year;
      };
  
      Calendar.prototype.drawDays = function() {
        var startDay = new Date(year, month, 1).getDay(),
          //      下面表示这个月总共有几天
          nDays = new Date(year, month + 1, 0).getDate(),
          n = startDay;
        //      清除原来的样式和日期
        for (var k = 0; k < 42; k++) {
          days[k].innerHTML = "";
          days[k].id = "";
          days[k].className = "";
        }
  
        for (var i = 1; i <= nDays; i++) {
          days[n].innerHTML = i;
          n++;
        }
  
        for (var j = 0; j < 42; j++) {
          if (days[j].innerHTML === "") {
            days[j].id = "disabled";
          } else if (j === day + startDay - 1) {
            if (
              (this.options &&
                month === setDate.getMonth() &&
                year === setDate.getFullYear()) ||
              (!this.options &&
                month === today.getMonth() &&
                year === today.getFullYear())
            ) {
              this.drawHeader(day);
              days[j].id = "today";
            }
          }
          if (selectedDay) {
            if (
              j === selectedDay.getDate() + startDay - 1 &&
              month === selectedDay.getMonth() &&
              year === selectedDay.getFullYear()
            ) {
              days[j].className = "selected";
              this.drawHeader(selectedDay.getDate());
            }
          }
        }
      };
  
      Calendar.prototype.clickDay = function(o) {
        var selected = document.getElementsByClassName("selected"),
          len = selected.length;
        if (len !== 0) {
          selected[0].className = "";
        }
        console.log(year, month, o.innerHTML);
        o.className = "selected";
        selectedDay = new Date(year, month, o.innerHTML);
        this.drawHeader(o.innerHTML);
        this.setCookie("selected_day", 1);
        var date_set = document.getElementById("timeline");
        data_set_len = date_set.length;
        if (data_set_len !== 0) {
          date_set.innerHTML =
            "<h4 class = 'text-dark'>Timeline of " +
            o.innerHTML +
            " " +
            monthTag[month] +
            year +
            "</h4>";
          jQuery(function($) {
            $("#timeline-spinner").show();
            $.post(
              " http://127.0.0.1:8000/get_schedule_details",
              {
                date: year + "-" + (month + 1) + "-" + o.innerHTML
              },
              function(data, status) {
                console.log(data);
                $("#timeline-spinner").hide();
                var html_data = "";
                if (data["error"] != null) {
                  $("#timelineArea").html(
                    "<div class = 'container text-center'><h6 class = 'text-dark text-center'> " +
                      data["error"] +
                      "</h6></div>"
                  );
                } else {
                  $.each(data, function(i, d) {
                    console.log(d["event_type"]);
                    if (d["event_type"] === 0) {
                      html_data +=
                        '<div class="timeline-task">\
                  <div class="icon bg1">\
                    <i class="fa fa-envelope"></i>\
                  </div>\
                  <div class="tm-title">\
                    <h4>' +
                        d["title"] +
                        '</h4>\
                    <span class="time"><i class="ti-time"></i>' +
                        d["start_time"] +
                        " - " +
                        d["end_time"] +
                        "</span>\
                  </div>\
                  <p>\
                    " +
                        d["description"] +
                        "\
                  </p>\
                </div> ";
                    } else if (d["event_type"] === 1) {
                      html_data +=
                        '<div class="timeline-task">\
                  <div class="icon bg2">\
                    <i class="fa fa-exclamation-triangle"></i>\
                  </div>\
                  <div class="tm-title">\
                    <h4>' +
                        d["title"] +
                        '</h4>\
                    <span class="time"><i class="ti-time"></i>' +
                        d["start_time"] +
                        " - " +
                        d["end_time"] +
                        "</span>\
                  </div>\
                  <p>\
                    " +
                        d["description"] +
                        "\
                  </p>\
                </div> ";
                    } else {
                      html_data +=
                        '<div class="timeline-task">\
                  <div class="icon bg3">\
                    <i class="fa fa-bomb"></i>\
                  </div>\
                  <div class="tm-title">\
                    <h4>' +
                        d["title"] +
                        '</h4>\
                    <span class="time"><i class="ti-time"></i>' +
                        d["start_time"] +
                        " - " +
                        d["end_time"] +
                        "</span>\
                  </div>\
                  <p>\
                    " +
                        d["description"] +
                        "\
                  </p>\
                </div> ";
                    }
                  });
  
                  $("#timelineArea").html(html_data);
                }
              }
            );
          });
        }
      };
  
      Calendar.prototype.preMonth = function() {
        if (month < 1) {
          month = 11;
          year = year - 1;
        } else {
          month = month - 1;
        }
        this.drawHeader(1);
        this.drawDays();
      };
  
      Calendar.prototype.nextMonth = function() {
        if (month >= 11) {
          month = 0;
          year = year + 1;
        } else {
          month = month + 1;
        }
        this.drawHeader(1);
        this.drawDays();
      };
  
      Calendar.prototype.getOptions = function() {
        if (this.options) {
          var sets = this.options.split("-");
          setDate = new Date(sets[0], sets[1] - 1, sets[2]);
          day = setDate.getDate();
          year = setDate.getFullYear();
          month = setDate.getMonth();
        }
      };
  
      Calendar.prototype.reset = function() {
        month = today.getMonth();
        year = today.getFullYear();
        day = today.getDate();
        this.options = undefined;
        this.drawDays();
      };
  
      Calendar.prototype.setCookie = function(name, expiredays) {
        if (expiredays) {
          var date = new Date();
          date.setTime(date.getTime() + expiredays * 24 * 60 * 60 * 1000);
          var expires = "; expires=" + date.toGMTString();
        } else {
          var expires = "";
        }
        document.cookie = name + "=" + selectedDay + expires + "; path=/";
      };
  
      Calendar.prototype.getCookie = function(name) {
        if (document.cookie.length) {
          var arrCookie = document.cookie.split(";"),
            nameEQ = name + "=";
          for (var i = 0, cLen = arrCookie.length; i < cLen; i++) {
            var c = arrCookie[i];
            while (c.charAt(0) == " ") {
              c = c.substring(1, c.length);
            }
            if (c.indexOf(nameEQ) === 0) {
              selectedDay = new Date(c.substring(nameEQ.length, c.length));
            }
          }
        }
      };
      var calendar = new Calendar();
    },
    false
  );
  