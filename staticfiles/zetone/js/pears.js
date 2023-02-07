//fecha
const fecha = async() => {
    try{
        const response = await fetch("fecha");
        const data = await response.json();
        let dataFecha = JSON.parse(data);
        if(dataFecha.message=="Success"){
            let listaFecha = ``;
            dataFecha.fechas.forEach((fechas) =>{
                listaFecha += `<div class="parrafos">Fecha: ${fechas.fecha}</div>`;
            });
            document.getElementById('fecha').innerHTML = listaFecha;
        }
    } catch(error){
        console.error(error)
    }
};

const cantidadEmbalado = async() => {
    try{
        const response = await fetch("pears/cantidad/embalado");
        const data = await response.json();
        //console.log(data)
        let cantEmbalado = JSON.parse(data)
        //console.log(cantEmbalado)
        let cantidadEmbalado = ``;
        cantidadEmbalado = `<div class="numeros">CANTIDAD DE CAJAS EMBALADAS<br>${cantEmbalado.cantidad}</div>`;
        document.getElementById('detalle').innerHTML = cantidadEmbalado; 
        
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

//VARIEDAD
const procesoVariedad = async() => {
    try{
        const response = await fetch("pears/proceso");
        const data = await response.json();
        let procesoVariedad = JSON.parse(data)
        if (procesoVariedad.message == "Success"){
            let cantidadEmbalado = ``;
            cantidadEmbalado = `<h6>EMPAQUE PERA - PROCESANDO: ${procesoVariedad.variedad}</h6>`;
            document.getElementById('proceso').innerHTML = cantidadEmbalado;
            cargaLotes();
        }else{
            let cantidadEmbalado = ``;
            cantidadEmbalado = `<h6>EMPAQUE PERA - SIN PROCESO</h6>`;
            document.getElementById('proceso').innerHTML = cantidadEmbalado;
        }
        
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};



//LOTES DE PERA
const cargaLotes = async() => {
    limpiezaListado();
    limpiezaCantidad();
    try{
        const response = await fetch("pears/lote");
        const data = await response.json();
        //console.log(data)
        let dataLotes = JSON.parse(data)
        await tituloLotes();
        //console.log(dataLotes.message)
        if(dataLotes.message=="Success"){
            await cantidadPera();
            let listaLotes = ``;
            dataLotes.lotes.forEach((lotes) =>{
                listaLotes += `<div class="listado">${lotes.lote} &#8594; ${lotes.bins} Bins &#8594; ${lotes.hora} Hs.</div>`;
            });
            document.getElementById('listadoPera').innerHTML = listaLotes;
        }else{
            alert("No se encontraron lotes")
        }
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const cantidadPera = async() => {
    try{
        const response = await fetch("pears/cantidad/lotes");
        const data = await response.json();
        //console.log(data)
        let dataLotes = JSON.parse(data)
        //console.log(dataLotes.cantidad)
        let cantidadLotes = ``;
        cantidadLotes = `<div class="numeros">CANTIDAD DE BINS PROCESADOS<br>${dataLotes.cantidad}</div>`;
        document.getElementById('detalle').innerHTML = cantidadLotes; 
        
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const cargaInicial = async() => {
    await procesoVariedad();
};

const tituloLotes = async() => {
    document.getElementById('titulo').innerHTML = 'LOTE / PRODUCTOR - BINS EMB. - HORA';
};



//CAJAS POR CALIDAD
const cajasCalidadPera = async() => {
    limpiezaListado();
    limpiezaCantidad();
    try{
        const response = await fetch("pears/cajas/calidad");
        const data = await response.json();
        //console.log(data)
        let dataCajasCalidad = JSON.parse(data)
        //console.log(dataLotes.message)
        tituloCalidad();
        if(dataCajasCalidad.message=="Success"){
            cantidadEmbalado();
            let listaCajasCalidad = ``;
            dataCajasCalidad.cajas.forEach((cajas) =>{
                listaCajasCalidad += `<div class="listado">${cajas.calidad} &#8594; ${cajas.cantidad} Bultos</div>`;
            });
            document.getElementById('listadoPera').innerHTML = listaCajasCalidad;
        }else{
            //let listaLotes = ``;
            //listaLotes += `<div class="listado"></div>`;
            //document.getElementById('listadoPera').innerHTML = listaLotes;
            alert("No se encontraron Cajas")
        }
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const tituloCalidad = async() => {
    document.getElementById('titulo').innerHTML = 'CALIDAD - CANTIDAD DE CAJAS';
};

//CAJAS POR CALIBRE
const cajasCalibrePera = async() => {
    limpiezaListado();
    limpiezaCantidad();
    try{
        const response = await fetch("pears/cajas/calibre");
        const data = await response.json();
        //console.log(data)
        let dataCajasCalibre = JSON.parse(data)
        //console.log(dataLotes.message)
        tituloCalibre();
        if(dataCajasCalibre.message=="Success"){
            cantidadEmbalado();
            let listaCajasCalibre = ``;
            dataCajasCalibre.cajas.forEach((cajas) =>{
                listaCajasCalibre += `<div class="listado">Calibre &#8594;${cajas.calibre} &#8594; ${cajas.cantidad} Bultos</div>`;
            });
            document.getElementById('listadoPera').innerHTML = listaCajasCalibre;
        }else{
            alert("No se encontraron Cajas")
        }
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const tituloCalibre = async() => {
    document.getElementById('titulo').innerHTML = 'CALIBRE - CANTIDAD DE CAJAS';
};

//CAJAS POR CALIBRE
const cajasMarcaPera = async() => {
    limpiezaListado();
    limpiezaCantidad();
    try{
        const response = await fetch("pears/cajas/marca");
        const data = await response.json();
        //console.log(data)
        let dataCajasMarca = JSON.parse(data)
        //console.log(dataLotes.message)
        tituloMarca();
        if(dataCajasMarca.message=="Success"){
            cantidadEmbalado();
            let listaCajasMarca = ``;
            dataCajasMarca.cajas.forEach((cajas) =>{
                listaCajasMarca += `<div class="listado">${cajas.marca} &#8594; ${cajas.cantidad} Bultos</div>`;
            });
            document.getElementById('listadoPera').innerHTML = listaCajasMarca;
        }else{
            alert("No se encontraron Cajas")
        }
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const tituloMarca = async() => {
    document.getElementById('titulo').innerHTML = 'MARCA - CANTIDAD DE CAJAS';
};

//CAJAS POR ENVASE
const cajasEnvasePera = async() => {
    limpiezaListado();
    limpiezaCantidad();
    try{
        const response = await fetch("pears/cajas/envase");
        const data = await response.json();
        //console.log(data)
        let dataCajasEnvase = JSON.parse(data)
        //console.log(dataLotes.message)
        tituloEnvase();
        if(dataCajasEnvase.message=="Success"){
            cantidadEmbalado();
            let listaCajasEnvase = ``;
            dataCajasEnvase.cajas.forEach((cajas) =>{
                listaCajasEnvase += `<div class="listado">${cajas.envase} &#8594; ${cajas.cantidad} Bultos</div>`;
            });
            document.getElementById('listadoPera').innerHTML = listaCajasEnvase;
        }else{
            alert("No se encontraron Cajas")
        }
    } catch(error){
        console.error(error)
        alert("se produjo un error a procesar la solicitud")
    }
};

const tituloEnvase = async() => {
    document.getElementById('titulo').innerHTML = 'ENVASE - CANTIDAD DE CAJAS';
};

const limpiezaListado = async() => {
    let limpezaListados = ``;
    limpezaListados = `<div class=""></div>`;
    document.getElementById('listadoPera').innerHTML = limpezaListados; 
};

const limpiezaCantidad = async() => {
let limpieza = ``;
limpieza = `<div class="numeros"></div>`;
document.getElementById('detalle').innerHTML = limpieza; 
};



window.addEventListener("load", async () =>{
    await cargaInicial();
    fecha();

    comboxPera.addEventListener("change", (event) =>{
        //console.log(event);
        //console.log(event.target);
        //console.log(event.target.value);
        if(event.target.value=="cantCajasCalidad"){
            cajasCalidadPera();
        }
        if(event.target.value=="binsProcesados"){
            cargaInicial();
        }
        if(event.target.value=="cantCajasCalibre"){
            cajasCalibrePera();
        }
        if(event.target.value=="cantCajasMarca"){
            cajasMarcaPera();
        }
        if(event.target.value=="cantCajasEnvase"){
            cajasEnvasePera();
        }
    });
});