$(document).ready(function () {
        $('.input_text').keydown(function () {

            var text = $('.input_text').val()
            if (text == '') {

                $('.modal-header').removeClass('active')
                $('.panel-heading').removeClass('active')

            } else {

                                        // $('.modal-header').addClass('active')
            }


        });



         $('.submit_button').click(function () {



            // var text = ;



            $.post('http://10.127.197.120:8000/genre/lyrics/ ',{'lyrics':$('.input_text').val()},function (data) {

                var result = data['result'];
                for (x in result.splice(2)){
                        console.log(result[x]);
                    // if (result[x][0]=''){}

                        $('.'+result[x][0]).addClass('active')

                }


            })






        })



    })

