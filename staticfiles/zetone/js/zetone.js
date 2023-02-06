//TOKEN
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



//pagina cargar registros
function listadoCalcHoras(){
  $.ajax({
    url:"/registros/calculo",
    type:"get",
    dataType:"json",
    success: function(response){
      console.log(response)
    },
    error: function(response){
      console.log("js")
    }
  });
}



const bultos = async ()=> {
  try {
    const response = await fetch("/json");
    const data = await response.json();
    var datos = data.legajo;
    console.log(data)
    var objetivo = document.getElementById('bultoPrueba');
    objetivo.innerHTML = datos;
  }catch(error){
    console.log(error);
  }
}


//window.onload = function(){
    //bultos();
  //setInterval('bultos()',1000);
//}

function verCalculoHoras() {
  var formCalchoras = new FormData(document.getElementById('formCalcHoras'));
  fetch("/json", {
    method: "POST",
    body: formCalchoras,
    headers: {
      "X-CSRFToken": getCookie('csrftoken'),
    }
  }).then(
    function(response){
      return response.json();      
    }
  ).then(
    function(data){
      console.log(data)
      try {
        let arrayData = JSON.parse(data);//CONVIERTE EL JSON en ARRAY
        let respuesta = document.querySelector('#tableCalHoras');
        respuesta.innerHTML = '';
        for(let i of arrayData){//RECORREMOS EL ARRAYLIST

          respuesta.innerHTML += `
          <tr>
            <td>${i.legajo}</td>
            <td>${i.nombre}</td>
            <td>${i.dia}</td>
            <td>${i.fecha}</td>
            <td>${i.f1}</td>
            <td>${i.f2}</td>
            <td>${i.f3}</td>
            <td>${i.f4}</td>
            <td>${i.hm}</td>
            <td>${i.ht}</td>
            <td>${i.ex}</td>
          </tr>
          ` 
          //console.log(i.legajo)
          //var tl = i.legajo.toString();
          //console.log(tl)
          //document.getElementById('tableLegajo').innerHTML = tl;
        }
      }catch(error){
        console.log(error);
      }
    }
  );  
}

$("#mostraCalcHoras").on("click",function(event){
  event.preventDefault();
  // resto de tu codigo
  verCalculoHoras();
});

$("#exportRegister").on("click",function(event){
  event.preventDefault();
  exportRegister();
});

function exportRegister() {
  var formCalchoras = new FormData(document.getElementById('formCalcHoras'));
  fetch("/download/register", {
    method: "POST",
    body: formCalchoras,
    headers: {
      "X-CSRFToken": getCookie('csrftoken'),
    }
  });
}


function nada(){
  try {
    //const response = await fetch("/json");
    //const data = await response.json();//CONVOERTE EL RESPONSE EN JSON
    for (let j of data){
      if (j.info == "sin Datos"){
        alert("No existen datos para esa fecha.");
      }else{
          if (j.info == "error"){
            alert("Se produjo un error al procesar la solicitud.");
          }else{
            let arrayData = JSON.parse(data);//CONVIERTE EL JSON en ARRAY
            let respuesta = document.querySelector('#tableCalHoras');
            respuesta.innerHTML = '';
            for(let i of arrayData){//RECORREMOS EL ARRAYLIST
              respuesta.innerHTML += `
              <tr>
                <td>${i.legajo}</td>
                <td>${i.nombre}</td>
                <td>${i.dia}</td>
                <td>${i.fecha}</td>
                <td>${i.f1}</td>
                <td>${i.f2}</td>
                <td>${i.f3}</td>
                <td>${i.f4}</td>
                <td>${i.hm}</td>
                <td>${i.ht}</td>
                <td>${i.ex}</td>
              </tr>
              ` 
            }
          }
        }   
      }
  }catch(error){
    console.log(error);
  }
}

