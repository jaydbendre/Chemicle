function edit_user(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[1].disabled = false;
    m[2].disabled = false;
    m[3].disabled = false;
    m[4].disabled = false;
    m[5].disabled = false;
    m[6].disabled = false;
    var id = "edit_"+x;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
    $('#save_'+x).submit(
        function(){
            console.log("hi")
        }
    )
}

// $('#edit_'+x).click(
//     function(){
//         $('#save_'+x).toggle();
//         $('#edit_'+x).hide();
//     }
// )

