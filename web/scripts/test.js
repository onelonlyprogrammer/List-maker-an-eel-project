function output_text (func_arg, item_arg){

    if (func_arg == "retrive"){
        eel.get_item(0, item_arg)(function(ret)
            {document.getElementById("output").innerHTML = ret[0] + ", " + ret[1] + ", $" + ret[2]
        });
    }
    else if (func_arg == "add_item"){
    eel.get_item( 1,item_arg)(function(ret) {console.log(ret)});
    }
    else if (func_arg == "delete"){
    eel.get_item(2, item_arg)(function(ret) {console.log(ret)});
    } 

}