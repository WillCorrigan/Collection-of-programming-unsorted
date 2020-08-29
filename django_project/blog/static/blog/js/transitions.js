$("nav a").on("click", function (event){

    event.preventDefault()

    const href = $(this).attr("href")

    window.history.pushState(null, null, href)

    $("nav a").removeClass("active")
    $(this).addClass("active")


    $.ajax({

        url: href,
        success: function (data) {

            $("#qtest").slideUp(250, function() {


                const newPage = $(data)


                $("#qtest").html(newPage)

                $("#qtest").fadeIn(250).html()





            })



        }



    })





})