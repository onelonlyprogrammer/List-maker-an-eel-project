function output_text(func_arg, item_arg) {

    let output = document.getElementById("output");
    if (func_arg == "retrive") {
        eel.get_item(0, item_arg)(function (ret) {
            console.log(ret);
            output.innerHTML = "";
            if (item_arg == "all") {
                for (r = 0; r < ret.length; r++) {
                    console.log(r);
                    output.innerHTML += ret[r][0] + ", " + ret[r][1] + ", $" + ret[r][2] + "<br>";
                }
            }
            else {
                for (r = 0; r < ret.length; r++){
                    if (r == 2){
                        output.innerHTML += "$"
                    }
                    output.innerHTML += ret[r] + ", ";
                }
            }
        });
    }
    else if (func_arg == "add_item") {
        var new_item = item_arg.split(" ");
        eel.get_item(1, new_item)(function (ret) {
            console.log(ret);
            if (ret) {
                output.innerHTML = ret;
            }
        });
    }
    else if (func_arg == "delete") {
        eel.get_item(2, item_arg)(function (ret) {
            console.log(ret);
            output.innerHTML = "Deleted " + ret;
        });
    }
    else if(func_arg == "get_total"){
        var new_item = item_arg.split(" ");
        eel.get_item(3, new_item)(function (ret){
            console.log(ret)
            output.innerHTML = ret;

        });
    }

}