$(function () {
    $("DIV#toggle_header").on("click", function () {

        if ($("header").hasClass("red") && $("header").hasClass("green"))
            $("header").removeClass("red");
        else if (!($("header").hasClass("red") && $("header").hasClass("green")))
            $("header").addClass("green");

        if ($("header").hasClass("red")) {
            $("header").removeClass("red");
            $("header").addClass("green");
        }
        else if ($("header").hasClass("green")) {
            $("header").removeClass("green");
            $("header").addClass("red");
        }
    })
});
