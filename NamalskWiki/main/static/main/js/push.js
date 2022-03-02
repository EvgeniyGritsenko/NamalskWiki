// создать всплывающее окно об том что сообщение автору отправлено
done = document.getElementById("done");
all = document.getElementsByClassName("all");

function Done(text){
    done.style.opacity = "1.0";
}

function CancelDone(){
    done.style.opacity = "0.0";
}
