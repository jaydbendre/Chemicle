function edit_user(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    m[1].disabled = false;
    m[2].disabled = false;
    m[3].disabled = false;
    m[4].disabled = false;
    m[5].disabled = false;
    m[6].disabled = false;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
}

function edit_lab(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    m[1].disabled = false;
    m[2].disabled = false;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
}

function edit_dept(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    m[1].disabled = false;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
}

function edit_schedule(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    m[1].disabled = false;
    m[2].disabled = false;
    m[3].disabled = false;
    m[4].disabled = false;
    m[5].disabled = false;
    m[6].disabled = false;
    m[7].disabled = false;
    m[8].disabled = false;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
}

function edit_request(x){
    console.log(x);
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    m[1].disabled = false;
    m[2].disabled = false;
    m[3].disabled = false;
    m[4].disabled = false;
    m[5].disabled = false;
    $("#save_"+ x).toggle();
    $("#edit_"+ x).hide();
}

function del(x){
    var m = document.getElementsByClassName(x);
    m[0].disabled = false;
    alert("Are you sure you want to delete user with User ID : "+x)
}
// $('#edit_'+x).click(
//     function(){
//         $('#save_'+x).toggle();
//         $('#edit_'+x).hide();
//     }
// )

