var idCal = 0
function agregarHoras(carga=false){
 if(carga){
    let alert = document.getElementById('alertHorario')
    let padreHorario = document.getElementById('horarios')
    padreHorario.style.borderColor = 'rgb(222, 226, 230)'
    padreHorario.style.backgroundColor = '#fff'
    padreHorario.style.color = 'black'
    if (alert.className === 'alert alert-warning'){
      alert.style.display = 'none'
      padreHorario.style.borderColor = '#000000'
      padreHorario.style.backgroundColor = 'transparent'
    }
    let dias = {"1":"Lunes","2":"Martes","3":"Miércoles","4":"Jueves","5":"Viernes","6":"Sábado","0":"Domingo"}
    const divHorario = document.createElement('div');
    const contHorario = document.createElement('div');
    contHorario.style.display = 'flex'
    let divLoader = document.createElement('div')
    divLoader.style.display = 'none'
    let cloneCont = contHorario.cloneNode(true)
    let divLoader2 = divLoader.cloneNode(true)
    const inputHorario = document.createElement("input");
    inputHorario.id = "";
    inputHorario.className = "form-control";
    inputHorario.autocomplete = "off";
    inputHorario.disabled = true
    inputHorario.style.marginBottom = "5px";
    contHorario.appendChild(inputHorario)
    contHorario.appendChild(divLoader)
    let pHorario = document.createElement("label");
    pHorario.textContent = "Hora de la clase:"
    pHorario.style.textAlign = "center";
    pHorario.style.fontWeight = "bold";
    const selectProfesor = document.createElement("select");
    selectProfesor.id = "";
    selectProfesor.className = "form-select";
    selectProfesor.autocomplete = "off";
    selectProfesor.disabled = true
    cloneCont.appendChild(selectProfesor)
    cloneCont.appendChild(divLoader2)
    divHorario.style.margin = "0 5px"
    divHorario.id = "Calendario"+idCal
    idCal= idCal+1
    divHorario.style.minWidth = "150px"
    padreHorario.style.height = '210px'
    if (esporadico == false){
      padreHorario.style.height = '200px'
      padreHorario.style.overflow = "auto"
      const dateDay = document.createElement("select");
      dateDay.className = "dia";
      dateDay.classList.add("form-select")
      dateDay.style.marginBottom = "5px";
      dateDay.autocomplete = "off";
      dateDay.setAttribute("onchange", "cargarDisponibilidad(event, true)");
      let optionSelected = document.createElement("option");
      optionSelected.innerHTML = "Eliga un día"
      optionSelected.selected = true
      dateDay.appendChild(optionSelected)
      for (let i = 0; i < 7; i++) {
          let option = document.createElement("option");
          option.value = i
          option.innerHTML = dias[i]
          dateDay.appendChild(option)
      }
      let pProfe = document.createElement("label");
      pProfe.textContent = "Profesor:"
      pProfe.style.textAlign = "center";
      pProfe.style.fontWeight = "bold"; 
      if(padreHorario.childElementCount < 7){
        divHorario.appendChild(dateDay);
        divHorario.appendChild(pHorario);
        divHorario.appendChild(contHorario);
        divHorario.appendChild(pProfe);
        divHorario.appendChild(cloneCont);
        padreHorario.appendChild(divHorario);
      }
    }else{
      if(padreHorario.childElementCount < 3){
        let pDia = document.createElement("label");
        pDia.textContent = "Día de la clase:"
        pDia.style.textAlign = "center";
        pDia.style.fontWeight = "bold";
        let pProfe = document.createElement("label");
        pProfe.textContent = "Profesor:"
        pProfe.style.textAlign = "center";
        pProfe.style.fontWeight = "bold"; 
        let fecha = document.createElement("input");
        fecha.type = 'date'
        fecha.className="form-control"
        fecha.setAttribute("onchange", "cargarDisponibilidad(event, true)");
        divHorario.appendChild(pDia);
        divHorario.appendChild(fecha)
        divHorario.appendChild(pHorario);
        divHorario.appendChild(contHorario);
        divHorario.appendChild(pProfe);
        divHorario.appendChild(cloneCont);
        padreHorario.appendChild(divHorario);
      }
    }
 }else{
  let alert = document.getElementById('alertHorario')
  if (alert.innerHTML === 'No se puede poner el mismo día 2 veces.' || alert.innerHTML === 'No se puede poner el mismo día 2 veces. <i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debemos solucionar este error.</b>' || alert.className==='alert alert-danger' && alert.style.display === 'block'){
    if( alert.innerHTML.includes(' <i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debemos solucionar este error.</b>') == false){
      if (alert.innerHTML === 'No se puede poner el mismo día 2 veces.'|| alert.className==='alert alert-danger' && alert.style.display === 'block'){
        alert.innerHTML += ' <i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debemos solucionar este error.</b>'
      }
    }
  }else{
    let padreHorario = document.getElementById('horarios')
    if (padreHorario.childElementCount > 0){
      if(padreHorario.lastElementChild.children[0].value === 'Eliga un día' && padreHorario.lastElementChild.children[0].tagName === 'SELECT'){
        alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la anterior clase.</b>'
        alert.style.display = 'block'
        alert.className = 'alert alert-warning'
        return false
      }
      if (padreHorario.lastElementChild.children[1].value === '' && padreHorario.lastElementChild.children[0].tagName === 'LABEL' ){
        alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la anterior clase.</b>'
        alert.style.display = 'block'
        alert.className = 'alert alert-warning'
        return false
      }
    }
    if (alert.className === 'alert alert-warning'){
      alert.style.display = 'none'
      padreHorario.style.borderColor = '#000000'
      padreHorario.style.backgroundColor = 'transparent'
    }
    let dias = {"1":"Lunes","2":"Martes","3":"Miércoles","4":"Jueves","5":"Viernes","6":"Sábado","0":"Domingo"}
    const divHorario = document.createElement('div');
    const contHorario = document.createElement('div');
    contHorario.style.display = 'flex'
    let divLoader = document.createElement('div')
    divLoader.style.display = 'none'
    let cloneCont = contHorario.cloneNode(true)
    let divLoader2 = divLoader.cloneNode(true)
    const inputHorario = document.createElement("input");
    inputHorario.id = "";
    inputHorario.className = "form-control";
    inputHorario.autocomplete = "off";
    inputHorario.disabled = true
    inputHorario.style.marginBottom = "5px";
    contHorario.appendChild(inputHorario)
    contHorario.appendChild(divLoader)
    let pHorario = document.createElement("label");
    pHorario.textContent = "Hora de la clase:"
    pHorario.style.textAlign = "center";
    pHorario.style.fontWeight = "bold";
    const selectProfesor = document.createElement("select");
    selectProfesor.id = "";
    selectProfesor.className = "form-select";
    selectProfesor.autocomplete = "off";
    selectProfesor.disabled = true
    cloneCont.appendChild(selectProfesor)
    cloneCont.appendChild(divLoader2)
    divHorario.style.margin = "0 5px"
    divHorario.id = "Calendario"+idCal
    idCal= idCal+1
    divHorario.style.minWidth = "150px"
    padreHorario.style.height = '210px'
    if (esporadico == false){
      padreHorario.style.height = '200px'
      padreHorario.style.overflow = "auto"
      const dateDay = document.createElement("select");
      dateDay.className = "dia";
      dateDay.classList.add("form-select")
      dateDay.style.marginBottom = "5px";
      dateDay.autocomplete = "off";
      dateDay.setAttribute("onchange", "cargarDisponibilidad(event)");
      let optionSelected = document.createElement("option");
      optionSelected.innerHTML = "Eliga un día"
      optionSelected.selected = true
      dateDay.appendChild(optionSelected)
      for (let i = 0; i < 7; i++) {
          let option = document.createElement("option");
          option.value = i
          option.innerHTML = dias[i]
          dateDay.appendChild(option)
      }
      let pProfe = document.createElement("label");
      pProfe.textContent = "Profesor:"
      pProfe.style.textAlign = "center";
      pProfe.style.fontWeight = "bold"; 
      if(padreHorario.childElementCount < 7){
        divHorario.appendChild(dateDay);
        divHorario.appendChild(pHorario);
        divHorario.appendChild(contHorario);
        divHorario.appendChild(pProfe);
        divHorario.appendChild(cloneCont);
        padreHorario.appendChild(divHorario);
      }
    }else{
      if(padreHorario.childElementCount < 3){
        let pDia = document.createElement("label");
        pDia.textContent = "Día de la clase:"
        pDia.style.textAlign = "center";
        pDia.style.fontWeight = "bold";
        let pProfe = document.createElement("label");
        pProfe.textContent = "Profesor:"
        pProfe.style.textAlign = "center";
        pProfe.style.fontWeight = "bold"; 
        let fecha = document.createElement("input");
        fecha.type = 'date'
        fecha.className="form-control"
        fecha.setAttribute("onchange", "cargarDisponibilidad(event)");
        divHorario.appendChild(pDia);
        divHorario.appendChild(fecha)
        divHorario.appendChild(pHorario);
        divHorario.appendChild(contHorario);
        divHorario.appendChild(pProfe);
        divHorario.appendChild(cloneCont);
        padreHorario.appendChild(divHorario);
      }
    }
    }
 }
}
function eliminarHoras(){
  let alert = document.getElementById('alertHorario')
  alert.style.display = 'none'
  let padreHorario = document.getElementById('horarios')
  padreHorario.style.borderColor = 'rgb(222, 226, 230)'
  padreHorario.style.backgroundColor = '#fff'
  padreHorario.style.color = 'black'
  let child = document.getElementById('horarios').lastChild;
  document.getElementById('horarios').removeChild(child);
  idCal = idCal - 1
}

