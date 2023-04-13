function esperarInformacion(elemento, intervalo, callback) {
    const intervalId = setInterval(() => {
    try{
        if (elemento.textContent) {
          clearInterval(intervalId);
          callback();
        }
    }catch{
        clearInterval(intervalId);
        callback();
    }
    }, intervalo);
  }
if (editar){
        let tipo_servicios = document.getElementById('id_tipo_servicio')
        if(tipo_servicios != null){
            esperarInformacion(tipo_servicios, 1000, function(){
                for (let p = 0; p < tipo_servicios.childNodes.length; p++){
                    if(tipo_servicios.children[p].value == datosRegistro['tipoServicio']){
                        tipo_servicios.children[p].selected = true;
                    }
                }
            });
        }
        document.getElementById('botonGuardar').innerHTML = "Editar"
        document.getElementById('id_inicioClase').value = datosRegistro['inicioClase']
        let picadero = document.getElementById('id_picadero')
        for(let i = 0; i < picadero.children.length; i++){
            if(picadero.children[i].value == datosRegistro['picadero'].id){
                picadero.children[i].selected = true
            }
        }
        posicion = 0
        for (let i = 0; i < datosRegistro['horario'].length; i++){
            horario = datosRegistro['horario'][i]
            const event = new Event('change')
            if (esporadico){
                agregarHoras(true)
                contHorario = document.getElementById('horarios')
                div = contHorario.children[i]
                try {
                    inputs = div.querySelectorAll('input')
                    inputs[0].value = horario['dia']
                    inputs[0].dispatchEvent(event)
                    inputs[1].value = horario['hora']
                    inputs[1].dispatchEvent(event)
                    profesor = div.lastElementChild.firstElementChild
                    new Promise((resolve, reject) =>{
                        esperarInformacion(profesor, 1000, function(){
                            for (let p = 0; p < profesor.childNodes.length; p++){
                                if(profesor.children[p].value == horario['profesor']){
                                    profesor.children[p].selected = true;
                                }
                            }
                        });
                        setTimeout(function() {
                            resolve(true)
                        }, 1000);
                    }).then(function(){
                        for (let i = 0; i < allElements.length; i++) {
                            allElements[i].style.cursor = "auto";
                        }
                    })
                } catch (error) {
                    
                }
            }else{
                if(horario['mensualidad'] == "True"){
                    anterior = datosRegistro['horario'][i-1]
                    if(i > 0){
                        if(anterior['diaClase'] === horario['diaClase'] && anterior['hora'] === horario['hora']){
                            continue
                        }
                    }
                    agregarHoras(true)
                    contHorario = document.getElementById('horarios')
                    div = contHorario.children[posicion]
                    selects = div.querySelectorAll('select')
                    inputs = div.querySelectorAll('input')
                    for(let i = 0; i < selects[0].children.length; i++){
                        if(selects[0].children[i].value == horario['diaClase']){
                            selects[0].children[i].selected = true
                            selects[0].dispatchEvent(event)
                        }
                    }
                    inputs[0].value = horario['hora']
                    inputs[0].dispatchEvent(event)
                    profesor = div.lastElementChild.firstElementChild
                    new Promise((resolve, reject) =>{
                        esperarInformacion(profesor, 1000, function(){
                            for (let p = 0; p < profesor.childNodes.length; p++){
                                if(profesor.children[p].value == horario['profesor']){
                                    profesor.children[p].selected = true;
                                }
                            }
                        });
                        setTimeout(function() {
                            resolve(true)
                        }, 1000);
                    }).then(function(){
                            for (let i = 0; i < allElements.length; i++) {
                                allElements[i].style.cursor = "auto";
                            }
                    })
                    posicion = posicion + 1;
                }else{
                    for (let i = 0; i < allElements.length; i++) {
                        allElements[i].style.cursor = "auto";
                    }
                }
            }
        }
    
}

