var staticURL = "{% static 'images/' %}";
const url = 'ws://' + window.location.host + '/ws/home/conv/';
const socket = new WebSocket(url)
const conv = document.querySelector(".conv");
let chat = document.querySelector('.chatbot');
const item1 = document.querySelector('.item1');
const newTab = document.querySelector('.new_tab');
const menu = document.querySelector('.menu');
newTab.addEventListener('click',function(e){
    const url = `ws://${window.location.host}/ws/newtab/`;
    const socket = new WebSocket(url);
    var convClone = conv.cloneNode(true);
    convClone.querySelector('.msg').textContent = "";
    convClone.querySelector('img').src = "#"
    item1.innerHTML = "";
    item1.appendChild(convClone)
    console.log("http://"+window.location.host)
    window.location.href = "http://"+window.location.host;
})
function deleteTab(event,id){
    var url = "ws://" + window.location.host + "/ws/delete/";
    const sock = new WebSocket(url);
    sock.onopen= function(){
        sock.send(JSON.stringify(id));
    }
    event.target.parentNode.parentNode.style.display = "none";

}
document.addEventListener('keydown',function(event){
    if (event.key == 'Enter'){
        const prompt = document.getElementById("prompt");
        var val = prompt.value
        data = JSON.stringify({'q':val})
        prompt.value = "";
        socket.send(data)
        if (! chat){
        chat = document.createElement("div");
        chat.className = 'chatbot';
        var img = document.createElement('img');
        img.src = "/static/images/user.png"
        chat.appendChild(img)
        let p = document.createElement("p");
        p.className = "msg";
        p.textContent = val;

        chat.appendChild(p);
        conv.appendChild(chat)
        }
        else{
            var chatClone = chat.cloneNode(true);
            var msg = chatClone.querySelector('.msg');
            msg.textContent = val;
            chatClone.querySelector("img").src = "/static/images/user.png";
            conv.appendChild(chatClone);
        }
    }
});
socket.onmessage = function(e){
    let data = JSON.parse(e.data);
    var history = document.querySelector('.history');
    history.style.display = "flex";
    if (history.querySelector('.htitle').textContent == ''){
        history.querySelector('.htitle').textContent = data['title'];
    }
    // chat = document.createElement("div");
    // chat.className = 'chatbot';
    // var img = document.createElement('img');
    // img.src = "/static/image/chatgpt.jpeg"
    // chat.appendChild(img);
    // let span = document.createElement("span");
    // span.className = "msg";
    // span.innerHTML = data['a'];
    // chat.appendChild(span);
    // conv.appendChild(chat)
        
    var chatClone = chat.cloneNode(true);
    var msg = chatClone.querySelector('.msg');
    msg.innerHTML = data['a'];
    chatClone.querySelector("img").src = "/static/images/chatgpt.jpeg";
    if (chatClone.querySelector(".msg").innerHTML != "undefined"){
        conv.appendChild(chatClone);
    }
}