function cargarProfesor(e){
  let hora = e.target.parentElement
  let dia = e.target.parentElement.previousElementSibling.previousElementSibling    
  let contenedor = e.target.parentElement.nextElementSibling.nextElementSibling    
  let loader = contenedor.lastElementChild
  let picadero = document.getElementById("id_picadero")
  loader.style.display = 'block'    
  loader.className = "spinner-border"    
  loader.setAttribute('role','status')
  loader.style.marginLeft = '5px'    
  loader.style.minWidth = '31.8px'   
   loader.style.minHeight = '30px'    
   new Promise((resolve, reject) =>{
    $.ajax({
      url:getProfesorUrl,
      data: {'csrfmiddlewaretoken':csrftoken,'hora':e.target.value, 'dia':dia.value},
      type: 'POST',
      success: function(data){
       let select = contenedor.firstElementChild         
       select.innerHTML = ''          
       if (data.data.length > 0){
          data.data.forEach(function(d){
            let options = document.createElement('option')
            options.value = d.pk              
            options.innerHTML = d.nombre              
            select.appendChild(options)
          })
          let alert = document.getElementById('alertHorario')
          if(alert.className != 'alert alert-danger'){
            alert.style.display = 'none'
          }
          select.disabled = false            
          resolve(true)
        }else{
          let alert = document.getElementById('alertHorario')          
          select.disabled = true           
          alert.style.display = 'block'            
          alert.innerHTML = 'No se encontro ningún profesor.'            
          alert.className = "alert alert-warning"  
          reject(false)
        }
        loader.style.display = 'none'        }
     }).then((result) => {
      $.ajax({
        url: "/Administracion/EspaciosLibrePicadero/",
        type: "GET",
        data: {"dia":dia.value, "hora":e.target.value, "picadero":picadero.value},
        success: function (response) {
          let select = contenedor.firstElementChild 
          let alert = document.getElementById('alertHorario')
          if(alert.style.display == 'none'|| alert.className=='alert alert-info'){
            select.disabled = false         
            alert.style.display = 'block'            
            alert.innerHTML = response["conteo"]           
            alert.className = "alert alert-info"  
          }         
        },
        error: function (error) {
        }
      });
     })
  })  
}
 function cargarDisponibilidad(e, carga=false){
    let alert = document.getElementById('alertHorario')
    let contenedor = e.target.nextElementSibling.nextElementSibling
    let input = contenedor.firstElementChild
    let loader = contenedor.lastElementChild
    loader.style.display = 'block'
    loader.className = "spinner-border"
    loader.setAttribute('role','status')
    loader.style.marginLeft = '5px'
    loader.style.minWidth = '31.8px'
    loader.style.minHeight = '30px'

    let dias = {"1":"lunes","2":"martes","3":"miercoles","4":"jueves","5":"viernes","6":"sabado","0":"domingo"}
    let dia = ''
    
    if (e.target.tagName === 'INPUT'){
        dia = e.target.value    
        const fecha = new Date(dia)
        const fechaActual = new Date();
        fecha.setDate(fecha.getDate() + 1)
        if (fecha.getTime() < fechaActual.getTime()) {
            if(carga == false){
              input.disabled = true
              alert.style.display = 'block'
              alert.innerHTML = 'No se puede poner una fecha anterior al día actual.'
              alert.className = "alert alert-danger"
            }
            
        }
    }else{
        dia = dias[e.target.value]
    }   
    if(dia===undefined){
        input.disabled = true
    }else{
        if(document.getElementById('horas'+dia)===null){
            input.id = 'horas'+dia
            let Fecha = null
            if (esporadico){
              const fecha = new Date(dia)
              const fechaActual = new Date();
              Fecha = fecha.getDay()
            } 
            if (esporadico){
              datepickerHoras(Fecha,dia).then((result) => {
                input.disabled = false
                loader.style.display = 'none'
              })
            }else{
              datepickerHoras(dia).then((result) => {
                input.disabled = false
                loader.style.display = 'none'
              })
            }
            input.setAttribute("onchange", "cargarProfesor(event)");
        }else{
            input.disabled = true
            alert.style.display = 'block'
            alert.innerHTML = 'No se puede poner el mismo día 2 veces.'
            alert.className = "alert alert-danger"
            if (e.target.tagName === 'INPUT'){
                e.target.value = ''
                e.target.innerHTML = ''
            }else{
                e.target.firstElementChild.selected = true
                e.target.firstElementChild.value = ''
            }
        }
        }
    }
function serializeRegistroMatriculado(){
    return new Promise((resolve, reject) =>{
        let alert = document.getElementById('alertHorario')
        let horarios = document.getElementById('horarios')
        horarios.style.borderColor = '#000000'
        horarios.style.backgroundColor = 'transparent'
        if (horarios.classList.contains('is-invalid')){
          horarios.classList.remove('is-invalid')
        }
        let serialize = []
        if (horarios.childElementCount == 0){
            alert.style.display = 'none'
            alert.style.display = 'block'
            alert.innerHTML = 'Para continuar, es necesario contar con al menos el horario de una clase.'
            alert.className = "alert alert-warning"
            horarios.style.borderColor = '#997404'
            horarios.style.backgroundColor = 'rgb(255, 243, 205)'
        }else{
            for(let i = 0; i < horarios.children.length; i++){
                let div = horarios.children[i]
                let diaClaseHorario = ''
                if(esporadico == false){
                    diaClaseHorario = div.firstElementChild.value
                    if(diaClaseHorario === 'Eliga un día' && diaClaseHorario.tagName === 'SELECT'){
                        alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la clase.</b>'
                        alert.style.display = 'block'
                        alert.className = 'alert alert-warning'
                        return false
                    }
                }else{
                    diaClaseHorario = div.children[1].value
                    if (diaClaseHorario === '' && div.children[1].tagName === 'INPUT' ){
                        alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la clase.</b>'
                        alert.style.display = 'block'
                        alert.className = 'alert alert-warning'
                        return false
                    }
                }
                let inputs = div.querySelectorAll('input')
                let hora =  inputs[inputs.length -1]
                hora.className = 'form-control'
                if (hora.value === ''){
                    alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la clase.</b>'
                    alert.style.display = 'block'
                    alert.className = 'alert alert-warning'
                    hora.classList.add('is-invalid')
                    return false
                }
                if(div.lastElementChild.tagName === 'SUB'){
                  div.removeChild(div.lastElementChild)
                }
                let profesor = div.lastElementChild.firstElementChild.value
                if (profesor === ''){
                    alert.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <b>Antes de continuar, debes completar la informacion de la clase.</b>'
                    alert.style.display = 'block'
                    alert.className = 'alert alert-warning'
                    hora.classList.add('is-invalid')
                    return false
                }
                serialize.push({
                    'id':i,
                    'dia':diaClaseHorario,
                    'hora':hora.value,
                    'profesor':profesor
                })
            }
        }
        resolve(serialize)
    })
}